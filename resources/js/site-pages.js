(function initSitePages() {
  const body = document.body;
  if (!body.classList.contains("content-page")) {
    return;
  }

  const modeToggle = document.getElementById("modeToggle");
  const menuToggle = document.querySelector(".show-menu");
  const currentPage = window.location.pathname.split("/").pop() || "index";
  let siteMenuOverlay = null;

  const siteMenuLinks = [
    { label: "Home", href: "index" },
    { label: "About", href: "about" },
    { label: "Elden Ring", href: "eldenring" },
    { label: "Bloodborne", href: "bloodborne" },
    { label: "Demon's Souls", href: "demonssouls" },
    { label: "Dark Souls Remastered", href: "ds1" },
    { label: "Dark Souls II: SotFS", href: "ds2" },
    { label: "Dark Souls III", href: "ds3" },
    { label: "Discord", href: "https://discord.gg/j8HHh8ffEn" },
    { label: "Github", href: "https://github.com/jadepilled/souls-fashion" },
    { label: "Feedback", href: "feedback" },
  ];
  const siteMenuSupportMessages = [
    "Make a girl smile ✨",
    "Satisfy a woman today 💦",
    "Make my day ☀️",
    "Caffeinate me ☕",
    "Support small devs 🛠️",
    "Hook me up 💸",
    "Show your love ❤️",
    "Is it Christmas? 🎅🏻",
    "Help me learn 🧪",
    "Bills don't pay themselves 💼",
    "Hosting ain't free 💻",
    "Cut me some slack ✂️",
    "A penny for my.. work? 🏆",
    "Let's break the ice 🧊",
    "The ball's in your court 🎾",
    "Your move, Maestro! ♟️",
    "Goth girls need money too 🖤",
    "Gotta get tattoos somehow 🖋️",
    "Pretty please? 🥺👉👈",
    "A gal's gotta eat 🍒",
    "Luck of the Irish 🍀",
    "You're a star 🌟",
    "Budgeting is hard 🥀",
    "Surrender ye booty 💀",
    "I vvaaanntt youur moonneyy 🩸🧛‍",
    "Lets make magic 🔮",
    "Weed's expensive man 🌱",
    "Powered by rainbows 🌈",
  ];

  function getRandomSupportMessage() {
    const storageKey = "siteMenuSupportMessageIndex";
    let lastIndex = -1;

    try {
      lastIndex = Number(localStorage.getItem(storageKey));
    } catch (error) {
      lastIndex = -1;
    }

    if (siteMenuSupportMessages.length === 1) {
      return siteMenuSupportMessages[0];
    }

    let nextIndex = Math.floor(Math.random() * siteMenuSupportMessages.length);
    if (siteMenuSupportMessages.length > 1) {
      while (nextIndex === lastIndex) {
        nextIndex = Math.floor(Math.random() * siteMenuSupportMessages.length);
      }
    }

    try {
      localStorage.setItem(storageKey, String(nextIndex));
    } catch (error) {
      // Ignore storage failures and continue with the current message.
    }

    return siteMenuSupportMessages[nextIndex];
  }

  function normalizePage(value) {
    return (value || "index").replace(/\.html$/, "");
  }

  function updateModeToggleIcon() {
    if (!modeToggle) {
      return;
    }

    const isLightMode = body.classList.contains("light-mode");
    modeToggle.textContent = "\u25d0";
    modeToggle.setAttribute(
      "aria-label",
      isLightMode ? "Switch to dark mode" : "Switch to light mode"
    );
    modeToggle.title = isLightMode ? "Switch to dark mode" : "Switch to light mode";
  }

  function getThemeIconPath() {
    return body.classList.contains("light-mode")
      ? "icons/FS_icon_black.png"
      : "icons/FS_icon_white.png";
  }

  function updateBrandIcon() {
    document.querySelectorAll(".content-brand-icon").forEach((icon) => {
      icon.src = getThemeIconPath();
    });

    window.SoulsPageTransition?.setThemeIcon?.(body.classList.contains("light-mode"));
  }

  function setSiteMenuOpen(open) {
    const shouldOpen = Boolean(open);
    body.classList.toggle("site-menu-open", shouldOpen);

    if (menuToggle) {
      menuToggle.setAttribute("aria-expanded", shouldOpen ? "true" : "false");
    }

    if (siteMenuOverlay) {
      siteMenuOverlay.setAttribute("aria-hidden", shouldOpen ? "false" : "true");
    }
  }

  function buildSiteMenu() {
    if (!menuToggle || siteMenuOverlay) {
      return;
    }

    menuToggle.setAttribute("type", "button");
    menuToggle.setAttribute("aria-label", "Toggle navigation menu");
    menuToggle.setAttribute("aria-expanded", "false");
    menuToggle.innerHTML =
      '<span class="menu-toggle-bar top"></span><span class="menu-toggle-bar middle"></span><span class="menu-toggle-bar bottom"></span>';

    const currentNormalized = normalizePage(currentPage);
    const linksMarkup = siteMenuLinks
      .map((link) => {
        const target =
          !/^https?:/i.test(link.href) && normalizePage(link.href) === currentNormalized
            ? ' aria-current="page"'
            : "";
        return `<li><a href="${link.href}" class="site-menu-link"${target}>${link.label}</a></li>`;
      })
      .join("");

    siteMenuOverlay = document.createElement("aside");
    siteMenuOverlay.className = "site-menu-overlay";
    siteMenuOverlay.id = "siteMenuOverlay";
    siteMenuOverlay.setAttribute("aria-hidden", "true");
    siteMenuOverlay.innerHTML = `
      <button class="site-menu-backdrop" type="button" aria-label="Close menu"></button>
      <div class="site-menu-shell">
        <section class="site-menu-panel site-menu-panel--support">
          <div class="site-menu-support-copy">
		    <p>${getRandomSupportMessage()}</p><p>Please consider supporting this project's ongoing existence if it has been useful to you.</p>
            <a href="https://ko-fi.com/psyopgirl" class="site-menu-donate">Donate</a>
          </div>
        </section>
        <section class="site-menu-panel site-menu-panel--links">
          <ul class="site-menu-link-list">
            ${linksMarkup}
          </ul>
        </section>
      </div>
    `;

    document.body.appendChild(siteMenuOverlay);

    menuToggle.addEventListener("click", () => {
      setSiteMenuOpen(!body.classList.contains("site-menu-open"));
    });

    siteMenuOverlay.querySelector(".site-menu-backdrop").addEventListener("click", () => {
      setSiteMenuOpen(false);
    });

    siteMenuOverlay.querySelectorAll(".site-menu-link, .site-menu-donate").forEach((link) => {
      link.addEventListener("click", () => {
        setSiteMenuOpen(false);
      });
    });
  }

  function navigateWithTransition(action) {
    document.body.classList.add("page-is-transitioning");
    window.SoulsPageTransition?.show();
    window.setTimeout(action, 180);
  }

  function initBackButtons() {
    document.querySelectorAll("[data-go-back]").forEach((button) => {
      button.addEventListener("click", () => {
        const fallback = button.dataset.fallback || "index";
        if (window.history.length > 1) {
          navigateWithTransition(() => {
            window.history.back();
          });
          return;
        }

        navigateWithTransition(() => {
          window.location.href = fallback;
        });
      });
    });
  }

  if (localStorage.getItem("theme") === "light") {
    body.classList.add("light-mode");
  }

  buildSiteMenu();
  initBackButtons();
  updateModeToggleIcon();
  updateBrandIcon();

  if (modeToggle) {
    modeToggle.addEventListener("click", () => {
      body.classList.toggle("light-mode");
      localStorage.setItem("theme", body.classList.contains("light-mode") ? "light" : "dark");
      updateModeToggleIcon();
      updateBrandIcon();
    });
  }

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      setSiteMenuOpen(false);
    }
  });

  if (!body.classList.contains("index-page") && !body.classList.contains("simulator-page")) {
    document.dispatchEvent(new Event("souls:page-ready"));
  }
})();
