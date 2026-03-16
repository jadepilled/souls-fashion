(function initPageTransitions() {
  function getThemeIconSrc(isLightMode = null) {
    const resolvedLightMode =
      typeof isLightMode === "boolean"
        ? isLightMode
        : document.body?.classList.contains("light-mode") ||
          localStorage.getItem("theme") === "light";

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

  function getPreloader() {
    if (!preloader) {
      preloader = ensurePreloader();
    }
    return preloader;
  }

  function setPreloaderIcon(isLightMode = null) {
    const overlay = getPreloader();
    const logo = overlay.querySelector(".preloader-logo");
    if (logo) {
      logo.src = getThemeIconSrc(isLightMode);
    }
  }

  function showPreloader() {
    const overlay = getPreloader();
    setPreloaderIcon();
    overlay.classList.remove("hidden");
    document.body.classList.add("preloader-visible");
  }

  function hidePreloader() {
    const overlay = getPreloader();
    ready = true;
    overlay.classList.add("hidden");
    document.body.classList.remove("preloader-visible");
    document.body.classList.remove("page-is-transitioning");
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
    navigationTimer = window.setTimeout(() => {
      window.location.href = href;
    }, 180);
  }

  document.addEventListener("DOMContentLoaded", () => {
    setPreloaderIcon();
    showPreloader();
  });

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
      showPreloader();
      navigateTo(link.href);
    },
    true
  );

  document.addEventListener("souls:page-ready", markReady);
  window.addEventListener("pageshow", () => {
    clearTimeout(navigationTimer);
    navigating = false;
    setPreloaderIcon();
    if (ready) {
      hidePreloader();
    } else {
      showPreloader();
    }
  });

  window.addEventListener("beforeunload", () => {
    if (!navigating) {
      document.body.classList.add("page-is-transitioning");
      showPreloader();
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
