const API_URL = "http://127.0.0.1:8000";

document.addEventListener("DOMContentLoaded", loadOffers);
document.getElementById("createOfferForm").addEventListener("submit", createOffer);

async function loadOffers() {
  const container = document.getElementById("offersContainer");
  container.innerHTML = "";
  try {
    const res = await fetch(`${API_URL}/offers/`);
    const data = await res.json();
    data.forEach(offer => {
      container.innerHTML += `
        <div class="col-md-4 mb-4">
          <div class="card shadow-sm border-success h-100">
            <div class="card-body">
              <h5 class="card-title text-success">${offer.title}</h5>
              <p>${offer.description || "Sin descripción"}</p>
              <p><strong>Presupuesto:</strong> ${offer.budget_cop || "N/A"} COP</p>
            </div>
          </div>
        </div>`;
    });
  } catch (err) {
    console.error(err);
    container.innerHTML = "<p class='text-danger'>Error al cargar ofertas.</p>";
  }
}

async function createOffer(e) {
  e.preventDefault();
  const form = e.target;
  const data = Object.fromEntries(new FormData(form));

  try {
    const res = await fetch(`${API_URL}/offers/`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    });
    if (res.ok) {
      alert("Oferta publicada ✅");
      form.reset();
      loadOffers();
    } else {
      alert("Error al publicar oferta ❌");
    }
  } catch (err) {
    console.error(err);
  }
}
