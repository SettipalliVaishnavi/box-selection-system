(function () {
  "use strict";

  var MAX_QTY = 100;
  var rows = Array.prototype.slice.call(document.querySelectorAll(".row[data-sku]"));
  var goBtn = document.getElementById("go");
  var clearBtn = document.getElementById("clear");
  var result = document.getElementById("result");

  function qtyOf(row) {
    var n = parseInt(row.querySelector("input").value, 10);
    return isNaN(n) || n < 0 ? 0 : Math.min(n, MAX_QTY);
  }

  function selectedItems() {
    return rows
      .map(function (r) { return { sku: r.dataset.sku, quantity: qtyOf(r) }; })
      .filter(function (i) { return i.quantity > 0; });
  }

  function updateButton() {
    goBtn.disabled = selectedItems().length === 0;
  }

  function esc(text) {
    var d = document.createElement("div");
    d.textContent = String(text);
    return d.innerHTML;
  }

  function showError(message) {
    result.innerHTML = '<div class="card none"><strong>Error:</strong> ' + esc(message) + "</div>";
  }

  function render(data) {
    var box = data.recommended_box;
    var head = box
      ? '<div class="card pick"><div class="meta">Recommended box</div>' +
        '<div class="big">' + esc(box.name) + "</div>" +
        "<div>Cost " + esc(box.cost) + " · inside " + box.internal_dimensions_cm.map(esc).join(" × ") +
        " cm · max " + esc(box.max_weight_kg) + " kg</div>"
      : '<div class="card none"><div class="big">No single box fits</div><div>' + esc(data.message) + "</div>";

    var details = data.evaluations.map(function (e) {
      return "<tr><td>" + esc(e.box) + '</td><td class="' + (e.fits ? "ok" : "bad") + '">' +
             (e.fits ? "Fits" : "No") + "</td><td>" + esc(e.reason) + "</td></tr>";
    }).join("");

    result.innerHTML = head +
      '<div class="meta totals">Order total: ' + esc(data.total_weight_kg) + " kg · " +
      esc(data.total_volume_cm3) + " cm³</div>" +
      "<table><thead><tr><th>Box</th><th>Result</th><th>Why</th></tr></thead><tbody>" +
      details + "</tbody></table></div>";
  }

  rows.forEach(function (row) {
    var input = row.querySelector("input");
    Array.prototype.forEach.call(row.querySelectorAll("button[data-step]"), function (btn) {
      btn.addEventListener("click", function () {
        input.value = Math.min(MAX_QTY, Math.max(0, qtyOf(row) + parseInt(btn.dataset.step, 10)));
        updateButton();
      });
    });
    input.addEventListener("input", updateButton);
  });

  clearBtn.addEventListener("click", function () {
    rows.forEach(function (r) { r.querySelector("input").value = 0; });
    result.innerHTML = "";
    updateButton();
  });

  goBtn.addEventListener("click", function () {
    goBtn.disabled = true;
    goBtn.textContent = "Working…";
    fetch("/api/recommend-box/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ items: selectedItems() })
    })
      .then(function (res) {
        return res.json().then(function (data) { return { ok: res.ok, data: data }; });
      })
      .then(function (r) {
        if (r.ok) { render(r.data); } else { showError(r.data.error || "Something went wrong."); }
      })
      .catch(function () { showError("Could not reach the server."); })
      .then(function () {
        goBtn.textContent = "Recommend box";
        updateButton();
      });
  });
})();
