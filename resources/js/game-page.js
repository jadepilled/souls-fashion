(function initGamePage() {
  const currentPage =
    typeof page !== "undefined"
      ? page
      : window.location.pathname.split("/").pop().replace(/\.html$/, "");

  window.gamePrefix = `${currentPage}_`;

  const modeToggle = document.getElementById("modeToggle");
  const body = document.body;
  const toggleSearch = document.getElementById("toggleSearch");
  const colorPicker = document.getElementById("favcolor");
  const colorPickerGroup = colorPicker?.closest(".color-picker-group");
  const searchInput = document.getElementById("searchInput");
  const nav = document.querySelector(".navigation");
  const topnav = document.querySelector(".topnav");
  const toggleButton = document.querySelector(".show-menu");
  const sidebar = document.querySelector(".links-group");
  const brandLink = document.querySelector(".FashionSouls-nav");
  const itemGrid = document.querySelector(".item-grid");
  const exportButton = document.getElementById("export");

  let navActive = true;
  let sidebarActive = false;
  let scrollRafId = null;
  let currentDesktopGridColumns = 6;
  let currentMobileGridColumns = 2;
  let activeScrollTarget = null;
  let pageScrollRegion = null;
  let siteMenuOverlay = null;
  let rightClickedSlotId = null;
  let rightClickedItem = null;
  let mobileActionSheet = null;
  let mobileActionSheetTitle = null;
  let mobileActionSheetSubtitle = null;
  let mobileActionSheetActions = null;
  let mobileActionSheetBackdrop = null;
  let colorPickerTrigger = null;
  let colorPickerPopover = null;
  let colorPickerHexInput = null;
  let desktopSlotContextMenu = null;
  let desktopSlotContextBody = null;
  let desktopSlotContextTitle = null;
  let desktopSlotContextSubtitle = null;
  let desktopSlotContextActions = null;
  let activeDesktopSlotMode = "replace";
  let activeDesktopSlotId = "";
  let activeDesktopSlotItem = null;
  let activeDesktopSlotSearch = "";
  const MOBILE_GRID_MIN = 2;
  const MOBILE_GRID_MAX = 16;
  const desktopGridLevels = Array.from(
    { length: MOBILE_GRID_MAX - MOBILE_GRID_MIN + 1 },
    (_, index) => index + MOBILE_GRID_MIN
  );
  const desktopContextColorMatchWeight = 0.35;
  const slotLabels = {
    head: "Head",
    chest: "Chest",
    hands: "Hands",
    legs: "Legs",
    weapons: "Weapons",
    shields: "Shields",
  };
  const desktopColorPresets = [
    "#ffffff",
    "#000000",
    "#d1b388",
    "#9b4536",
    "#4f5966",
    "#7b7b7b",
  ];
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

  function isMobileViewport() {
    return window.matchMedia("(max-width: 1199px)").matches;
  }

  function setMobileSidebarVisible(visible) {
    if (!isMobileViewport()) {
      body.classList.remove("mobile-sidebar-visible");
      sidebarActive = false;
      navActive = true;
      return;
    }

    body.classList.toggle("mobile-sidebar-visible", visible);
    sidebarActive = visible;
    navActive = !visible;
  }

  function showOutfitSidebar() {
    setMobileSidebarVisible(true);
  }

  function hideOutfitSidebar() {
    setMobileSidebarVisible(false);
  }

  function showNav() {
    if (isMobileViewport()) {
      return;
    }

    nav.classList.remove("hidden-on-scroll");
  }

  function hideNav() {
    if (isMobileViewport()) {
      return;
    }

    nav.classList.add("hidden-on-scroll");
  }

  function adjustPinnedStyles() {
    if (!window.matchMedia("(min-width: 0px) and (max-width: 1199px)").matches && itemGrid) {
      const scale = window.devicePixelRatio;
      itemGrid.style.marginLeft = scale >= 1.25 ? "4rem" : "6rem";
    }
  }

  function ensurePageScrollRegion() {
    if (pageScrollRegion) {
      return pageScrollRegion;
    }

    pageScrollRegion = document.createElement("div");
    pageScrollRegion.className = "page-scroll-region";

    const nodesToMove = [".FashionSouls", ".hover-trigger", ".item-grid", ".footer"];
    nav.insertAdjacentElement("afterend", pageScrollRegion);

    nodesToMove.forEach((selector) => {
      const node = document.querySelector(selector);
      if (node) {
        pageScrollRegion.appendChild(node);
      }
    });

    body.classList.add("game-page");
    return pageScrollRegion;
  }

  function updatePageScrollOffset() {
    document.documentElement.style.setProperty("--page-scroll-top", `${nav.offsetHeight || 0}px`);
  }

  function getScrollHost() {
    return !isMobileViewport() ? ensurePageScrollRegion() : window;
  }

  function bindScrollHost() {
    const nextScrollTarget = getScrollHost();
    if (activeScrollTarget === nextScrollTarget) {
      return;
    }

    if (activeScrollTarget) {
      activeScrollTarget.removeEventListener("scroll", onScroll);
    }

    activeScrollTarget = nextScrollTarget;
    activeScrollTarget.addEventListener("scroll", onScroll, { passive: true });
  }

  function getScrollTop() {
    if (!isMobileViewport()) {
      return ensurePageScrollRegion().scrollTop;
    }

    return Math.max(window.scrollY || window.pageYOffset || 0, 0);
  }

  function scrollPageToTop(behavior = "smooth") {
    if (!isMobileViewport()) {
      ensurePageScrollRegion().scrollTo({ top: 0, behavior });
      return;
    }

    window.scrollTo({ top: 0, behavior });
  }

  function estimateDesktopCardWidth(columns) {
    const gridWidth = itemGrid?.clientWidth || Math.max(window.innerWidth - 320, 640);
    const gapWidth = (columns - 1) * 20;
    return (gridWidth - gapWidth) / columns;
  }

  function getDefaultDesktopGridColumns() {
    return desktopGridLevels.reduce((closest, candidate) => {
      const currentDistance = Math.abs(estimateDesktopCardWidth(candidate) - 200);
      const bestDistance = Math.abs(estimateDesktopCardWidth(closest) - 200);
      return currentDistance < bestDistance ? candidate : closest;
    }, desktopGridLevels[0]);
  }

  function updateModeToggleIcon() {
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
    const brandIcon = document.querySelector(".nav-brand-icon");
    if (brandIcon) {
      brandIcon.src = getThemeIconPath();
    }

    window.SoulsPageTransition?.setThemeIcon?.(body.classList.contains("light-mode"));
    window.syncThemeAwareColorPicker?.();
    syncColorPickerPresentation();
  }

  function isDesktopViewport() {
    return window.matchMedia("(min-width: 1200px)").matches;
  }

  function isValidHexColor(value) {
    return /^#[0-9a-f]{6}$/i.test(value || "");
  }

  function syncColorPickerPresentation() {
    if (!colorPickerGroup || !colorPicker) {
      return;
    }

    const fallbackValue = body.classList.contains("light-mode") ? "#000000" : "#ffffff";
    const currentValue = isValidHexColor(colorPicker.value) ? colorPicker.value : fallbackValue;
    colorPickerGroup.style.setProperty("--picker-preview", currentValue);

    if (colorPickerHexInput && document.activeElement !== colorPickerHexInput) {
      colorPickerHexInput.value = currentValue.toUpperCase();
    }
  }

  function closeColorPickerPopover() {
    if (!colorPickerGroup || !colorPickerPopover) {
      return;
    }

    colorPickerGroup.classList.remove("is-open");
  }

  function toggleColorPickerPopover(forceOpen = null) {
    if (!colorPickerGroup || !colorPickerPopover || !isDesktopViewport()) {
      return;
    }

    const shouldOpen =
      typeof forceOpen === "boolean"
        ? forceOpen
        : !colorPickerGroup.classList.contains("is-open");

    colorPickerGroup.classList.toggle("is-open", shouldOpen);
    syncColorPickerPresentation();

    if (shouldOpen && colorPickerHexInput) {
      colorPickerHexInput.focus();
      colorPickerHexInput.select();
    }
  }

  function applyColorPickerValue(nextValue, closeAfter = false) {
    if (!colorPicker || !isValidHexColor(nextValue)) {
      return false;
    }

    const normalizedValue = nextValue.toLowerCase();
    colorPicker.value = normalizedValue;
    colorPicker.dispatchEvent(new Event("input", { bubbles: true }));
    colorPicker.dispatchEvent(new Event("change", { bubbles: true }));
    syncColorPickerPresentation();

    if (closeAfter) {
      closeColorPickerPopover();
    }

    return true;
  }

  function initializeModernColorPicker() {
    if (!colorPickerGroup || !colorPicker || colorPickerGroup.dataset.enhanced === "true") {
      return;
    }

    colorPickerGroup.dataset.enhanced = "true";
    colorPickerGroup.style.setProperty("--picker-preview", colorPicker.value || "#ffffff");

    colorPickerTrigger = document.createElement("button");
    colorPickerTrigger.type = "button";
    colorPickerTrigger.className = "color-picker-trigger";
    colorPickerTrigger.setAttribute("aria-label", "Open hex colour controls");

    colorPickerPopover = document.createElement("div");
    colorPickerPopover.className = "color-picker-popover";
    colorPickerPopover.innerHTML = `
      <div class="color-picker-swatch-grid">
        ${desktopColorPresets
          .map(
            (color) =>
              `<button type="button" class="color-picker-swatch" data-color="${color}" style="--swatch-color: ${color};"></button>`
          )
          .join("")}
      </div>
      <div class="color-picker-hex-row">
        <input type="text" class="color-picker-hex-input" maxlength="7" spellcheck="false" aria-label="Hex colour value">
        <button type="button" class="color-picker-native-button">More</button>
      </div>
    `;

    colorPickerGroup.appendChild(colorPickerTrigger);
    colorPickerGroup.appendChild(colorPickerPopover);
    colorPickerHexInput = colorPickerPopover.querySelector(".color-picker-hex-input");

    colorPickerTrigger.addEventListener("click", (event) => {
      event.preventDefault();
      event.stopPropagation();
      toggleColorPickerPopover();
    });

    colorPickerPopover.querySelectorAll(".color-picker-swatch").forEach((button) => {
      button.addEventListener("click", (event) => {
        event.preventDefault();
        applyColorPickerValue(button.dataset.color, true);
      });
    });

    colorPickerPopover
      .querySelector(".color-picker-native-button")
      .addEventListener("click", (event) => {
        event.preventDefault();
        colorPicker.click();
      });

    colorPickerHexInput.addEventListener("keydown", (event) => {
      if (event.key === "Enter") {
        event.preventDefault();
        applyColorPickerValue(colorPickerHexInput.value, true);
      }

      if (event.key === "Escape") {
        closeColorPickerPopover();
      }
    });

    colorPickerHexInput.addEventListener("change", () => {
      applyColorPickerValue(colorPickerHexInput.value, false);
    });

    colorPicker.addEventListener("input", syncColorPickerPresentation);
    colorPicker.addEventListener("change", syncColorPickerPresentation);

    document.addEventListener("pointerdown", (event) => {
      if (!colorPickerGroup.contains(event.target)) {
        closeColorPickerPopover();
      }
    });

    window.addEventListener(
      "resize",
      () => {
        if (!isDesktopViewport()) {
          closeColorPickerPopover();
        }
        syncColorPickerPresentation();
      },
      { passive: true }
    );

    window.syncGamePageColorPickerUI = syncColorPickerPresentation;
    syncColorPickerPresentation();
  }

  function setColorPickerVisible(visible) {
    const shouldShow = Boolean(visible);
    if (colorPickerGroup) {
      colorPickerGroup.classList.toggle("is-visible", shouldShow);
    }

    if (colorPicker) {
      colorPicker.disabled = !shouldShow;
    }

    if (!shouldShow) {
      closeColorPickerPopover();
    }
  }

  function setSliderLabelValue(controlId, valueText) {
    const label = document.querySelector(`label[for="${controlId}"]`);
    if (!label) {
      return;
    }

    const baseLabel = label.dataset.baseLabel || label.textContent.split(":")[0].trim();
    label.dataset.baseLabel = baseLabel;
    label.textContent = `${baseLabel}: ${valueText}`;
  }

  function setSiteMenuOpen(open) {
    const shouldOpen = Boolean(open);
    body.classList.toggle("site-menu-open", shouldOpen);

    if (toggleButton) {
      toggleButton.setAttribute("aria-expanded", shouldOpen ? "true" : "false");
    }

    if (siteMenuOverlay) {
      siteMenuOverlay.setAttribute("aria-hidden", shouldOpen ? "false" : "true");
    }
  }

  function buildSiteMenu() {
    if (!topnav || !toggleButton || !brandLink) {
      return;
    }

    sidebar?.classList.add("legacy-nav-links");
    toggleButton.classList.add("menu-toggle-button");
    toggleButton.setAttribute("type", "button");
    toggleButton.setAttribute("aria-label", "Toggle navigation menu");
    toggleButton.setAttribute("aria-expanded", "false");
    toggleButton.innerHTML =
      '<span class="menu-toggle-bar top"></span><span class="menu-toggle-bar middle"></span><span class="menu-toggle-bar bottom"></span>';

    if (modeToggle.parentElement !== topnav) {
      topnav.appendChild(modeToggle);
    }

    brandLink.classList.add("nav-brand-link");
    brandLink.setAttribute("aria-label", "Fashion Souls home");
    brandLink.innerHTML =
      `<img src="${getThemeIconPath()}" alt="Fashion Souls" class="nav-brand-icon" />`;

    let navSiteCopy = topnav.querySelector(".nav-site-copy");
    if (!navSiteCopy) {
      navSiteCopy = document.createElement("div");
      navSiteCopy.className = "content-site-copy nav-site-copy";
      navSiteCopy.innerHTML =
        '<h3 class="content-site-title">Fashion Souls</h3><p class="site-tagline">SoulsBorne Fashion Tool by psyopgirl</p>';
      topnav.appendChild(navSiteCopy);
    }

    if (siteMenuOverlay) {
      return;
    }

    siteMenuOverlay = document.createElement("aside");
    siteMenuOverlay.className = "site-menu-overlay";
    siteMenuOverlay.id = "siteMenuOverlay";
    siteMenuOverlay.setAttribute("aria-hidden", "true");

    const linksMarkup = siteMenuLinks
      .map((link) => {
        const target = link.href === currentPage || link.href === `${currentPage}.html` ? ' aria-current="page"' : "";
        return `<li><a href="${link.href}" class="site-menu-link"${target}>${link.label}</a></li>`;
      })
      .join("");

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

    toggleButton.addEventListener("click", () => {
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

    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape") {
        setSiteMenuOpen(false);
      }
    });
  }

  function applyDesktopGridColumns(value, persist = true) {
    const numericValue = Number(value);
    const clampedValue = desktopGridLevels.includes(numericValue)
      ? numericValue
      : getDefaultDesktopGridColumns();

    currentDesktopGridColumns = clampedValue;
    document.documentElement.style.setProperty("--desktop-grid-columns", clampedValue.toString());

    const gridZoomSlider = document.getElementById("gridZoomSlider");
    if (gridZoomSlider) {
      gridZoomSlider.value = clampedValue.toString();
    }
    setSliderLabelValue("gridZoomSlider", clampedValue.toString());

    if (persist) {
      localStorage.setItem(`${window.gamePrefix}desktopGridColumns`, clampedValue.toString());
    }
  }

  function applyMobileGridColumns(value, persist = true) {
    const numericValue = Number(value);
    const clampedValue = Math.min(
      MOBILE_GRID_MAX,
      Math.max(
        MOBILE_GRID_MIN,
        Number.isFinite(numericValue) ? Math.round(numericValue) : MOBILE_GRID_MIN
      )
    );

    currentMobileGridColumns = clampedValue;
    document.documentElement.style.setProperty("--mobile-grid-columns", clampedValue.toString());

    if (persist) {
      localStorage.setItem(`${window.gamePrefix}tileColumns`, clampedValue.toString());
    }
  }

  function initGridZoomControl() {
    const gridZoomSlider = document.getElementById("gridZoomSlider");
    if (!gridZoomSlider) {
      return;
    }

    const gridZoomLabel = document.querySelector('label[for="gridZoomSlider"]');
    if (gridZoomLabel) {
      gridZoomLabel.dataset.baseLabel = "Cards Per Row";
    }

    gridZoomSlider.min = desktopGridLevels[0].toString();
    gridZoomSlider.max = desktopGridLevels[desktopGridLevels.length - 1].toString();
    gridZoomSlider.step = "1";

    const sliderContainer = gridZoomSlider.closest(".slider-container");
    const syncSliderVisibility = () => {
      if (!sliderContainer) return;
      sliderContainer.style.display = isMobileViewport() ? "none" : "";
    };

    const savedDesktopColumns = Number(localStorage.getItem(`${window.gamePrefix}desktopGridColumns`));
    const initialDesktopColumns = desktopGridLevels.includes(savedDesktopColumns)
      ? savedDesktopColumns
      : getDefaultDesktopGridColumns();
    applyDesktopGridColumns(initialDesktopColumns, false);

    const savedColumns = Number(localStorage.getItem(`${window.gamePrefix}tileColumns`));
    const initialColumns = isMobileViewport()
      ? MOBILE_GRID_MIN
      : Number.isFinite(savedColumns)
        ? Math.min(MOBILE_GRID_MAX, Math.max(MOBILE_GRID_MIN, savedColumns))
        : MOBILE_GRID_MIN;
    applyMobileGridColumns(initialColumns, false);
    syncSliderVisibility();

    gridZoomSlider.addEventListener("input", (event) => {
      if (isMobileViewport()) {
        return;
      }

      applyDesktopGridColumns(event.target.value);
    });

    window.addEventListener(
      "resize",
      () => {
        syncSliderVisibility();
        if (!isMobileViewport()) {
          applyDesktopGridColumns(currentDesktopGridColumns, false);
        }
      },
      { passive: true }
    );
  }

  function setupPinchZoom() {
    if (document.body.dataset.mobilePinchBound === "true") {
      return;
    }

    document.body.dataset.mobilePinchBound = "true";

    let pinchActive = false;
    let pinchLastDistance = 0;

    const getDistance = (touchA, touchB) => {
      const dx = touchA.clientX - touchB.clientX;
      const dy = touchA.clientY - touchB.clientY;
      return Math.hypot(dx, dy);
    };

    const getPinchStepSize = () => {
      const itemGridElement = document.getElementById("itemGrid");
      const gridWidth = itemGridElement?.clientWidth || window.innerWidth || 320;
      return Math.max(16, Math.min(34, gridWidth * 0.045));
    };

    const isTouchInsideGrid = (touch) => {
      const itemGridElement = document.getElementById("itemGrid");
      if (!itemGridElement || !touch) {
        return false;
      }

      const rect = itemGridElement.getBoundingClientRect();
      return (
        touch.clientX >= rect.left &&
        touch.clientX <= rect.right &&
        touch.clientY >= rect.top &&
        touch.clientY <= rect.bottom
      );
    };

    const canStartPinch = (event) =>
      isMobileViewport() &&
      event.touches.length === 2 &&
      isTouchInsideGrid(event.touches[0]) &&
      isTouchInsideGrid(event.touches[1]);

    const onTouchStart = (event) => {
      if (!canStartPinch(event)) {
        return;
      }

      pinchActive = true;
      pinchLastDistance = getDistance(event.touches[0], event.touches[1]);
      event.preventDefault();
    };

    const onTouchMove = (event) => {
      if (!pinchActive && canStartPinch(event)) {
        pinchActive = true;
        pinchLastDistance = getDistance(event.touches[0], event.touches[1]);
      }

      if (!pinchActive || !isMobileViewport() || event.touches.length !== 2) {
        return;
      }

      const currentDistance = getDistance(event.touches[0], event.touches[1]);
      const pinchStepSize = getPinchStepSize();
      let delta = currentDistance - pinchLastDistance;
      let updatedColumns = false;

      while (Math.abs(delta) >= pinchStepSize) {
        const nextColumns =
          delta > 0 ? currentMobileGridColumns - 1 : currentMobileGridColumns + 1;

        if (nextColumns === currentMobileGridColumns) {
          pinchLastDistance = currentDistance;
          break;
        }

        applyMobileGridColumns(nextColumns);
        pinchLastDistance += delta > 0 ? pinchStepSize : -pinchStepSize;
        delta = currentDistance - pinchLastDistance;
        updatedColumns = true;
      }

      if (updatedColumns || pinchActive) {
        event.preventDefault();
      }
    };

    const onTouchEnd = (event) => {
      if (event.touches.length < 2) {
        pinchActive = false;
        pinchLastDistance = 0;
      }
    };

    document.addEventListener("touchstart", onTouchStart, {
      passive: false,
      capture: true,
    });
    document.addEventListener("touchmove", onTouchMove, {
      passive: false,
      capture: true,
    });
    document.addEventListener("touchend", onTouchEnd, {
      passive: true,
      capture: true,
    });
    document.addEventListener("touchcancel", onTouchEnd, {
      passive: true,
      capture: true,
    });
  }

  function preventMobileViewportZoom() {
    let lastTouchEnd = 0;

    const preventGesture = (event) => {
      if (!isMobileViewport()) {
        return;
      }

      event.preventDefault();
    };

    document.addEventListener("gesturestart", preventGesture, { passive: false });
    document.addEventListener("gesturechange", preventGesture, { passive: false });
    document.addEventListener("gestureend", preventGesture, { passive: false });

    document.addEventListener(
      "touchend",
      (event) => {
        if (!isMobileViewport()) {
          return;
        }

        const interactiveTarget = event.target.closest(
          'input, textarea, select, [contenteditable="true"]'
        );
        if (interactiveTarget) {
          lastTouchEnd = Date.now();
          return;
        }

        const now = Date.now();
        if (now - lastTouchEnd <= 300) {
          event.preventDefault();
        }
        lastTouchEnd = now;
      },
      { passive: false }
    );
  }

  function updateScrollUI() {
    const scrollY = getScrollTop();
    const backToTopButton = document.querySelector(".back-to-top-button");
    const footer = document.querySelector(".footer");

    if (scrollY > 400) {
      backToTopButton.style.opacity = "1";
      backToTopButton.style.display = "block";
      footer.style.opacity = "1";
    } else {
      backToTopButton.style.opacity = "0";
      backToTopButton.style.display = "none";
      footer.style.opacity = "0";
    }

    if (isMobileViewport()) {
      const controlsHeight = nav.offsetHeight || 0;
      const atTop = scrollY <= 4;
      const controlsVisible = atTop || scrollY <= controlsHeight + 24;
      body.classList.toggle("mobile-controls-visible", controlsVisible);
      document.documentElement.style.setProperty("--mobile-controls-offset", `${controlsHeight}px`);
      const shouldShowSidebar = !controlsVisible && scrollY > controlsHeight + 24;
      setMobileSidebarVisible(shouldShowSidebar);
    } else {
      body.classList.remove("mobile-sidebar-visible");
      body.classList.remove("mobile-controls-visible");
      sidebarActive = false;
      navActive = true;
      showNav();
    }
  }

  function onScroll() {
    if (scrollRafId !== null) {
      return;
    }

    scrollRafId = requestAnimationFrame(() => {
      updateScrollUI();
      scrollRafId = null;
    });
  }

  function updateSearchFromItem(item) {
    searchInput.value = item.name;
    setColorPickerVisible(false);
    toggleSearch.textContent = "Item";
    searchInput.placeholder = "Search by item";
    searchInput.readOnly = false;
    searchInput.setAttribute("aria-readonly", "false");

    hideOutfitSidebar();
    showNav();
    scrollPageToTop();
    updateMatchingItems();
  }

  function findItemByName(itemName) {
    if (!itemName) {
      return null;
    }

    return items.find((entry) => entry.name === itemName) || null;
  }

  function resolveEquipSlotType(item) {
    if (!item?.type) {
      return "";
    }

    let slotType = `${item.type}Slot`;
    if (item.type === "weapons" || item.type === "shields") {
      const outfitSlots =
        JSON.parse(localStorage.getItem(`${window.gamePrefix}outfitSlots`)) || {};
      const alternateSlot = slotType === "weaponsSlot" ? "shieldsSlot" : "weaponsSlot";
      slotType = outfitSlots[slotType] ? alternateSlot : slotType;
    }

    return slotType;
  }

  function equipItemToOutfit(item, options = {}) {
    const { revealSidebar = true } = options;
    if (!item) {
      return;
    }

    const slotType = resolveEquipSlotType(item);
    if (!slotType) {
      return;
    }

    addItemToSlot(slotType, item);

    if (revealSidebar) {
      showOutfitSidebar();
      hideNav();
    }
  }

  function equipItemByName(itemName, options = {}) {
    const item = findItemByName(itemName);
    if (!item) {
      console.error("Item not found in loaded item data:", itemName);
      return;
    }

    equipItemToOutfit(item, options);
  }

  function ensureMobileActionSheet() {
    if (mobileActionSheet) {
      return mobileActionSheet;
    }

    mobileActionSheetBackdrop = document.createElement("button");
    mobileActionSheetBackdrop.type = "button";
    mobileActionSheetBackdrop.className = "mobile-action-sheet-backdrop";
    mobileActionSheetBackdrop.setAttribute("aria-label", "Close action menu");

    mobileActionSheet = document.createElement("div");
    mobileActionSheet.className = "mobile-action-sheet";
    mobileActionSheet.setAttribute("role", "dialog");
    mobileActionSheet.setAttribute("aria-modal", "true");
    mobileActionSheet.setAttribute("aria-hidden", "true");
    mobileActionSheet.innerHTML = `
      <div class="mobile-action-sheet-header">
        <div class="mobile-action-sheet-copy">
          <p class="mobile-action-sheet-title"></p>
          <p class="mobile-action-sheet-subtitle"></p>
        </div>
        <button type="button" class="mobile-action-sheet-close" aria-label="Close action menu">Close</button>
      </div>
      <div class="mobile-action-sheet-actions"></div>
    `;

    document.body.appendChild(mobileActionSheetBackdrop);
    document.body.appendChild(mobileActionSheet);

    mobileActionSheetTitle = mobileActionSheet.querySelector(".mobile-action-sheet-title");
    mobileActionSheetSubtitle = mobileActionSheet.querySelector(".mobile-action-sheet-subtitle");
    mobileActionSheetActions = mobileActionSheet.querySelector(".mobile-action-sheet-actions");

    const closeButton = mobileActionSheet.querySelector(".mobile-action-sheet-close");
    closeButton?.addEventListener("click", closeMobileActionSheet);
    mobileActionSheetBackdrop.addEventListener("click", closeMobileActionSheet);

    return mobileActionSheet;
  }

  function closeMobileActionSheet() {
    if (!mobileActionSheet) {
      return;
    }

    mobileActionSheet.classList.remove("is-open");
    mobileActionSheet.setAttribute("aria-hidden", "true");
    document.body.classList.remove("mobile-action-sheet-open");
  }

  function openMobileActionSheet(config) {
    if (!isMobileViewport()) {
      return;
    }

    ensureMobileActionSheet();

    const { title = "", subtitle = "", actions = [] } = config || {};
    mobileActionSheetTitle.textContent = title;
    mobileActionSheetSubtitle.textContent = subtitle;
    mobileActionSheetSubtitle.hidden = !subtitle;
    mobileActionSheetActions.innerHTML = "";

    actions.forEach((action) => {
      const actionButton = document.createElement("button");
      actionButton.type = "button";
      actionButton.className = "mobile-action-sheet-button";

      if (action.tone) {
        actionButton.dataset.tone = action.tone;
      }

      actionButton.textContent = action.label;
      actionButton.addEventListener("click", () => {
        closeMobileActionSheet();
        action.onSelect?.();
      });
      mobileActionSheetActions.appendChild(actionButton);
    });

    const cancelButton = document.createElement("button");
    cancelButton.type = "button";
    cancelButton.className = "mobile-action-sheet-button";
    cancelButton.dataset.tone = "secondary";
    cancelButton.textContent = "Cancel";
    cancelButton.addEventListener("click", closeMobileActionSheet);
    mobileActionSheetActions.appendChild(cancelButton);

    mobileActionSheet.classList.add("is-open");
    mobileActionSheet.setAttribute("aria-hidden", "false");
    document.body.classList.add("mobile-action-sheet-open");
  }

  function openMobileItemActionSheet(item) {
    if (!item) {
      return;
    }

    openMobileActionSheet({
      title: item.name,
      subtitle: "Choose what to do with this item.",
      actions: [
        {
          label: "Search Using Item",
          onSelect: () => updateSearchFromItem(item),
        },
        {
          label: "Equip in Outfit",
          onSelect: () => equipItemToOutfit(item),
        },
      ],
    });
  }

  function openMobileSlotActionSheet(slotId, item) {
    if (!slotId || !item) {
      return;
    }

    openMobileActionSheet({
      title: item.name,
      subtitle: "Choose what to do with this equipped item.",
      actions: [
        {
          label: "Search Using Item",
          onSelect: () => updateSearchFromItem(item),
        },
        {
          label: "Unequip Item",
          tone: "danger",
          onSelect: () => removeItemFromSlot(slotId),
        },
      ],
    });
  }

  function removeItemFromSlot(slotId) {
    const outfit = JSON.parse(localStorage.getItem(`${window.gamePrefix}outfitSlots`)) || {};
    if (!outfit[slotId]) {
      return;
    }

    delete outfit[slotId];
    localStorage.setItem(`${window.gamePrefix}outfitSlots`, JSON.stringify(outfit));
    loadOutfitFromStorage();
  }

  function getSlotTypeFromId(slotId) {
    return (slotId || "").replace(/Slot$/, "");
  }

  function getSlotLabel(slotId) {
    const slotType = getSlotTypeFromId(slotId);
    return slotLabels[slotType] || slotType;
  }

  function getItemsForSlot(slotId) {
    const slotType = getSlotTypeFromId(slotId);
    return Array.isArray(items) ? items.filter((item) => item.type === slotType) : [];
  }

  function getContextSecondaryColors(item) {
    if (Array.isArray(item?.secondaryColors) && item.secondaryColors.length > 0) {
      return item.secondaryColors;
    }

    return item?.primaryColor ? [item.primaryColor, item.primaryColor] : [];
  }

  function getContextColorMatches(slotId, item) {
    if (
      !item?.primaryColor ||
      typeof hexToLAB !== "function" ||
      typeof calculateWeightedDistance !== "function"
    ) {
      return [];
    }

    const inputLab = hexToLAB(item.primaryColor);
    return getItemsForSlot(slotId)
      .filter((candidate) => candidate.name !== item.name && candidate.primaryColor)
      .map((candidate) => ({
        ...candidate,
        distance: calculateWeightedDistance(
          inputLab,
          candidate.primaryColor,
          getContextSecondaryColors(candidate),
          desktopContextColorMatchWeight
        ),
      }))
      .sort((left, right) => left.distance - right.distance)
      .slice(0, 8);
  }

  function createDesktopContextOption(item, onClick) {
    const option = document.createElement("button");
    option.type = "button";
    option.className = "simulator-replacement-option";

    const image = document.createElement("img");
    image.src = `pages/${currentPage}/icons/${item.image}`;
    image.alt = item.name;

    const title = document.createElement("div");
    title.className = "simulator-replacement-option-title";
    title.textContent = item.name;

    option.appendChild(image);
    option.appendChild(title);
    option.addEventListener("click", () => {
      onClick(item);
    });

    return option;
  }

  function ensureDesktopSlotContextMenu() {
    if (desktopSlotContextMenu) {
      return desktopSlotContextMenu;
    }

    desktopSlotContextMenu = document.createElement("div");
    desktopSlotContextMenu.id = "desktopSlotContextMenu";
    desktopSlotContextMenu.className = "simulator-context-menu";
    desktopSlotContextMenu.setAttribute("aria-hidden", "true");
    desktopSlotContextMenu.innerHTML = `
      <div class="simulator-context-header">
        <div>
          <p class="simulator-context-title"></p>
          <p class="simulator-context-subtitle"></p>
        </div>
        <button type="button" class="simulator-context-close" aria-label="Close">x</button>
      </div>
      <div class="simulator-context-actions">
        <button type="button" class="simulator-context-action" data-mode="replace">Replace Item</button>
        <button type="button" class="simulator-context-action" data-mode="colour">Replace By Colour</button>
        <button type="button" class="simulator-context-action" data-mode="unequip">Unequip Item</button>
      </div>
      <div class="simulator-context-body"></div>
    `;

    document.body.appendChild(desktopSlotContextMenu);
    desktopSlotContextBody = desktopSlotContextMenu.querySelector(".simulator-context-body");
    desktopSlotContextTitle = desktopSlotContextMenu.querySelector(".simulator-context-title");
    desktopSlotContextSubtitle = desktopSlotContextMenu.querySelector(".simulator-context-subtitle");
    desktopSlotContextActions = desktopSlotContextMenu.querySelector(".simulator-context-actions");

    desktopSlotContextMenu
      .querySelector(".simulator-context-close")
      .addEventListener("click", closeDesktopSlotContextMenu);

    desktopSlotContextMenu.querySelectorAll(".simulator-context-action").forEach((button) => {
      button.addEventListener("click", () => {
        const mode = button.dataset.mode;
        if (mode === "unequip") {
          removeItemFromSlot(activeDesktopSlotId);
          closeDesktopSlotContextMenu();
          return;
        }

        activeDesktopSlotMode = mode;
        renderDesktopSlotContextBody();
      });
    });

    return desktopSlotContextMenu;
  }

  function setDesktopSlotContextMetadata(slotId, item) {
    activeDesktopSlotId = slotId;
    activeDesktopSlotItem = item || null;
    activeDesktopSlotSearch = "";

    if (desktopSlotContextTitle) {
      desktopSlotContextTitle.textContent = item?.name || "Select Item";
    }

    if (desktopSlotContextSubtitle) {
      desktopSlotContextSubtitle.textContent = getSlotLabel(slotId);
    }
  }

  function positionDesktopSlotContextMenu(clientX, clientY) {
    if (!desktopSlotContextMenu) {
      return;
    }

    desktopSlotContextMenu.classList.add("is-open");
    desktopSlotContextMenu.style.visibility = "hidden";
    desktopSlotContextMenu.style.left = "0px";
    desktopSlotContextMenu.style.top = "0px";

    const maxLeft = Math.max(8, window.innerWidth - desktopSlotContextMenu.offsetWidth - 8);
    const maxTop = Math.max(8, window.innerHeight - desktopSlotContextMenu.offsetHeight - 8);
    const left = Math.min(Math.max(8, clientX), maxLeft);
    const top = Math.min(Math.max(8, clientY), maxTop);

    desktopSlotContextMenu.style.left = `${left}px`;
    desktopSlotContextMenu.style.top = `${top}px`;
    desktopSlotContextMenu.style.visibility = "visible";
    desktopSlotContextMenu.setAttribute("aria-hidden", "false");
  }

  function closeDesktopSlotContextMenu() {
    if (!desktopSlotContextMenu) {
      return;
    }

    desktopSlotContextMenu.classList.remove("is-open");
    desktopSlotContextMenu.style.visibility = "";
    desktopSlotContextMenu.setAttribute("aria-hidden", "true");
  }

  function replaceDesktopSlotItem(slotId, item) {
    addItemToSlot(slotId, item);
  }

  function renderDesktopSlotReplaceBody() {
    const slotLabel = getSlotLabel(activeDesktopSlotId).toLowerCase();
    const matchingItems = getItemsForSlot(activeDesktopSlotId)
      .filter((item) => !activeDesktopSlotItem || item.name !== activeDesktopSlotItem.name)
      .filter((item) =>
        item.name.toLowerCase().includes(activeDesktopSlotSearch.trim().toLowerCase())
      )
      .slice(0, 14);

    const searchField = document.createElement("input");
    searchField.type = "search";
    searchField.className = "simulator-context-search";
    searchField.placeholder = activeDesktopSlotItem
      ? `Replace ${slotLabel}...`
      : `Select ${slotLabel}...`;
    searchField.value = activeDesktopSlotSearch;
    searchField.addEventListener("input", () => {
      activeDesktopSlotSearch = searchField.value;
      renderDesktopSlotContextBody();
    });
    desktopSlotContextBody.appendChild(searchField);

    if (matchingItems.length === 0) {
      const emptyState = document.createElement("p");
      emptyState.className = "simulator-context-empty";
      emptyState.textContent = "No matching items were found for that search.";
      desktopSlotContextBody.appendChild(emptyState);
      searchField.focus();
      return;
    }

    const list = document.createElement("div");
    list.className = "simulator-replacement-list";

    matchingItems.forEach((item) => {
      list.appendChild(
        createDesktopContextOption(item, (selectedItem) => {
          replaceDesktopSlotItem(activeDesktopSlotId, selectedItem);
          closeDesktopSlotContextMenu();
        })
      );
    });

    desktopSlotContextBody.appendChild(list);
    searchField.focus();
  }

  function renderDesktopSlotColourBody() {
    const matches = getContextColorMatches(activeDesktopSlotId, activeDesktopSlotItem);

    if (matches.length === 0) {
      const emptyState = document.createElement("p");
      emptyState.className = "simulator-context-empty";
      emptyState.textContent = "No similarly coloured replacements were available for this slot.";
      desktopSlotContextBody.appendChild(emptyState);
      return;
    }

    const grid = document.createElement("div");
    grid.className = "simulator-replacement-grid";

    matches.forEach((item) => {
      grid.appendChild(
        createDesktopContextOption(item, (selectedItem) => {
          replaceDesktopSlotItem(activeDesktopSlotId, selectedItem);
          closeDesktopSlotContextMenu();
        })
      );
    });

    desktopSlotContextBody.appendChild(grid);
  }

  function renderDesktopSlotContextBody() {
    if (!desktopSlotContextBody || !desktopSlotContextMenu) {
      return;
    }

    const hasActiveItem = Boolean(activeDesktopSlotItem);
    desktopSlotContextBody.innerHTML = "";

    if (desktopSlotContextActions) {
      desktopSlotContextActions.hidden = !hasActiveItem;
    }

    desktopSlotContextMenu.querySelectorAll(".simulator-context-action").forEach((button) => {
      button.classList.toggle("is-active", button.dataset.mode === activeDesktopSlotMode);
    });

    if (!hasActiveItem || activeDesktopSlotMode === "select") {
      renderDesktopSlotReplaceBody();
      return;
    }

    if (activeDesktopSlotMode === "colour") {
      renderDesktopSlotColourBody();
      return;
    }

    renderDesktopSlotReplaceBody();
  }

  function openDesktopSlotContextMenu(clientX, clientY, slotId, item) {
    ensureDesktopSlotContextMenu();
    activeDesktopSlotMode = item ? "replace" : "select";
    setDesktopSlotContextMetadata(slotId, item);
    renderDesktopSlotContextBody();
    positionDesktopSlotContextMenu(clientX, clientY);
  }

  function loadOutfitFromStorage() {
    const types = ["head", "chest", "hands", "legs", "weapons", "shields"];
    const outfitSlots = JSON.parse(localStorage.getItem(`${window.gamePrefix}outfitSlots`)) || {};
    const outfitContainer = document.getElementById("outfitSlots");
    outfitContainer.innerHTML = "";

    types.forEach((type) => {
      const slotId = `${type}Slot`;
      const item = outfitSlots[slotId];
      const slot = document.createElement("div");
      slot.classList.add("slot");
      slot.dataset.slotId = slotId;

      if (item) {
        slot.classList.add("equipped-slot");
        slot.dataset.itemName = item.name;
        slot.setAttribute("role", "button");
        slot.setAttribute("tabindex", "0");

        const img = document.createElement("img");
        img.src = `pages/${currentPage}/icons/${item.image}`;
        img.alt = item.name;
        img.draggable = false;

        const hoverLabel = document.createElement("div");
        hoverLabel.classList.add("slot-hover-name");
        hoverLabel.textContent = item.name;

        slot.addEventListener("click", (event) => {
          event.preventDefault();
          const fullItem = findItemByName(item.name);
          if (fullItem) {
            if (isMobileViewport()) {
              openMobileSlotActionSheet(slotId, fullItem);
              return;
            }

            updateSearchFromItem(fullItem);
          }
        });

        slot.addEventListener("keydown", (event) => {
          if (event.key !== "Enter" && event.key !== " ") {
            return;
          }

          event.preventDefault();
          const fullItem = findItemByName(item.name);
          if (!fullItem) {
            return;
          }

          if (isMobileViewport()) {
            openMobileSlotActionSheet(slotId, fullItem);
            return;
          }

          updateSearchFromItem(fullItem);
        });

        slot.appendChild(img);
        slot.appendChild(hoverLabel);
      } else {
        const placeholder = document.createElement("div");
        placeholder.classList.add("placeholder-tile");
        const placeholderText = document.createElement("p");

        switch (type) {
          case "head":
            placeholderText.textContent = "No helm equipped.";
            break;
          case "chest":
            placeholderText.textContent = "No chest armor equipped.";
            break;
          case "hands":
            placeholderText.textContent = "No gauntlets equipped.";
            break;
          case "legs":
            placeholderText.textContent = "No leg armor equipped.";
            break;
          case "weapons":
            placeholderText.textContent = "No main-hand item equipped.";
            break;
          case "shields":
            placeholderText.textContent = "No off-hand item equipped.";
            break;
          default:
            placeholderText.textContent = `No ${type} selected`;
        }

        placeholder.appendChild(placeholderText);
        slot.appendChild(placeholder);
      }

      slot.addEventListener("contextmenu", (event) => {
        event.preventDefault();
        showContextMenu(event, "remove", slotId);
      });

      outfitContainer.appendChild(slot);
    });

    if (!document.body.dataset.contextMenuDismissBound) {
      document.body.dataset.contextMenuDismissBound = "true";
      document.addEventListener("click", () => {
        const contextMenu = document.getElementById("contextMenu");
        if (contextMenu.style.display === "flex") {
          contextMenu.style.display = "none";
        }
      });

      document.addEventListener("pointerdown", (event) => {
        if (!desktopSlotContextMenu?.classList.contains("is-open")) {
          return;
        }

        if (
          desktopSlotContextMenu.contains(event.target) ||
          event.target.closest("#outfitSlots .slot")
        ) {
          return;
        }

        closeDesktopSlotContextMenu();
      });
    }

    initializeDragAndDrop();
  }

  function showContextMenu(event, action, identifier) {
    if (isMobileViewport()) {
      if (action === "send") {
        openMobileItemActionSheet(identifier);
        return;
      }

      if (action === "remove") {
        const slotElement = document.querySelector(`#outfitSlots .slot[data-slot-id="${identifier}"]`);
        const item = findItemByName(slotElement?.dataset.itemName || "");
        if (item) {
          openMobileSlotActionSheet(identifier, item);
          return;
        }

        return;
      }
    }

    if (action === "remove") {
      const slotElement = document.querySelector(`#outfitSlots .slot[data-slot-id="${identifier}"]`);
      const item = findItemByName(slotElement?.dataset.itemName || "");
      const legacyMenu = document.getElementById("contextMenu");
      if (legacyMenu) {
        legacyMenu.style.display = "none";
      }
      openDesktopSlotContextMenu(event.clientX, event.clientY, identifier, item);
      return;
    }

    const contextMenu = document.getElementById("contextMenu");
    const contextMenuList = document.getElementById("contextMenuList");
    contextMenuList.innerHTML = "";
    closeDesktopSlotContextMenu();

    const menuOption = document.createElement("li");
    if (action === "remove") {
      rightClickedSlotId = identifier;
      menuOption.textContent = "Remove Item";
      menuOption.addEventListener("click", removeItemFromOutfit);
    } else if (action === "send") {
      rightClickedItem = identifier;
      menuOption.textContent = "Send to Outfit Simulator";
      menuOption.addEventListener("click", sendItemToOutfitSimulator);
    }

    contextMenuList.appendChild(menuOption);
    contextMenu.style.top = `${event.pageY}px`;
    contextMenu.style.left = `${event.pageX}px`;
    contextMenu.style.display = "flex";
  }

  function removeItemFromOutfit() {
    if (rightClickedSlotId) {
      const outfit = JSON.parse(localStorage.getItem(`${window.gamePrefix}outfitSlots`)) || {};
      delete outfit[rightClickedSlotId];
      localStorage.setItem(`${window.gamePrefix}outfitSlots`, JSON.stringify(outfit));
      loadOutfitFromStorage();
    }

    document.getElementById("contextMenu").style.display = "none";
  }

  function sendItemToOutfitSimulator() {
    if (rightClickedItem) {
      equipItemToOutfit(rightClickedItem);
    }

    document.getElementById("contextMenu").style.display = "none";
    showOutfitSidebar();
    hideNav();
  }

  function initializeItemGrid() {
    const itemGridElement = document.getElementById("itemGrid");

    itemGridElement.querySelectorAll(".item-card").forEach((card) => {
      card.addEventListener("contextmenu", (event) => {
        event.preventDefault();
        const itemInfo = card.querySelector(".item-info");
        const titleContainer = itemInfo.querySelector(".title-container");
        const title = titleContainer.querySelector("a").textContent;
        const item = items.find((entry) => entry.name === title);
        if (item) {
          showContextMenu(event, "send", item);
        }
      });
    });
  }

  function initializeDragAndDrop() {
    const itemGridElement = document.getElementById("itemGrid");
    const outfitSlotsContainer = document.getElementById("outfitSlots");
    const mobileMode = isMobileViewport();

    if (!itemGridElement || !outfitSlotsContainer) {
      return;
    }

    const clearDropTargets = () => {
      outfitSlotsContainer.querySelectorAll(".slot.drop-target").forEach((slot) => {
        slot.classList.remove("drop-target");
      });
    };

    let activeDraggedSlotId = null;
    let slotDragDropHandled = false;

    itemGridElement.querySelectorAll(".item-card").forEach((card) => {
      card.setAttribute("draggable", mobileMode ? "false" : "true");

      if (card.dataset.dragBound === "true") {
        return;
      }

      card.dataset.dragBound = "true";

      if (mobileMode) {
        return;
      }

      card.addEventListener("dragstart", (event) => {
        const itemName = card.querySelector(".item-info .title-container a").textContent;
        event.dataTransfer.setData("text/plain", itemName);
        event.dataTransfer.effectAllowed = "move";

        let dragPreview = null;
        if (!isMobileViewport()) {
          dragPreview = card.cloneNode(true);
          dragPreview.classList.add("drag-preview");
          dragPreview.style.position = "fixed";
          dragPreview.style.top = "-9999px";
          dragPreview.style.left = "-9999px";
          dragPreview.style.width = `${card.offsetWidth}px`;
          dragPreview.style.pointerEvents = "none";
          dragPreview.style.transform = "scale(0.6)";
          dragPreview.style.transformOrigin = "top left";
          dragPreview.style.zIndex = "9999";
          document.body.appendChild(dragPreview);
          event.dataTransfer.setDragImage(dragPreview, 20, 20);
        }

        card._dragPreview = dragPreview;
        card.classList.add("dragging");
        document.body.classList.add("is-dragging-item");
      });

      card.addEventListener("dragend", () => {
        if (card._dragPreview) {
          card._dragPreview.remove();
          card._dragPreview = null;
        }
        card.classList.remove("dragging");
        document.body.classList.remove("is-dragging-item");
        clearDropTargets();
      });
    });

    outfitSlotsContainer.querySelectorAll(".slot.equipped-slot").forEach((slot) => {
      slot.setAttribute("draggable", mobileMode ? "false" : "true");

      if (slot.dataset.slotDragBound === "true") {
        return;
      }
      slot.dataset.slotDragBound = "true";

      if (mobileMode) {
        return;
      }

      slot.addEventListener("dragstart", (event) => {
        const slotId = slot.dataset.slotId;
        activeDraggedSlotId = slotId;
        slotDragDropHandled = false;
        event.dataTransfer.setData("application/x-slot-id", slotId);
        event.dataTransfer.setData("text/plain", "unequip-slot-item");
        event.dataTransfer.effectAllowed = "move";
        document.body.classList.add("is-dragging-item");
      });

      slot.addEventListener("dragend", () => {
        if (activeDraggedSlotId && !slotDragDropHandled) {
          removeItemFromSlot(activeDraggedSlotId);
        }

        activeDraggedSlotId = null;
        slotDragDropHandled = false;
        document.body.classList.remove("is-dragging-item");
        clearDropTargets();
      });
    });

    if (outfitSlotsContainer.dataset.dropBound === "true") {
      return;
    }

    outfitSlotsContainer.dataset.dropBound = "true";

    document.addEventListener("dragover", (event) => {
      const slot = event.target.closest("#outfitSlots .slot");
      if (slot) {
        event.preventDefault();
        clearDropTargets();
        slot.classList.add("drop-target");
        return;
      }

      if (event.dataTransfer && event.dataTransfer.types.includes("application/x-slot-id")) {
        event.preventDefault();
      }
    });

    document.addEventListener("dragleave", (event) => {
      const slot = event.target.closest("#outfitSlots .slot");
      if (!slot) {
        return;
      }

      const nextTarget = event.relatedTarget;
      if (!nextTarget || !slot.contains(nextTarget)) {
        slot.classList.remove("drop-target");
      }
    });

    document.addEventListener("drop", (event) => {
      const draggedSlotId = event.dataTransfer?.getData("application/x-slot-id");
      const slotTarget = event.target.closest("#outfitSlots .slot");

      if (draggedSlotId && !slotTarget) {
        event.preventDefault();
        slotDragDropHandled = true;
        removeItemFromSlot(draggedSlotId);
        clearDropTargets();
        document.body.classList.remove("is-dragging-item");
        activeDraggedSlotId = null;
        return;
      }

      if (!slotTarget) {
        return;
      }

      event.preventDefault();
      clearDropTargets();
      document.body.classList.remove("is-dragging-item");

      if (draggedSlotId) {
        slotDragDropHandled = true;
        removeItemFromSlot(draggedSlotId);
        activeDraggedSlotId = null;
        return;
      }

      const itemName = event.dataTransfer.getData("text/plain");
      equipItemByName(itemName);
    });
  }

  function addItemToSlot(slotType, item) {
    const outfitSlots = JSON.parse(localStorage.getItem(`${window.gamePrefix}outfitSlots`)) || {};
    outfitSlots[slotType] = { name: item.name, image: item.image };
    localStorage.setItem(`${window.gamePrefix}outfitSlots`, JSON.stringify(outfitSlots));
    loadOutfitFromStorage();
  }

  if (localStorage.getItem("theme") === "light") {
    body.classList.add("light-mode");
  }
  initializeModernColorPicker();
  updateModeToggleIcon();
  updateBrandIcon();
  window.syncThemeAwareColorPicker?.(true);

  modeToggle.addEventListener("click", () => {
    body.classList.toggle("light-mode");
    localStorage.setItem("theme", body.classList.contains("light-mode") ? "light" : "dark");
    updateModeToggleIcon();
    updateBrandIcon();
  });

  toggleSearch.addEventListener("click", () => {
    const isColorPickerVisible = colorPickerGroup?.classList.contains("is-visible");
    setColorPickerVisible(!isColorPickerVisible);
    toggleSearch.textContent = isColorPickerVisible ? "Item" : "Hex";
    searchInput.placeholder = isColorPickerVisible ? "Search by item" : "Search by hex";
    searchInput.readOnly = !isColorPickerVisible;
    searchInput.setAttribute("aria-readonly", isColorPickerVisible ? "false" : "true");
    searchInput.value = "";
    window.syncThemeAwareColorPicker?.(true);
    updateMatchingItems();
  });

  setColorPickerVisible(false);
  searchInput.readOnly = false;
  searchInput.setAttribute("aria-readonly", "false");

  exportButton.addEventListener("click", () => {
    window.location.href = `simulator_${currentPage}`;
  });

  window.addEventListener(
    "resize",
    () => {
      updatePageScrollOffset();
      bindScrollHost();
      adjustPinnedStyles();
      initializeDragAndDrop();
      updateScrollUI();
      closeMobileActionSheet();
      closeDesktopSlotContextMenu();
    },
    { passive: true }
  );

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      closeMobileActionSheet();
      closeDesktopSlotContextMenu();
    }
  });

  document.querySelector(".back-to-top-button").addEventListener("click", () => {
    scrollPageToTop();
    showNav();
    hideOutfitSidebar();
  });

  document.addEventListener("DOMContentLoaded", () => {
    const fullScreenNotice = document.getElementById("fullScreenNotice");
    const dismissNotice = document.getElementById("dismissNotice");

    if (!localStorage.getItem("noticeDismissed")) {
      fullScreenNotice.classList.add("show");
    }

    dismissNotice.addEventListener("click", () => {
      fullScreenNotice.classList.remove("show");
      localStorage.setItem("noticeDismissed", "true");
    });
  });

  window.isMobileViewport = isMobileViewport;
  window.showOutfitSidebar = showOutfitSidebar;
  window.hideOutfitSidebar = hideOutfitSidebar;
  window.showNav = showNav;
  window.hideNav = hideNav;
  window.adjustPinnedStyles = adjustPinnedStyles;
  window.loadOutfitFromStorage = loadOutfitFromStorage;
  window.showContextMenu = showContextMenu;
  window.initializeItemGrid = initializeItemGrid;
  window.initializeDragAndDrop = initializeDragAndDrop;
  window.removeItemFromSlot = removeItemFromSlot;
  window.addItemToSlot = addItemToSlot;
  window.equipItemToOutfit = equipItemToOutfit;
  window.openMobileItemActionSheet = openMobileItemActionSheet;
  window.openMobileSlotActionSheet = openMobileSlotActionSheet;
  window.scrollPageToTop = scrollPageToTop;

  window.onload = function () {
    buildSiteMenu();
    initializeModernColorPicker();
    updateBrandIcon();
    ensurePageScrollRegion();
    updatePageScrollOffset();
    bindScrollHost();
    preventMobileViewportZoom();

    fetchItems().then(() => {
      loadOutfitFromStorage();
      initializeItemGrid();
      initializeDragAndDrop();
      adjustPinnedStyles();
      updateScrollUI();
      initGridZoomControl();
      setupPinchZoom();
    });
  };

  (function setupPreloader() {
    let markedReady = false;
    const markReady = () => {
      if (markedReady) {
        return;
      }

      markedReady = true;
      document.dispatchEvent(new Event("souls:page-ready"));
    };

    window.addEventListener("initial-grid-images-loaded", markReady, { once: true });
    window.addEventListener(
      "load",
      () => {
        setTimeout(markReady, 2600);
      },
      { once: true }
    );
  })();
})();
