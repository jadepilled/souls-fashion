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
  let colorPickerTrigger = null;
  let colorPickerPopover = null;
  let colorPickerHexInput = null;
  const desktopGridLevels = Array.from({ length: 21 }, (_, index) => index + 4);
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
             <p>Make a girl smile!</p><p>Please consider supporting this project's ongoing existence if it has been useful to you.</p>
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
      5,
      Math.max(2, Number.isFinite(numericValue) ? Math.round(numericValue) : 2)
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
    const initialColumns = Number.isFinite(savedColumns)
      ? Math.min(5, Math.max(2, savedColumns))
      : 2;
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
    const itemGridElement = document.getElementById("itemGrid");
    if (!itemGridElement) {
      return;
    }

    let pinchStartDistance = null;
    let pinchStartColumns = currentMobileGridColumns;
    const pinchStepSize = 18;

    const getDistance = (touchA, touchB) => {
      const dx = touchA.clientX - touchB.clientX;
      const dy = touchA.clientY - touchB.clientY;
      return Math.hypot(dx, dy);
    };

    const onTouchStart = (event) => {
      if (!isMobileViewport() || event.touches.length !== 2) {
        return;
      }

      pinchStartDistance = getDistance(event.touches[0], event.touches[1]);
      pinchStartColumns = currentMobileGridColumns;
      event.preventDefault();
    };

    const onTouchMove = (event) => {
      if (!isMobileViewport() || pinchStartDistance === null || event.touches.length !== 2) {
        return;
      }

      const currentDistance = getDistance(event.touches[0], event.touches[1]);
      const delta = currentDistance - pinchStartDistance;
      const steps = Math.trunc(delta / pinchStepSize);

      if (steps !== 0) {
        applyMobileGridColumns(pinchStartColumns - steps);
      }

      event.preventDefault();
    };

    const onTouchEnd = (event) => {
      if (event.touches.length < 2) {
        pinchStartDistance = null;
      }
    };

    itemGridElement.addEventListener("touchstart", onTouchStart, { passive: false });
    itemGridElement.addEventListener("touchmove", onTouchMove, { passive: false });
    itemGridElement.addEventListener("touchend", onTouchEnd, { passive: true });
    itemGridElement.addEventListener("touchcancel", onTouchEnd, { passive: true });
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

  function removeItemFromSlot(slotId) {
    const outfit = JSON.parse(localStorage.getItem(`${window.gamePrefix}outfitSlots`)) || {};
    if (!outfit[slotId]) {
      return;
    }

    delete outfit[slotId];
    localStorage.setItem(`${window.gamePrefix}outfitSlots`, JSON.stringify(outfit));
    loadOutfitFromStorage();
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

        const img = document.createElement("img");
        img.src = `pages/${currentPage}/icons/${item.image}`;
        img.alt = item.name;
        img.draggable = false;

        const hoverLabel = document.createElement("div");
        hoverLabel.classList.add("slot-hover-name");
        hoverLabel.textContent = item.name;

        slot.addEventListener("click", () => {
          const fullItem = items.find((entry) => entry.name === item.name);
          if (fullItem) {
            updateSearchFromItem(fullItem);
          }
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
    }

    initializeDragAndDrop();
  }

  function showContextMenu(event, action, identifier) {
    const contextMenu = document.getElementById("contextMenu");
    const contextMenuList = document.getElementById("contextMenuList");
    contextMenuList.innerHTML = "";

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
      addItemToSimulator(rightClickedItem);
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

    if (!itemGridElement || !outfitSlotsContainer) {
      return;
    }

    const clearDropTargets = () => {
      outfitSlotsContainer.querySelectorAll(".slot.drop-target").forEach((slot) => {
        slot.classList.remove("drop-target");
      });
    };

    const equipItemByName = (itemName) => {
      if (!itemName) {
        return;
      }

      const item = items.find((entry) => entry.name === itemName);
      if (!item) {
        console.error("Item not found in loaded item data:", itemName);
        return;
      }

      let slotType = `${item.type}Slot`;
      if (item.type === "weapons" || item.type === "shields") {
        const outfitSlots =
          JSON.parse(localStorage.getItem(`${window.gamePrefix}outfitSlots`)) || {};
        const alternateSlot = slotType === "weaponsSlot" ? "shieldsSlot" : "weaponsSlot";
        slotType = outfitSlots[slotType] ? alternateSlot : slotType;
      }

      addItemToSlot(slotType, item);
    };

    let activeDraggedSlotId = null;
    let slotDragDropHandled = false;

    itemGridElement.querySelectorAll(".item-card").forEach((card) => {
      if (card.dataset.dragBound === "true") {
        return;
      }

      card.dataset.dragBound = "true";
      card.setAttribute("draggable", "true");

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

      card.addEventListener(
        "touchstart",
        (event) => {
          const touch = event.touches[0];
          if (!touch) return;
          card.dataset.touchDragStartX = String(touch.clientX);
          card.dataset.touchDragStartY = String(touch.clientY);
          card.dataset.touchDragging = "false";
        },
        { passive: true }
      );

      card.addEventListener(
        "touchmove",
        (event) => {
          const touch = event.touches[0];
          if (!touch) return;
          const startX = Number(card.dataset.touchDragStartX || touch.clientX);
          const startY = Number(card.dataset.touchDragStartY || touch.clientY);
          const movedDistance = Math.hypot(touch.clientX - startX, touch.clientY - startY);
          if (movedDistance >= 14) {
            card.dataset.touchDragging = "true";
            event.preventDefault();
          }
        },
        { passive: false }
      );

      card.addEventListener(
        "touchend",
        (event) => {
          const changed = event.changedTouches[0];
          if (!changed) return;

          const startX = Number(card.dataset.touchDragStartX || changed.clientX);
          const startY = Number(card.dataset.touchDragStartY || changed.clientY);
          const movedDistance = Math.hypot(changed.clientX - startX, changed.clientY - startY);
          if (movedDistance < 18 || card.dataset.touchDragging !== "true") {
            return;
          }

          const target = document.elementFromPoint(changed.clientX, changed.clientY);
          const slotTarget = target ? target.closest("#outfitSlots .slot") : null;
          if (!slotTarget) {
            clearDropTargets();
            return;
          }

          const itemName = card.querySelector(".item-info .title-container a")?.textContent || "";
          equipItemByName(itemName);
          clearDropTargets();
        },
        { passive: true }
      );
    });

    outfitSlotsContainer.querySelectorAll(".slot.equipped-slot").forEach((slot) => {
      slot.setAttribute("draggable", "true");

      if (slot.dataset.slotDragBound === "true") {
        return;
      }
      slot.dataset.slotDragBound = "true";

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

      slot.addEventListener(
        "touchstart",
        (event) => {
          const touch = event.touches[0];
          slot.dataset.touchStartX = String(touch.clientX);
          slot.dataset.touchStartY = String(touch.clientY);
        },
        { passive: true }
      );

      slot.addEventListener(
        "touchend",
        (event) => {
          const changed = event.changedTouches[0];
          if (!changed) return;

          const startX = Number(slot.dataset.touchStartX || changed.clientX);
          const startY = Number(slot.dataset.touchStartY || changed.clientY);
          const movedDistance = Math.hypot(changed.clientX - startX, changed.clientY - startY);
          if (movedDistance < 18) {
            return;
          }

          const slotsBounds = outfitSlotsContainer.getBoundingClientRect();
          const droppedInsideSlots =
            changed.clientX >= slotsBounds.left &&
            changed.clientX <= slotsBounds.right &&
            changed.clientY >= slotsBounds.top &&
            changed.clientY <= slotsBounds.bottom;

          if (!droppedInsideSlots) {
            removeItemFromSlot(slot.dataset.slotId);
          }
        },
        { passive: true }
      );
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
      updateScrollUI();
    },
    { passive: true }
  );

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
  window.scrollPageToTop = scrollPageToTop;

  window.onload = function () {
    buildSiteMenu();
    initializeModernColorPicker();
    updateBrandIcon();
    ensurePageScrollRegion();
    updatePageScrollOffset();
    bindScrollHost();

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
