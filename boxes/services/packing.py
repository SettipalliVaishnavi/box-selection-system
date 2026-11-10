"""
Pure-Python box selection logic (no Django imports, so it is easy to unit test).

Approach
--------
1. Expand each order line into individual items (quantity N -> N items).
2. For every candidate box run cheap rejection checks first:
     - total weight <= box.max_weight
     - total item volume <= box volume
     - every single item fits the box in at least one of its 6 orientations
3. For boxes that pass, run a heuristic 3D packer ("extreme points" with
   rotation) to prove the items physically fit.
4. Among boxes that really fit, choose the CHEAPEST. Ties are broken by the
   smaller internal volume, then by the smaller box id/name for determinism.

Limitations (documented honestly)
---------------------------------
3D bin packing is NP-hard. The packer is a greedy heuristic: if it says an
order fits, it DOES fit (placements are checked for overlap and bounds), but it
may occasionally say "does not fit" for a tight arrangement that a perfect
solver would find. It therefore errs on the safe side. It also assumes
rigid cuboid items, no stacking/fragility rules, and no packing material.
"""
from dataclasses import dataclass, field
from decimal import Decimal
from itertools import permutations
from typing import Iterable, List, Optional, Sequence, Tuple

ZERO = Decimal("0")

# The packer is a greedy heuristic whose cost grows quickly with item count.
# Orders larger than this should be split into several parcels first.
MAX_ITEMS_PER_ORDER = 100


@dataclass(frozen=True)
class Item:
    label: str
    length: Decimal
    width: Decimal
    height: Decimal
    weight: Decimal

    @property
    def volume(self) -> Decimal:
        return self.length * self.width * self.height

    def orientations(self) -> List[Tuple[Decimal, Decimal, Decimal]]:
        return sorted(set(permutations((self.length, self.width, self.height))))


@dataclass(frozen=True)
class BoxSpec:
    id: int
    name: str
    length: Decimal
    width: Decimal
    height: Decimal
    max_weight: Decimal
    cost: Decimal

    @property
    def volume(self) -> Decimal:
        return self.length * self.width * self.height


@dataclass
class BoxEvaluation:
    box: BoxSpec
    fits: bool
    reason: str = ""


@dataclass
class Recommendation:
    box: Optional[BoxSpec]
    total_weight: Decimal
    total_volume: Decimal
    evaluations: List[BoxEvaluation] = field(default_factory=list)
    message: str = ""


class PackingError(ValueError):
    pass


def _dec(v) -> Decimal:
    return v if isinstance(v, Decimal) else Decimal(str(v))


def _overlaps(a, b) -> bool:
    ax, ay, az, al, aw, ah = a
    bx, by, bz, bl, bw, bh = b
    return not (
        ax + al <= bx or bx + bl <= ax
        or ay + aw <= by or by + bw <= ay
        or az + ah <= bz or bz + bh <= az
    )


def can_pack(items: Sequence[Item], box: BoxSpec) -> bool:
    """Heuristic proof that every item can be placed inside the box."""
    if not items:
        return True
    # Largest first gives the greedy packer the best chance.
    ordered = sorted(items, key=lambda i: i.volume, reverse=True)
    placed: List[Tuple[Decimal, ...]] = []
    points = [(ZERO, ZERO, ZERO)]

    for item in ordered:
        placement = None
        # Prefer low, then back, then left positions to keep space compact.
        for (px, py, pz) in sorted(set(points), key=lambda p: (p[2], p[1], p[0])):
            for (l, w, h) in item.orientations():
                if px + l > box.length or py + w > box.width or pz + h > box.height:
                    continue
                candidate = (px, py, pz, l, w, h)
                if any(_overlaps(candidate, p) for p in placed):
                    continue
                placement = candidate
                break
            if placement:
                break
        if placement is None:
            return False
        placed.append(placement)
        x, y, z, l, w, h = placement
        points.extend([(x + l, y, z), (x, y + w, z), (x, y, z + h)])
    return True


def _evaluate(items: Sequence[Item], box: BoxSpec, total_weight: Decimal, total_volume: Decimal) -> BoxEvaluation:
    if total_weight > box.max_weight:
        return BoxEvaluation(box, False, "total weight exceeds box capacity")
    if total_volume > box.volume:
        return BoxEvaluation(box, False, "total item volume exceeds box volume")
    box_dims = sorted((box.length, box.width, box.height))
    for it in items:
        item_dims = sorted((it.length, it.width, it.height))
        if any(i > b for i, b in zip(item_dims, box_dims)):
            return BoxEvaluation(box, False, f"item '{it.label}' is too large for this box")
    if not can_pack(items, box):
        return BoxEvaluation(box, False, "items could not be arranged inside the box")
    return BoxEvaluation(box, True, "fits")


def recommend_box(items: Iterable[Item], boxes: Iterable[BoxSpec]) -> Recommendation:
    items = list(items)
    boxes = list(boxes)
    if not items:
        raise PackingError("Order has no items.")
    if len(items) > MAX_ITEMS_PER_ORDER:
        raise PackingError(
            f"Order has {len(items)} items; the limit is {MAX_ITEMS_PER_ORDER}. Split it into several parcels."
        )
    for it in items:
        if min(it.length, it.width, it.height, it.weight) <= 0:
            raise PackingError(f"Item '{it.label}' has non-positive dimensions or weight.")

    total_weight = sum((i.weight for i in items), ZERO)
    total_volume = sum((i.volume for i in items), ZERO)

    evaluations = [_evaluate(items, b, total_weight, total_volume) for b in boxes]
    fitting = [e for e in evaluations if e.fits]

    if not boxes:
        return Recommendation(None, total_weight, total_volume, evaluations, "No boxes are available.")
    if not fitting:
        return Recommendation(None, total_weight, total_volume, evaluations,
                              "No single box can hold this order. It needs to be split into multiple parcels.")

    best = min(fitting, key=lambda e: (e.box.cost, e.box.volume, e.box.id))
    return Recommendation(best.box, total_weight, total_volume, evaluations,
                          "Cheapest box that fits all items.")
