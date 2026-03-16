(function initFeedbackPage() {
  const modeToggle = document.getElementById("modeToggle");
  const body = document.body;
  const toggleButton = document.querySelector(".show-menu");
  const sidebar = document.querySelector(".links-group");

  if (!modeToggle || !toggleButton || !sidebar) {
    return;
  }

  function syncModeToggleText() {
    modeToggle.textContent = body.classList.contains("light-mode")
      ? "Dark Mode"
      : "Light Mode";
  }

  if (localStorage.getItem("theme") === "light") {
    body.classList.add("light-mode");
  }
  syncModeToggleText();

  modeToggle.addEventListener("click", () => {
    body.classList.toggle("light-mode");
    localStorage.setItem("theme", body.classList.contains("light-mode") ? "light" : "dark");
    syncModeToggleText();
  });

  toggleButton.addEventListener("click", () => {
    sidebar.classList.toggle("show");
  });

  document.dispatchEvent(new Event("souls:page-ready"));
})();
