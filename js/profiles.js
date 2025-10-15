const API_URL = "http://127.0.0.1:8000";

document.addEventListener("DOMContentLoaded", loadProfiles);
document.getElementById("createProfileForm").addEventListener("submit", createProfile);

async function loadProfiles() {
  const container = document.getElementById("profilesContainer");
  container.innerHTML = "";
  try {
    const res = await fetch(`${API_URL}/profiles/`);
    const data = await res.json();
    data.forEach(profile => {
      container.innerHTML += `
        <div class="col-md-4 mb-4">
          <div class="card shadow-sm h-100">
            <div class="card-body">
              <h5 class="card-title text-primary">${profile.full_name}</h5>
              <p class="card-text">${profile.profession || "Sin profesión"}</p>
              <p class="text-muted">${profile.city || ""}</p>
              <p>${profile.bio || ""}</p>
            </div>
          </div>
        </div>`;
    });
  } catch (err) {
    console.error(err);
    container.innerHTML = "<p class='text-danger'>Error al cargar perfiles.</p>";
  }
}

async function createProfile(e) {
  e.preventDefault();
  const form = e.target;
  const data = Object.fromEntries(new FormData(form));
  data.role = "client";

  try {
    const res = await fetch(`${API_URL}/profiles/`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    });
    if (res.ok) {
      alert("Perfil creado ✅");
      form.reset();
      loadProfiles();
    } else {
      alert("Error al crear perfil ❌");
    }
  } catch (err) {
    console.error(err);
  }
}
