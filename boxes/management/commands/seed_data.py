from django.core.management.base import BaseCommand

from boxes.models import Box, Order, OrderItem, Product

PRODUCTS = [
    ("BOOK-01", "Paperback book", 20, 13, 3, "0.4"),
    ("MUG-01", "Ceramic mug", 10, 10, 11, "0.35"),
    ("SHOE-01", "Sneakers (boxed)", 33, 22, 12, "0.9"),
    ("LAPTOP-01", "Laptop 14in", 33, 23, 2, "1.4"),
    ("DUMBBELL-01", "Dumbbell 10kg", 30, 12, 12, "10.0"),
]
BOXES = [
    ("Small", 25, 18, 10, "2", "10.00"),
    ("Medium", 35, 25, 15, "8", "18.00"),
    ("Large", 50, 40, 30, "20", "35.00"),
]


class Command(BaseCommand):
    help = "Load sample products, boxes and an example order."

    def handle(self, *args, **opts):
        for sku, name, l, w, h, wt in PRODUCTS:
            Product.objects.get_or_create(sku=sku, defaults=dict(name=name, length=l, width=w, height=h, weight=wt))
        for name, l, w, h, mw, cost in BOXES:
            Box.objects.get_or_create(name=name, defaults=dict(length=l, width=w, height=h, max_weight=mw, cost=cost))
        order, created = Order.objects.get_or_create(reference="ORD-1001")
        if created:
            OrderItem.objects.create(order=order, product=Product.objects.get(sku="BOOK-01"), quantity=2)
            OrderItem.objects.create(order=order, product=Product.objects.get(sku="MUG-01"), quantity=1)
        self.stdout.write(self.style.SUCCESS("Sample data loaded. Try order ORD-1001."))
