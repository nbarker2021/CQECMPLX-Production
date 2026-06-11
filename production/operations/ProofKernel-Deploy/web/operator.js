const health = document.querySelector("#health");
const tokenInput = document.querySelector("#tokenInput");
const receipt = document.querySelector("#receipt");
const training = document.querySelector("#training");
const localFull = document.querySelector("#localFull");
const modules = document.querySelector("#modules");
const events = document.querySelector("#events");
const docker = document.querySelector("#docker");
const proofs = document.querySelector("#proofs");
const repoForms = document.querySelector("#repoForms");
const packageManifest = document.querySelector("#packageManifest");

async function api(path, options = {}) {
  const response = await fetch(path, {
    headers: {"content-type": "application/json"},
    ...options,
  });
  const payload = await response.json();
  if (!response.ok) throw new Error(payload.error || response.statusText);
  return payload;
}

function item(title, detail) {
  const node = document.createElement("div");
  node.className = "item";
  node.innerHTML = `<strong></strong><span class="muted"></span>`;
  node.querySelector("strong").textContent = title;
  node.querySelector("span").textContent = detail;
  return node;
}

async function loadHealth() {
  const payload = await api("/api/health");
  const auth = payload.security.auth_required ? "auth on" : "local open";
  health.textContent = `${payload.status} · ${payload.kernel} · ${auth}`;
}

async function loadModules() {
  const payload = await api("/api/modules");
  modules.replaceChildren();
  for (const mod of payload.modules) {
    modules.appendChild(item(mod.title, `${mod.kind} · ${mod.status} · ${mod.capabilities.join(", ")}`));
  }
}

async function loadEvents() {
  const payload = await api("/api/events?limit=12");
  events.replaceChildren();
  for (const event of payload.events) {
    events.appendChild(item(`${event.id} · ${event.event_type}`, `${event.module_id || "kernel"} · ${event.token_sha256 || "no token"}`));
  }
}

async function loadDocker() {
  const status = await api("/api/docker/status");
  const inventory = await api("/api/docker/inventory");
  docker.replaceChildren();
  docker.appendChild(item("Docker", `${status.docker.ok ? status.docker.stdout : status.docker.stderr}`));
  docker.appendChild(item("Compose", `${status.compose.ok ? status.compose.stdout : status.compose.stderr}`));
  docker.appendChild(item("Control", status.control_enabled ? "enabled" : "read-only"));
  docker.appendChild(item("Compose files", `${inventory.compose_files.length}`));
}

async function loadProofs() {
  const payload = await api("/api/proofs");
  proofs.replaceChildren();
  for (const doc of payload.docs.slice(0, 16)) {
    proofs.appendChild(item(doc.relative_path, `${doc.bytes} bytes`));
  }
}

async function loadRepoForms() {
  const payload = await api("/api/repo-forms");
  repoForms.replaceChildren();
  for (const repo of payload.repos.slice(0, 16)) {
    repoForms.appendChild(item(repo.repo, `${repo.bytes} bytes`));
  }
}

async function loadPackage() {
  const payload = await api("/api/package/manifest?limit=16");
  packageManifest.replaceChildren();
  for (const row of payload.rows) {
    packageManifest.appendChild(item(row.RelativePath, `${row.Bytes} bytes`));
  }
}

async function runKernel() {
  const kernel_options = {
    training_mode: training.checked || localFull.checked,
    require_guess_mode: localFull.checked,
  };
  const payload = await api("/api/process", {
    method: "POST",
    body: JSON.stringify({
      token_string: tokenInput.value,
      task: "operator_console",
      host: "operator-web",
      kernel_options,
    }),
  });
  receipt.textContent = JSON.stringify(payload, null, 2);
  await loadEvents();
}

document.querySelector("#run").addEventListener("click", runKernel);
document.querySelector("#copy").addEventListener("click", () => navigator.clipboard.writeText(receipt.textContent));
document.querySelector("#refreshModules").addEventListener("click", loadModules);
document.querySelector("#refreshEvents").addEventListener("click", loadEvents);
document.querySelector("#refreshDocker").addEventListener("click", loadDocker);
document.querySelector("#refreshProofs").addEventListener("click", loadProofs);
document.querySelector("#refreshRepoForms").addEventListener("click", loadRepoForms);
document.querySelector("#refreshPackage").addEventListener("click", loadPackage);

Promise.all([loadHealth(), loadModules(), loadEvents(), loadDocker(), loadProofs(), loadRepoForms(), loadPackage()]).catch((error) => {
  health.textContent = error.message;
});
