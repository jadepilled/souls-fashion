(function initPageTransitions() {
  const TRANSITION_STORAGE_KEY = "soulsNavigationPending";
  const TRANSITION_STORAGE_TTL = 12000;

  function resolveLightMode(isLightMode = null) {
    return typeof isLightMode === "boolean"
      ? isLightMode
      : document.body?.classList.contains("light-mode") ||
          localStorage.getItem("theme") === "light";
  }

  function getThemeIconSrc(isLightMode = null) {
    const resolvedLightMode = resolveLightMode(isLightMode);

    return resolvedLightMode ? "icons/FS_icon_black.png" : "icons/FS_icon_white.png";
  }

  function ensurePreloader() {
    let preloader = document.getElementById("preloader");
    if (preloader) {
      return preloader;
    }

    preloader = document.createElement("div");
    preloader.id = "preloader";
    preloader.className = "preloader";

    const logo = document.createElement("img");
    logo.src = getThemeIconSrc();
    logo.alt = "souls.fashion";
    logo.className = "preloader-logo";
    preloader.appendChild(logo);

    if (document.body.firstChild) {
      document.body.insertBefore(preloader, document.body.firstChild);
    } else {
      document.body.appendChild(preloader);
    }

    return preloader;
  }

  function isNavigableLink(link, event) {
    if (!link || event.defaultPrevented) {
      return false;
    }

    if (link.target && link.target !== "_self") {
      return false;
    }

    if (link.hasAttribute("download")) {
      return false;
    }

    if (
      event.button !== 0 ||
      event.metaKey ||
      event.ctrlKey ||
      event.shiftKey ||
      event.altKey
    ) {
      return false;
    }

    const href = link.getAttribute("href");
    if (!href || href.startsWith("#") || href.startsWith("javascript:")) {
      return false;
    }

    const targetUrl = new URL(link.href, window.location.href);
    const currentUrl = new URL(window.location.href);

    if (
      targetUrl.origin === currentUrl.origin &&
      targetUrl.pathname === currentUrl.pathname &&
      targetUrl.search === currentUrl.search &&
      targetUrl.hash === currentUrl.hash
    ) {
      return false;
    }

    return true;
  }

  let preloader = null;
  let ready = false;
  let navigating = false;
  let navigationTimer = null;
  let initialized = false;

  function getPreloader() {
    if (!preloader) {
      preloader = ensurePreloader();
    }
    return preloader;
  }

  function hasPendingTransition() {
    try {
      const lastTransition = Number(sessionStorage.getItem(TRANSITION_STORAGE_KEY));
      return Number.isFinite(lastTransition) && Date.now() - lastTransition < TRANSITION_STORAGE_TTL;
    } catch (error) {
      return false;
    }
  }

  function setPendingTransition(active) {
    try {
      if (active) {
        sessionStorage.setItem(TRANSITION_STORAGE_KEY, String(Date.now()));
      } else {
        sessionStorage.removeItem(TRANSITION_STORAGE_KEY);
      }
    } catch (error) {
      // Ignore storage failures and continue with the transition.
    }
  }

  function setPreloaderIcon(isLightMode = null) {
    const overlay = getPreloader();
    const resolvedLightMode = resolveLightMode(isLightMode);
    overlay.classList.toggle("light-mode", resolvedLightMode);
    const logo = overlay.querySelector(".preloader-logo");
    if (logo) {
      logo.src = getThemeIconSrc(resolvedLightMode);
    }
  }

  function showPreloader(options = {}) {
    const { persistState = false } = options;
    const overlay = getPreloader();
    setPreloaderIcon();
    overlay.classList.remove("hidden");
    document.body.classList.add("preloader-visible");

    if (persistState) {
      setPendingTransition(true);
    }
  }

  function hidePreloader() {
    const overlay = getPreloader();
    ready = true;
    overlay.classList.add("hidden");
    document.body.classList.remove("preloader-visible");
    document.body.classList.remove("page-is-transitioning");
    setPendingTransition(false);
  }

  function markReady() {
    if (ready) {
      hidePreloader();
      return;
    }

    window.requestAnimationFrame(() => {
      hidePreloader();
    });
  }

  function navigateTo(href) {
    clearTimeout(navigationTimer);
    setPendingTransition(true);
    navigationTimer = window.setTimeout(() => {
      window.location.href = href;
    }, 180);
  }

  function initializePreloader() {
    if (initialized || !document.body) {
      return;
    }

    initialized = true;
    setPreloaderIcon();
    showPreloader();
  }

  initializePreloader();
  document.addEventListener("DOMContentLoaded", initializePreloader, { once: true });

  document.addEventListener(
    "click",
    (event) => {
      const link = event.target.closest("a[href]");
      if (!isNavigableLink(link, event)) {
        return;
      }

      navigating = true;
      event.preventDefault();
      document.body.classList.add("page-is-transitioning");
      showPreloader({ persistState: true });
      navigateTo(link.href);
    },
    true
  );

  document.addEventListener("souls:page-ready", markReady);
  window.addEventListener("pageshow", (event) => {
    clearTimeout(navigationTimer);
    navigating = false;
    setPreloaderIcon();

    if (event.persisted && ready) {
      hidePreloader();
      return;
    }

    if (!ready || hasPendingTransition()) {
      showPreloader();
      return;
    }

    hidePreloader();
  });

  window.addEventListener("beforeunload", () => {
    if (!navigating) {
      document.body.classList.add("page-is-transitioning");
      showPreloader({ persistState: true });
    }
  });

  window.addEventListener(
    "load",
    () => {
      window.setTimeout(() => {
        if (!ready) {
          markReady();
        }
      }, 5000);
    },
    { once: true }
  );

  window.SoulsPageTransition = {
    markReady,
    show: showPreloader,
    hide: hidePreloader,
    setThemeIcon: setPreloaderIcon,
  };
})();
