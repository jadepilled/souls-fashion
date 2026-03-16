(function initSimulatorPage() {
  const body = document.body;
  if (!body.classList.contains("simulator-page")) {
    return;
  }

  const simulatorPage = window.location.pathname.split("/").pop().replace(/\.html$/, "");
  const gameKey = body.dataset.gameKey || simulatorPage.replace(/^simulator_/, "");
  const gameTitle = body.dataset.gameTitle || gameKey;
  const gamePrefix = `${gameKey}_`;
  const layoutOrder = ["head", "weapons", "chest", "shields", "hands", "legs"];
  const slotGridPositions = {
    head: { column: "2", row: "1" },
    weapons: { column: "1", row: "2" },
    chest: { column: "2", row: "2" },
    shields: { column: "3", row: "2" },
    hands: { column: "1", row: "3" },
    legs: { column: "2", row: "3" },
  };
  const slotLabels = {
    head: "Head",
    chest: "Chest",
    hands: "Hands",
    legs: "Legs",
    weapons: "Weapons",
    shields: "Shields",
  };
  const exportCardWidth = 200;
  const exportCardHeight = 260;
  const exportGap = 15;
  const exportStageWidth = exportCardWidth * 3 + exportGap * 2;
  const exportStageHeight = exportCardHeight * 3 + exportGap * 2;
  const exportFooterText = "Created using souls.fashion v1.0.9";
  const defaultOutfitName = "Current Outfit";
  const colorMatchWeight = 0.35;
  const presetStorageKey = `${gamePrefix}presets`;
  const legacyPresetCount = 5;

  let currentOutfitName = defaultOutfitName;
  let simulatorStageShell = null;
  let stageResizeObserver = null;
  let presetDrawerToggle = null;
  let presetDrawerBackdrop = null;
  let simulatorContextMenu = null;
  let simulatorContextBody = null;
  let simulatorContextTitle = null;
  let simulatorContextSubtitle = null;
  let simulatorContextActions = null;
  let activeContextMode = "replace";
  let activeContextSlotId = "";
  let activeContextItem = null;
  let activeContextSearch = "";
  let itemCatalog = [];
  let itemMap = new Map();
  let presetCollection = [];

  function isMobileViewport() {
    return window.matchMedia("(max-width: 1199px)").matches;
  }

  function isLightModeActive() {
    return body.classList.contains("light-mode") || localStorage.getItem("theme") === "light";
  }

  function getThemeIconPath() {
    return isLightModeActive() ? "icons/FS_icon_black.png" : "icons/FS_icon_white.png";
  }

  function getExportTheme() {
    if (isLightModeActive()) {
      return {
        background: "#f5f5f5",
        text: "#141414",
        mutedText: "#5b564d",
        cardSurface: "#ebebeb",
        cardBorder: "#cfc7ba",
      };
    }

    return {
      background: "#121212",
      text: "#ffffff",
      mutedText: "#a3a3a3",
      cardSurface: "#0f0f0f",
      cardBorder: "#555555",
    };
  }

  function getExportHeading() {
    return `${currentOutfitName} - ${gameTitle}`;
  }

  function getExportFilename() {
    return `${getExportHeading().replace(/[<>:"/\\|?*]+/g, "").replace(/\s+/g, " ").trim()}_Outfit.png`;
  }

  function getSlotKey(slotType) {
    return `${slotType}Slot`;
  }

  function getOutfitData() {
    try {
      return JSON.parse(localStorage.getItem(`${gamePrefix}outfitSlots`)) || {};
    } catch (error) {
      console.error("Unable to read simulator outfit data:", error);
      return {};
    }
  }

  function saveOutfitData(outfit) {
    localStorage.setItem(`${gamePrefix}outfitSlots`, JSON.stringify(outfit));
  }

  function getDefaultPresetName(index) {
    return `Preset ${index}`;
  }

  function createPresetId() {
    return `preset_${Date.now().toString(36)}_${Math.random().toString(36).slice(2, 8)}`;
  }

  function sanitizeStoredOutfit(outfit) {
    if (!outfit || typeof outfit !== "object" || Array.isArray(outfit)) {
      return null;
    }

    const normalized = {};
    Object.entries(outfit).forEach(([slotId, value]) => {
      if (
        /Slot$/.test(slotId) &&
        value &&
        typeof value === "object" &&
        typeof value.name === "string" &&
        typeof value.image === "string"
      ) {
        normalized[slotId] = { name: value.name, image: value.image };
      }
    });

    return normalized;
  }

  function cloneOutfit(outfit) {
    return JSON.parse(JSON.stringify(outfit || {}));
  }

  function createPreset(index, data = {}) {
    return {
      id: typeof data.id === "string" && data.id ? data.id : createPresetId(),
      name:
        typeof data.name === "string" && data.name.trim()
          ? data.name.replace(/\s+/g, " ").trim()
          : getDefaultPresetName(index),
      outfit: sanitizeStoredOutfit(data.outfit),
    };
  }

  function savePresetCollection(presets = presetCollection) {
    presetCollection = presets.map((preset, index) => createPreset(index + 1, preset));
    localStorage.setItem(presetStorageKey, JSON.stringify(presetCollection));
    return presetCollection;
  }

  function migrateLegacyPresets() {
    return Array.from({ length: legacyPresetCount }, (_, index) => {
      const presetNumber = index + 1;
      let outfit = null;

      try {
        outfit = sanitizeStoredOutfit(
          JSON.parse(localStorage.getItem(`${gamePrefix}preset${presetNumber}`) || "null")
        );
      } catch (error) {
        outfit = null;
      }

      return createPreset(presetNumber, {
        id: `legacy_${presetNumber}`,
        name:
          localStorage.getItem(`${gamePrefix}presetName${presetNumber}`) ||
          getDefaultPresetName(presetNumber),
        outfit,
      });
    });
  }

  function loadPresetCollection() {
    try {
      const parsed = JSON.parse(localStorage.getItem(presetStorageKey) || "null");
      if (Array.isArray(parsed) && parsed.length > 0) {
        return parsed.map((preset, index) => createPreset(index + 1, preset));
      }
    } catch (error) {
      console.warn("Unable to read preset collection:", error);
    }

    const migrated = migrateLegacyPresets();
    savePresetCollection(migrated);
    return migrated;
  }

  function getPresetById(presetId) {
    return presetCollection.find((preset) => preset.id === presetId) || null;
  }

  function getNextPresetName() {
    let nextIndex = presetCollection.length + 1;
    let candidate = getDefaultPresetName(nextIndex);

    while (presetCollection.some((preset) => preset.name === candidate)) {
      nextIndex += 1;
      candidate = getDefaultPresetName(nextIndex);
    }

    return candidate;
  }

  function countPresetItems(preset) {
    return preset?.outfit ? Object.keys(preset.outfit).length : 0;
  }

  function findMatchingPreset(outfit) {
    const normalizedOutfit = sanitizeStoredOutfit(outfit);
    if (!normalizedOutfit) {
      return null;
    }

    const outfitString = JSON.stringify(normalizedOutfit);
    return (
      presetCollection.find((preset) => {
        if (!preset.outfit) {
          return false;
        }

        return JSON.stringify(preset.outfit) === outfitString;
      }) || null
    );
  }

  function getPlaceholderText(slotId) {
    switch (slotId) {
      case "head":
        return "No helm equipped.";
      case "chest":
        return "No chest armor equipped.";
      case "hands":
        return "No gauntlets equipped.";
      case "legs":
        return "No leg armor equipped.";
      case "weapons":
        return "No main-hand item equipped.";
      case "shields":
        return "No off-hand item equipped.";
      default:
        return `No ${slotId} item selected.`;
    }
  }

  function createDownloadCard() {
    const card = document.createElement("div");
    card.id = "downloadImageLink";
    card.className = "item-card-simple simulator-download-card";
    card.setAttribute("role", "button");
    card.setAttribute("tabindex", "0");
    card.setAttribute("aria-label", "Download outfit image");
    card.style.gridColumn = "1";
    card.style.gridRow = "1";

    const label = document.createElement("p");
    label.className = "placeholder-tile simulator-download-label";
    label.textContent = "Download outfit image";

    card.appendChild(label);

    const handleActivate = () => {
      downloadSimulatorImage();
    };

    card.addEventListener("click", handleActivate);
    card.addEventListener("keydown", (event) => {
      if (event.key === "Enter" || event.key === " ") {
        event.preventDefault();
        handleActivate();
      }
    });

    return card;
  }

  function inferItemType(item = {}) {
    if (item.type) {
      return item.type;
    }

    const imagePath = item.image || "";
    const category = imagePath.split("/")[0].toLowerCase();
    if (category.includes("head")) return "head";
    if (category.includes("chest")) return "chest";
    if (category.includes("hand")) return "hands";
    if (category.includes("leg")) return "legs";
    if (category.includes("shield")) return "shields";
    if (category.includes("weapon")) return "weapons";
    return "";
  }

  function normalizeItem(savedItem) {
    if (!savedItem) {
      return null;
    }

    const catalogItem = itemMap.get(savedItem.name);
    if (catalogItem) {
      return catalogItem;
    }

    return {
      ...savedItem,
      type: inferItemType(savedItem),
      link: savedItem.link || "",
      primaryColor: savedItem.primaryColor || "",
      secondaryColors: Array.isArray(savedItem.secondaryColors)
        ? savedItem.secondaryColors
        : [],
    };
  }

  async function fetchItemCatalog() {
    try {
      const response = await fetch(`pages/${gameKey}/typed_items_for_web.json`);
      if (!response.ok) {
        throw new Error(`HTTP ${response.status}`);
      }

      itemCatalog = await response.json();
      itemMap = new Map(itemCatalog.map((item) => [item.name, item]));
    } catch (error) {
      console.error("Unable to load simulator item catalog:", error);
      itemCatalog = [];
      itemMap = new Map();
    }
  }

  function createLinkedItemName(item) {
    if (item?.link) {
      const link = document.createElement("a");
      link.className = "simulator-item-link";
      link.href = item.link;
      link.target = "_blank";
      link.rel = "noopener noreferrer";
      link.textContent = item.name;
      link.addEventListener("click", (event) => {
        event.stopPropagation();
      });
      return link;
    }

    const label = document.createElement("span");
    label.textContent = item?.name || "";
    return label;
  }

  function createSimulatorCard(slotId, savedItem, options = {}) {
    const { exportMode = false, exportTheme = null } = options;
    const item = normalizeItem(savedItem);
    const card = document.createElement("div");
    card.classList.add("item-card-simple");
    card.dataset.slotId = getSlotKey(slotId);
    card.dataset.slotType = slotId;

    if (!exportMode) {
      card.id = `${slotId}Card`;
    } else {
      const gridPosition = slotGridPositions[slotId];
      card.style.gridColumn = gridPosition.column;
      card.style.gridRow = gridPosition.row;
      card.style.display = "flex";
      card.style.flexDirection = "column";
      card.style.width = `${exportCardWidth}px`;
      card.style.height = `${exportCardHeight}px`;
      card.style.padding = "10px";
      card.style.border = `1px solid ${(exportTheme?.cardBorder || "#555555")}`;
      card.style.borderRadius = "10px";
      card.style.backgroundColor = exportTheme?.cardSurface || "#0f0f0f";
      card.style.color = exportTheme?.text || "#ffffff";
      card.style.textAlign = "center";
      card.style.fontFamily = "'Spectral', Helvetica, Arial, sans-serif";
    }

    if (item) {
      card.classList.add("equipped-simulator-item");
      card.dataset.itemName = item.name;

      const img = document.createElement("img");
      img.src = `pages/${gameKey}/icons/${item.image}`;
      img.alt = item.name;

      if (exportMode) {
        img.style.width = "100%";
        img.style.maxHeight = "150px";
        img.style.objectFit = "contain";
        img.style.margin = "0 auto";
      }

      const name = document.createElement(exportMode ? "p" : "div");
      if (exportMode) {
        name.textContent = item.name;
        name.style.margin = "0.75rem 0 0 0";
        name.style.fontSize = "0.9rem";
        name.style.lineHeight = "1.2";
      } else {
        name.appendChild(createLinkedItemName(item));
      }

      card.appendChild(img);
      card.appendChild(name);
    } else {
      const placeholder = document.createElement("p");
      placeholder.classList.add("placeholder-tile");
      placeholder.textContent = getPlaceholderText(slotId);

      if (exportMode) {
        placeholder.style.display = "flex";
        placeholder.style.alignItems = "center";
        placeholder.style.justifyContent = "center";
        placeholder.style.width = "100%";
        placeholder.style.height = "100%";
        placeholder.style.margin = "0";
        placeholder.style.padding = "0";
        placeholder.style.background = "transparent";
        placeholder.style.border = "none";
        placeholder.style.fontSize = "0.85rem";
        placeholder.style.lineHeight = "1.35";
        placeholder.style.color = exportTheme?.mutedText || "#a3a3a3";
      }

      card.appendChild(placeholder);
    }

    return card;
  }

  function findMatchingPresetName(outfit) {
    return findMatchingPreset(outfit)?.name || defaultOutfitName;
  }

  function syncCurrentOutfitName() {
    currentOutfitName = findMatchingPresetName(getOutfitData());
  }

  function addPreset() {
    savePresetCollection([
      ...presetCollection,
      createPreset(presetCollection.length + 1, { name: getNextPresetName(), outfit: null }),
    ]);
    renderPresetList();
    syncCurrentOutfitName();
  }

  function clearPreset(presetId) {
    savePresetCollection(
      presetCollection.map((preset) =>
        preset.id === presetId ? { ...preset, outfit: null } : preset
      )
    );
    setPresetDrawerOpen(false);
    syncCurrentOutfitName();
    renderPresetList();
  }

  function savePreset(presetId) {
    const currentOutfit = cloneOutfit(sanitizeStoredOutfit(getOutfitData()) || {});
    savePresetCollection(
      presetCollection.map((preset) =>
        preset.id === presetId ? { ...preset, outfit: currentOutfit } : preset
      )
    );
    currentOutfitName = getPresetById(presetId)?.name || defaultOutfitName;
    setPresetDrawerOpen(false);
    renderPresetList();
  }

  function loadPreset(presetId) {
    const preset = getPresetById(presetId);
    if (!preset?.outfit) {
      return;
    }

    saveOutfitData(cloneOutfit(preset.outfit));
    currentOutfitName = preset.name;
    loadOutfitFromStorage();
    setPresetDrawerOpen(false);
  }

  function deletePreset(presetId) {
    if (presetCollection.length <= 1) {
      clearPreset(presetId);
      return;
    }

    savePresetCollection(presetCollection.filter((preset) => preset.id !== presetId));
    renderPresetList();
    syncCurrentOutfitName();
  }

  function updatePresetName(presetId, value) {
    const presetIndex = presetCollection.findIndex((preset) => preset.id === presetId);
    if (presetIndex === -1) {
      return;
    }

    const cleanedValue =
      value.replace(/\s+/g, " ").trim() || getDefaultPresetName(presetIndex + 1);
    savePresetCollection(
      presetCollection.map((preset) =>
        preset.id === presetId ? { ...preset, name: cleanedValue } : preset
      )
    );
    syncCurrentOutfitName();
    renderPresetList();
  }

  function createPresetAction(action, presetId, label, disabled = false) {
    const button = document.createElement("button");
    button.type = "button";
    button.className = "preset-action";
    button.dataset.action = action;
    button.dataset.presetId = presetId;
    button.textContent = label;
    button.disabled = disabled;
    return button;
  }

  function createPresetCard(preset, index, activePresetId) {
    const card = document.createElement("article");
    card.className = "preset";
    card.dataset.presetId = preset.id;
    if (preset.id === activePresetId) {
      card.classList.add("is-active");
    }

    const header = document.createElement("div");
    header.className = "preset-head";

    const badge = document.createElement("span");
    badge.className = "preset-badge";
    badge.textContent = `Preset ${index + 1}`;
    header.appendChild(badge);

    if (presetCollection.length > 1) {
      const deleteButton = document.createElement("button");
      deleteButton.type = "button";
      deleteButton.className = "preset-delete-button";
      deleteButton.dataset.presetId = preset.id;
      deleteButton.setAttribute("aria-label", `Delete ${preset.name}`);
      deleteButton.textContent = "×";
      header.appendChild(deleteButton);
    }

    const name = document.createElement("h3");
    name.className = "editable-preset-name";
    name.dataset.presetId = preset.id;
    name.contentEditable = "true";
    name.spellcheck = false;
    name.textContent = preset.name;

    const slotCount = countPresetItems(preset);
    const meta = document.createElement("p");
    meta.className = "preset-meta";
    meta.textContent =
      preset.outfit === null
        ? "Empty preset"
        : slotCount === 0
          ? "Saved empty look"
          : `${slotCount} equipped slot${slotCount === 1 ? "" : "s"} saved`;

    const actions = document.createElement("div");
    actions.className = "preset-actions";
    actions.appendChild(createPresetAction("save", preset.id, "Save"));
    actions.appendChild(createPresetAction("load", preset.id, "Load", preset.outfit === null));
    actions.appendChild(createPresetAction("clear", preset.id, "Clear", preset.outfit === null));

    card.appendChild(header);
    card.appendChild(name);
    card.appendChild(meta);
    card.appendChild(actions);
    return card;
  }

  function renderPresetList() {
    const presetContainer = document.getElementById("presetContainer");
    if (!presetContainer) {
      return;
    }

    const matchingPreset = findMatchingPreset(getOutfitData());
    const activePresetId = matchingPreset?.id || "";
    presetContainer.innerHTML = "";

    const railHeader = document.createElement("div");
    railHeader.className = "preset-rail-header";

    const railCopy = document.createElement("div");
    railCopy.className = "preset-rail-copy";

    const title = document.createElement("p");
    title.className = "preset-rail-title";
    title.textContent = "Presets";

    const subtitle = document.createElement("p");
    subtitle.className = "preset-rail-subtitle";
    subtitle.textContent = `${presetCollection.length} look${presetCollection.length === 1 ? "" : "s"} ready`;

    railCopy.appendChild(title);
    railCopy.appendChild(subtitle);

    const addButton = document.createElement("button");
    addButton.type = "button";
    addButton.className = "preset-add-button";
    addButton.textContent = "New Preset";

    railHeader.appendChild(railCopy);
    railHeader.appendChild(addButton);
    presetContainer.appendChild(railHeader);

    const presetList = document.createElement("div");
    presetList.className = "preset-list";

    presetCollection.forEach((preset, index) => {
      presetList.appendChild(createPresetCard(preset, index, activePresetId));
    });

    presetContainer.appendChild(presetList);
  }

  function setPresetDrawerOpen(open) {
    const shouldOpen = Boolean(open) && isMobileViewport();
    document.body.classList.toggle("simulator-drawer-open", shouldOpen);

    if (presetDrawerToggle) {
      presetDrawerToggle.setAttribute("aria-expanded", shouldOpen ? "true" : "false");
      presetDrawerToggle.textContent = shouldOpen ? "Close Presets" : "Presets";
    }
  }

  function syncPresetDrawerState() {
    if (!isMobileViewport()) {
      document.body.classList.remove("simulator-drawer-open");
    }

    if (presetDrawerToggle) {
      const isOpen = document.body.classList.contains("simulator-drawer-open");
      presetDrawerToggle.hidden = !isMobileViewport();
      presetDrawerToggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
      presetDrawerToggle.textContent = isOpen ? "Close Presets" : "Presets";
    }
  }

  function ensureSimulatorStructure() {
    const simulatorGrid = document.getElementById("outfitSlotsSimulator");
    const topbar = document.querySelector(".simulator-page-topbar");
    if (!simulatorGrid) {
      return;
    }

    if (!simulatorGrid.parentElement.classList.contains("simulator-stage")) {
      const shell = document.createElement("div");
      shell.className = "simulator-stage-shell";

      const stage = document.createElement("div");
      stage.className = "simulator-stage";

      simulatorGrid.parentNode.insertBefore(shell, simulatorGrid);
      shell.appendChild(stage);
      stage.appendChild(simulatorGrid);
    }

    simulatorStageShell = document.querySelector(".simulator-stage-shell");

    if (typeof ResizeObserver === "function" && simulatorStageShell && !stageResizeObserver) {
      const scaleHost =
        simulatorStageShell.closest(".outfit-sim") || simulatorStageShell.parentElement;
      if (scaleHost) {
        stageResizeObserver = new ResizeObserver(() => {
          updateSimulatorScale();
        });
        stageResizeObserver.observe(scaleHost);
      }
    }

    if (!document.querySelector(".preset-drawer-toggle")) {
      presetDrawerToggle = document.createElement("button");
      presetDrawerToggle.type = "button";
      presetDrawerToggle.className = "preset-drawer-toggle";
      presetDrawerToggle.setAttribute("aria-controls", "presetContainer");
      presetDrawerToggle.setAttribute("aria-expanded", "false");
      presetDrawerToggle.textContent = "Presets";
      topbar?.appendChild(presetDrawerToggle);
    } else {
      presetDrawerToggle = document.querySelector(".preset-drawer-toggle");
      if (topbar && presetDrawerToggle.parentElement !== topbar) {
        topbar.appendChild(presetDrawerToggle);
      }
    }

    if (!document.querySelector(".preset-drawer-backdrop")) {
      presetDrawerBackdrop = document.createElement("div");
      presetDrawerBackdrop.className = "preset-drawer-backdrop";
      document.body.appendChild(presetDrawerBackdrop);
    } else {
      presetDrawerBackdrop = document.querySelector(".preset-drawer-backdrop");
    }
  }

  function ensureContextMenu() {
    if (simulatorContextMenu) {
      return;
    }

    simulatorContextMenu = document.createElement("div");
    simulatorContextMenu.id = "simulatorContextMenu";
    simulatorContextMenu.className = "simulator-context-menu";
    simulatorContextMenu.setAttribute("aria-hidden", "true");
    simulatorContextMenu.innerHTML = `
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

    document.body.appendChild(simulatorContextMenu);
    simulatorContextBody = simulatorContextMenu.querySelector(".simulator-context-body");
    simulatorContextTitle = simulatorContextMenu.querySelector(".simulator-context-title");
    simulatorContextSubtitle = simulatorContextMenu.querySelector(".simulator-context-subtitle");
    simulatorContextActions = simulatorContextMenu.querySelector(".simulator-context-actions");

    simulatorContextMenu
      .querySelector(".simulator-context-close")
      .addEventListener("click", closeContextMenu);

    simulatorContextMenu.querySelectorAll(".simulator-context-action").forEach((button) => {
      button.addEventListener("click", () => {
        const mode = button.dataset.mode;
        if (mode === "unequip") {
          removeSimulatorSlotItem(activeContextSlotId);
          closeContextMenu();
          return;
        }

        activeContextMode = mode;
        renderContextBody();
      });
    });
  }

  function setActiveContextMetadata(slotId, item) {
    activeContextSlotId = slotId;
    activeContextItem = normalizeItem(item);
    activeContextSearch = "";

    if (simulatorContextTitle) {
      simulatorContextTitle.textContent = activeContextItem?.name || "Select Item";
    }

    if (simulatorContextSubtitle) {
      const slotType = slotId.replace(/Slot$/, "");
      simulatorContextSubtitle.textContent = slotLabels[slotType] || slotType;
    }
  }

  function positionContextMenu(clientX, clientY) {
    if (!simulatorContextMenu) {
      return;
    }

    simulatorContextMenu.classList.add("is-open");
    simulatorContextMenu.style.visibility = "hidden";
    simulatorContextMenu.style.left = "0px";
    simulatorContextMenu.style.top = "0px";

    const maxLeft = Math.max(8, window.innerWidth - simulatorContextMenu.offsetWidth - 8);
    const maxTop = Math.max(8, window.innerHeight - simulatorContextMenu.offsetHeight - 8);
    const left = Math.min(Math.max(8, clientX), maxLeft);
    const top = Math.min(Math.max(8, clientY), maxTop);

    simulatorContextMenu.style.left = `${left}px`;
    simulatorContextMenu.style.top = `${top}px`;
    simulatorContextMenu.style.visibility = "visible";
    simulatorContextMenu.setAttribute("aria-hidden", "false");
  }

  function closeContextMenu() {
    if (!simulatorContextMenu) {
      return;
    }

    simulatorContextMenu.classList.remove("is-open");
    simulatorContextMenu.style.visibility = "";
    simulatorContextMenu.setAttribute("aria-hidden", "true");
  }

  function getItemsForSlot(slotType) {
    return itemCatalog.filter((item) => item.type === slotType);
  }

  function hexToLAB(hex) {
    const bigint = parseInt(hex.slice(1), 16);
    let red = (bigint >> 16) & 255;
    let green = (bigint >> 8) & 255;
    let blue = bigint & 255;
    let x;
    let y;
    let z;

    red /= 255;
    green /= 255;
    blue /= 255;

    red = red > 0.04045 ? Math.pow((red + 0.055) / 1.055, 2.4) : red / 12.92;
    green = green > 0.04045 ? Math.pow((green + 0.055) / 1.055, 2.4) : green / 12.92;
    blue = blue > 0.04045 ? Math.pow((blue + 0.055) / 1.055, 2.4) : blue / 12.92;

    x = (red * 0.4124 + green * 0.3576 + blue * 0.1805) / 0.95047;
    y = (red * 0.2126 + green * 0.7152 + blue * 0.0722) / 1.0;
    z = (red * 0.0193 + green * 0.1192 + blue * 0.9505) / 1.08883;

    x = x > 0.008856 ? Math.pow(x, 1 / 3) : 7.787 * x + 16 / 116;
    y = y > 0.008856 ? Math.pow(y, 1 / 3) : 7.787 * y + 16 / 116;
    z = z > 0.008856 ? Math.pow(z, 1 / 3) : 7.787 * z + 16 / 116;

    return [(116 * y) - 16, 500 * (x - y), 200 * (y - z)];
  }

  function calculateDistance(labA, labB) {
    const Kl = 5.0;
    const K1 = 0.048;
    const K2 = 0.014;
    const deltaL = labA[0] - labB[0];
    const deltaA = labA[1] - labB[1];
    const deltaB = labA[2] - labB[2];
    const c1 = Math.sqrt(labA[1] * labA[1] + labA[2] * labA[2]);
    const c2 = Math.sqrt(labB[1] * labB[1] + labB[2] * labB[2]);
    const deltaC = c1 - c2;
    let deltaH = deltaA * deltaA + deltaB * deltaB - deltaC * deltaC;
    deltaH = deltaH < 0 ? 0 : Math.sqrt(deltaH);
    const sc = 1.0 + K1 * c1;
    const sh = 1.0 + K2 * c1;
    const deltaLKlsl = deltaL / Kl;
    const deltaCkcsc = deltaC / sc;
    const deltaHkhsh = deltaH / sh;
    const value =
      deltaLKlsl * deltaLKlsl + deltaCkcsc * deltaCkcsc + deltaHkhsh * deltaHkhsh;
    return value < 0 ? 0 : Math.sqrt(value);
  }

  function calculateWeightedDistance(inputLAB, primaryColor, secondaryColors, secondaryWeight) {
    const primaryLAB = hexToLAB(primaryColor);
    const primaryDistance = calculateDistance(inputLAB, primaryLAB);
    const normalizedSecondaryColors = Array.isArray(secondaryColors) && secondaryColors.length > 0
      ? secondaryColors
      : [primaryColor];

    const secondaryDistances = normalizedSecondaryColors.map((secondaryColor) =>
      calculateDistance(inputLAB, hexToLAB(secondaryColor))
    );

    const minSecondaryDistance = Math.min(...secondaryDistances);
    return (1 - secondaryWeight) * primaryDistance + secondaryWeight * minSecondaryDistance;
  }

  function getColorMatches(slotType, item) {
    if (!item?.primaryColor) {
      return [];
    }

    const inputLAB = hexToLAB(item.primaryColor);
    return getItemsForSlot(slotType)
      .filter((candidate) => candidate.name !== item.name && candidate.primaryColor)
      .map((candidate) => ({
        ...candidate,
        distance: calculateWeightedDistance(
          inputLAB,
          candidate.primaryColor,
          candidate.secondaryColors,
          colorMatchWeight
        ),
      }))
      .sort((left, right) => left.distance - right.distance)
      .slice(0, 8);
  }

  function createReplacementOption(item, onClick) {
    const option = document.createElement("button");
    option.type = "button";
    option.className = "simulator-replacement-option";

    const image = document.createElement("img");
    image.src = `pages/${gameKey}/icons/${item.image}`;
    image.alt = item.name;

    const title = document.createElement("div");
    title.className = "simulator-replacement-option-title";
    title.textContent = item.name;

    option.appendChild(image);
    option.appendChild(title);
    option.addEventListener("click", onClick);
    return option;
  }

  function renderReplaceItemBody() {
    const slotType = activeContextSlotId.replace(/Slot$/, "");
    const matchingItems = getItemsForSlot(slotType)
      .filter((item) => !activeContextItem || item.name !== activeContextItem.name)
      .filter((item) =>
        item.name.toLowerCase().includes(activeContextSearch.trim().toLowerCase())
      )
      .slice(0, 14);

    const searchField = document.createElement("input");
    searchField.type = "search";
    searchField.className = "simulator-context-search";
    searchField.placeholder = activeContextItem
      ? `Replace ${slotLabels[slotType]?.toLowerCase() || "item"}...`
      : `Select ${slotLabels[slotType]?.toLowerCase() || "item"}...`;
    searchField.value = activeContextSearch;
    searchField.addEventListener("input", () => {
      activeContextSearch = searchField.value;
      renderContextBody();
    });
    simulatorContextBody.appendChild(searchField);

    if (matchingItems.length === 0) {
      const emptyState = document.createElement("p");
      emptyState.className = "simulator-context-empty";
      emptyState.textContent = "No matching items were found for that search.";
      simulatorContextBody.appendChild(emptyState);
      searchField.focus();
      return;
    }

    const list = document.createElement("div");
    list.className = "simulator-replacement-list";

    matchingItems.forEach((item) => {
      list.appendChild(
        createReplacementOption(item, () => {
          replaceItemInSlot(activeContextSlotId, item);
          closeContextMenu();
        })
      );
    });

    simulatorContextBody.appendChild(list);
    searchField.focus();
  }

  function renderReplaceByColorBody() {
    const slotType = activeContextSlotId.replace(/Slot$/, "");
    const matches = getColorMatches(slotType, activeContextItem);

    if (matches.length === 0) {
      const emptyState = document.createElement("p");
      emptyState.className = "simulator-context-empty";
      emptyState.textContent = "No similarly coloured replacements were available for this slot.";
      simulatorContextBody.appendChild(emptyState);
      return;
    }

    const grid = document.createElement("div");
    grid.className = "simulator-replacement-grid";

    matches.forEach((item) => {
      grid.appendChild(
        createReplacementOption(item, () => {
          replaceItemInSlot(activeContextSlotId, item);
          closeContextMenu();
        })
      );
    });

    simulatorContextBody.appendChild(grid);
  }

  function renderContextBody() {
    if (!simulatorContextMenu || !simulatorContextBody) {
      return;
    }

    simulatorContextBody.innerHTML = "";
    const hasActiveItem = Boolean(activeContextItem);
    if (simulatorContextActions) {
      simulatorContextActions.hidden = !hasActiveItem;
    }

    simulatorContextMenu.querySelectorAll(".simulator-context-action").forEach((button) => {
      button.classList.toggle("is-active", button.dataset.mode === activeContextMode);
    });

    if (!hasActiveItem || activeContextMode === "select") {
      renderReplaceItemBody();
      return;
    }

    if (activeContextMode === "colour") {
      renderReplaceByColorBody();
      return;
    }

    renderReplaceItemBody();
  }

  function openContextMenu(clientX, clientY, slotId, item) {
    ensureContextMenu();
    activeContextMode = item ? "replace" : "select";
    setActiveContextMetadata(slotId, item);
    renderContextBody();
    positionContextMenu(clientX, clientY);
  }

  function replaceItemInSlot(slotId, item) {
    const outfit = getOutfitData();
    outfit[slotId] = { name: item.name, image: item.image };
    saveOutfitData(outfit);
    loadOutfitFromStorage();
  }

  function removeSimulatorSlotItem(slotId) {
    if (!slotId) {
      return;
    }

    const outfit = getOutfitData();
    if (!outfit[slotId]) {
      return;
    }

    delete outfit[slotId];
    saveOutfitData(outfit);
    loadOutfitFromStorage();
  }

  function bindCardContextMenu(card, slotId, item) {
    card.addEventListener("contextmenu", (event) => {
      event.preventDefault();
      openContextMenu(event.clientX, event.clientY, slotId, item);
    });

    let longPressTimer = null;
    let touchPoint = null;

    card.addEventListener(
      "touchstart",
      (event) => {
        const touch = event.touches[0];
        if (!touch) {
          return;
        }

        touchPoint = { x: touch.clientX, y: touch.clientY };
        longPressTimer = window.setTimeout(() => {
          openContextMenu(touchPoint.x, touchPoint.y, slotId, item);
          longPressTimer = null;
        }, 475);
      },
      { passive: true }
    );

    const cancelLongPress = () => {
      if (longPressTimer) {
        clearTimeout(longPressTimer);
        longPressTimer = null;
      }
    };

    card.addEventListener("touchmove", cancelLongPress, { passive: true });
    card.addEventListener("touchend", cancelLongPress, { passive: true });
    card.addEventListener("touchcancel", cancelLongPress, { passive: true });
  }

  function loadOutfitFromStorage() {
    const outfit = getOutfitData();
    const outfitSlots = document.getElementById("outfitSlotsSimulator");
    if (!outfitSlots) {
      return;
    }

    outfitSlots.innerHTML = "";
    outfitSlots.appendChild(createDownloadCard());
    layoutOrder.forEach((slotId) => {
      const savedItem = outfit[getSlotKey(slotId)];
      const card = createSimulatorCard(slotId, savedItem);

      bindCardContextMenu(card, getSlotKey(slotId), savedItem || null);

      outfitSlots.appendChild(card);
    });

    currentOutfitName = findMatchingPresetName(outfit);
    renderPresetList();
    updateSimulatorScale();
  }

  function updateSimulatorScale() {
    if (!simulatorStageShell) {
      return;
    }

    const stageHost = simulatorStageShell.closest(".outfit-sim");
    const hostRect = stageHost?.getBoundingClientRect();
    const shellRect = simulatorStageShell.getBoundingClientRect();
    const availableWidth = Math.floor((hostRect?.width || shellRect.width || 0) - 4);
    const availableHeight = Math.floor((hostRect?.height || shellRect.height || 0) - 4);

    if (availableWidth < 120 || availableHeight < 120) {
      window.requestAnimationFrame(() => {
        updateSimulatorScale();
      });
      return;
    }

    const widthScale = availableWidth / exportStageWidth;
    const heightScale = availableHeight / exportStageHeight;
    const scale = Math.min(1, Math.max(0.3, Math.min(widthScale, heightScale)));
    const scaledHeight = Math.round(exportStageHeight * scale);

    document.documentElement.style.setProperty("--simulator-stage-scale", scale.toFixed(4));
    simulatorStageShell.style.height = `${scaledHeight}px`;
    simulatorStageShell.style.minHeight = `${scaledHeight}px`;
  }

  async function waitForImages(container) {
    const images = Array.from(container.querySelectorAll("img"));
    await Promise.all(
      images.map((image) => {
        if (image.complete && image.naturalWidth > 0) {
          return Promise.resolve();
        }

        return new Promise((resolve) => {
          image.addEventListener("load", resolve, { once: true });
          image.addEventListener("error", resolve, { once: true });
        });
      })
    );

    if (document.fonts?.ready) {
      try {
        await document.fonts.ready;
      } catch (error) {
        console.warn("Font readiness check failed:", error);
      }
    }
  }

  function createExportContainer() {
    const exportTheme = getExportTheme();
    const container = document.createElement("div");
    container.style.position = "absolute";
    container.style.left = "-9999px";
    container.style.top = "0";
    container.style.width = "742px";
    container.style.padding = "28px 32px 24px";
    container.style.backgroundColor = exportTheme.background;
    container.style.display = "flex";
    container.style.flexDirection = "column";
    container.style.alignItems = "center";
    container.style.gap = "18px";
    container.style.color = exportTheme.text;
    container.style.fontFamily = "'Spectral', Helvetica, Arial, sans-serif";

    const header = document.createElement("h3");
    header.textContent = getExportHeading();
    header.style.margin = "0";
    header.style.fontSize = "1.85rem";
    header.style.lineHeight = "1.15";
    header.style.letterSpacing = "-0.04em";
    header.style.textAlign = "center";
    container.appendChild(header);

    const simulatorDiv = document.createElement("div");
    simulatorDiv.style.display = "grid";
    simulatorDiv.style.width = `${exportStageWidth}px`;
    simulatorDiv.style.gridTemplateColumns = `repeat(3, ${exportCardWidth}px)`;
    simulatorDiv.style.gridTemplateRows = `repeat(3, ${exportCardHeight}px)`;
    simulatorDiv.style.gap = `${exportGap}px`;
    simulatorDiv.style.justifyItems = "stretch";

    const outfit = getOutfitData();
    layoutOrder.forEach((slotId) => {
      simulatorDiv.appendChild(
        createSimulatorCard(slotId, outfit[getSlotKey(slotId)], {
          exportMode: true,
          exportTheme,
        })
      );
    });
    container.appendChild(simulatorDiv);

    const footerWrap = document.createElement("div");
    footerWrap.style.display = "flex";
    footerWrap.style.flexDirection = "column";
    footerWrap.style.alignItems = "center";
    footerWrap.style.gap = "0.35rem";
    footerWrap.style.marginTop = "4px";

    const logo = document.createElement("img");
    logo.src = getThemeIconPath();
    logo.alt = "souls.fashion logo";
    logo.width = 28;
    logo.height = 28;
    logo.style.display = "block";
    logo.style.width = "28px";
    logo.style.height = "28px";
    logo.style.objectFit = "contain";
    footerWrap.appendChild(logo);

    const footer = document.createElement("p");
    footer.textContent = exportFooterText;
    footer.style.margin = "0";
    footer.style.fontSize = "0.95rem";
    footer.style.lineHeight = "1.2";
    footer.style.textAlign = "center";
    footer.style.color = exportTheme.mutedText;
    footerWrap.appendChild(footer);

    container.appendChild(footerWrap);
    return container;
  }

  async function downloadSimulatorImage() {
    if (typeof html2canvas !== "function") {
      console.error("html2canvas is not available.");
      return;
    }

    const container = createExportContainer();
    const exportTheme = getExportTheme();
    document.body.appendChild(container);

    try {
      await waitForImages(container);
      const canvas = await html2canvas(container, {
        backgroundColor: exportTheme.background,
        scale: 3,
        width: container.offsetWidth,
        height: container.offsetHeight,
      });

      const link = document.createElement("a");
      link.href = canvas.toDataURL("image/png");
      link.download = getExportFilename();
      link.click();
    } catch (error) {
      console.error("Error generating outfit export:", error);
    } finally {
      document.body.removeChild(container);
    }
  }

  function bindPresetInteractions() {
    const presetContainer = document.getElementById("presetContainer");
    if (presetContainer && presetContainer.dataset.bound !== "true") {
      presetContainer.dataset.bound = "true";

      presetContainer.addEventListener("click", (event) => {
        const addButton = event.target.closest(".preset-add-button");
        if (addButton) {
          addPreset();
          return;
        }

        const deleteButton = event.target.closest(".preset-delete-button");
        if (deleteButton) {
          deletePreset(deleteButton.dataset.presetId);
          return;
        }

        const actionButton = event.target.closest(".preset-action");
        if (!actionButton) {
          return;
        }

        const presetId = actionButton.dataset.presetId;
        switch (actionButton.dataset.action) {
          case "save":
            savePreset(presetId);
            break;
          case "load":
            loadPreset(presetId);
            break;
          case "clear":
            clearPreset(presetId);
            break;
          default:
            break;
        }
      });

      presetContainer.addEventListener("focusin", (event) => {
        const nameField = event.target.closest(".editable-preset-name");
        if (!nameField) {
          return;
        }

        nameField.classList.add("is-editing");
      });

      presetContainer.addEventListener("focusout", (event) => {
        const nameField = event.target.closest(".editable-preset-name");
        if (!nameField) {
          return;
        }

        nameField.classList.remove("is-editing");
        updatePresetName(nameField.dataset.presetId, nameField.textContent);
      });

      presetContainer.addEventListener("keydown", (event) => {
        const nameField = event.target.closest(".editable-preset-name");
        if (!nameField) {
          return;
        }

        if (event.key === "Enter") {
          event.preventDefault();
          nameField.blur();
          return;
        }

        if (event.key === "Escape") {
          event.preventDefault();
          nameField.textContent = getPresetById(nameField.dataset.presetId)?.name || "";
          nameField.blur();
        }
      });
    }

    if (presetDrawerToggle && presetDrawerToggle.dataset.bound !== "true") {
      presetDrawerToggle.dataset.bound = "true";
      presetDrawerToggle.addEventListener("click", () => {
        setPresetDrawerOpen(!document.body.classList.contains("simulator-drawer-open"));
      });
    }

    if (presetDrawerBackdrop && presetDrawerBackdrop.dataset.bound !== "true") {
      presetDrawerBackdrop.dataset.bound = "true";
      presetDrawerBackdrop.addEventListener("click", () => {
        setPresetDrawerOpen(false);
      });
    }
  }

  function bindGlobalDismissals() {
    document.addEventListener("pointerdown", (event) => {
      if (!simulatorContextMenu?.classList.contains("is-open")) {
        return;
      }

      if (
        simulatorContextMenu.contains(event.target) ||
        event.target.closest(".equipped-simulator-item")
      ) {
        return;
      }

      closeContextMenu();
    });

    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape") {
        closeContextMenu();
        setPresetDrawerOpen(false);
      }
    });

    window.addEventListener(
      "resize",
      () => {
        syncPresetDrawerState();
        updateSimulatorScale();
        closeContextMenu();
      },
      { passive: true }
    );
  }

  async function init() {
    ensureSimulatorStructure();
    ensureContextMenu();
    presetCollection = loadPresetCollection();
    renderPresetList();
    bindGlobalDismissals();
    bindPresetInteractions();
    await fetchItemCatalog();
    loadOutfitFromStorage();
    syncPresetDrawerState();
    updateSimulatorScale();
    window.requestAnimationFrame(() => {
      updateSimulatorScale();
    });
  }

  const bootstrap = async () => {
    try {
      await init();
    } catch (error) {
      console.error("Simulator initialization failed:", error);
    } finally {
      document.dispatchEvent(new Event("souls:page-ready"));
    }
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", bootstrap, { once: true });
  } else {
    bootstrap();
  }
})();
