const INDEX_ITEMS = [
  {
    img: "resources/grid-images/elden-ring-grid.webp",
    placeholder: "resources/grid-images/elden-ring-grid_placeholder.webp",
    link: "eldenring",
    label: "Elden Ring",
  },
  {
    img: "resources/grid-images/bloodborne-grid.webp",
    placeholder: "resources/grid-images/bloodborne-grid_placeholder.webp",
    link: "bloodborne",
    label: "Bloodborne",
  },
  {
    img: "resources/grid-images/dark-souls-grid.webp",
    placeholder: "resources/grid-images/dark-souls-grid_placeholder.webp",
    link: "ds1",
    label: "Dark Souls",
  },
  {
    img: "resources/grid-images/dark-souls-2-grid.webp",
    placeholder: "resources/grid-images/dark-souls-2-grid_placeholder.webp",
    link: "ds2",
    label: "Dark Souls II",
  },
  {
    img: "resources/grid-images/dark-souls-3-grid.webp",
    placeholder: "resources/grid-images/dark-souls-3-grid_placeholder.webp",
    link: "ds3",
    label: "Dark Souls III",
  },
  {
    img: "resources/grid-images/demons-souls-grid.webp",
    placeholder: "resources/grid-images/demons-souls-grid_placeholder.webp",
    link: "demonssouls",
    label: "Demon's Souls",
  },
];

const INDEX_GRID_GAP = 18;

function preloadImage(src) {
  return new Promise((resolve) => {
    const image = new Image();
    image.decoding = "async";
    image.onload = () => resolve(image);
    image.onerror = () => resolve(null);
    image.src = src;
  });
}

function updateIndexGridMetrics() {
  const hero = document.querySelector(".content-hero") || document.querySelector(".hero");
  const footer = document.querySelector(".copyright");
  const isMobile = window.matchMedia("(max-width: 900px)").matches;
  const columns = isMobile ? 2 : 3;
  const rows = isMobile ? 3 : 2;
  const horizontalPadding = isMobile ? 16 : 48;
  const verticalPadding = isMobile ? 16 : 28;
  const availableHeight =
    window.innerHeight - (hero?.offsetHeight || 0) - (footer?.offsetHeight || 0) - verticalPadding;
  const cardHeight = Math.max((availableHeight - INDEX_GRID_GAP * (rows - 1)) / rows, 120);
  const cardWidth = cardHeight * (2 / 3);
  const fittedGridWidth = cardWidth * columns + INDEX_GRID_GAP * (columns - 1);
  const maxGridWidth = Math.max(260, Math.min(window.innerWidth - horizontalPadding, fittedGridWidth));

  document.documentElement.style.setProperty("--index-columns", columns.toString());
  document.documentElement.style.setProperty("--index-rows", rows.toString());
  document.documentElement.style.setProperty("--grid-gap", `${INDEX_GRID_GAP}px`);
  document.documentElement.style.setProperty("--page-width", `${Math.floor(maxGridWidth)}px`);
}

function startAnimatedPreviewSwap(animatedImages) {
  const run = () => {
    animatedImages.forEach(({ liveSrc, imageElement }) => {
      preloadImage(liveSrc).then((animatedImg) => {
        if (!animatedImg || !imageElement.isConnected) {
          return;
        }

        animatedImg.className = imageElement.className;
        animatedImg.alt = imageElement.alt;
        animatedImg.decoding = "async";
        animatedImg.loading = "eager";
        imageElement.replaceWith(animatedImg);
      });
    });
  };

  window.setTimeout(run, 120);
}

async function loadImages() {
  const itemGrid = document.getElementById("itemGrid");
  itemGrid.innerHTML = "";

  const animatedImages = [];
  const placeholderLoads = INDEX_ITEMS.map((item) => preloadImage(item.placeholder));
  await Promise.all(placeholderLoads);

  INDEX_ITEMS.forEach((item) => {
    const itemCard = document.createElement("div");
    itemCard.className = "index-card";

    const linkElement = document.createElement("a");
    linkElement.className = "index-card-link";
    linkElement.href = item.link;
    linkElement.setAttribute("aria-label", item.label);

    const mediaElement = document.createElement("div");
    mediaElement.className = "index-media";

    const imgElement = document.createElement("img");
    imgElement.className = "index-image";
    imgElement.decoding = "async";
    imgElement.loading = "eager";
    imgElement.src = item.placeholder;
    imgElement.alt = item.label;

    mediaElement.appendChild(imgElement);
    linkElement.appendChild(mediaElement);
    itemCard.appendChild(linkElement);
    itemGrid.appendChild(itemCard);

    animatedImages.push({ liveSrc: item.img, imageElement: imgElement });
  });

  updateIndexGridMetrics();
  await new Promise((resolve) => {
    window.requestAnimationFrame(() => {
      window.requestAnimationFrame(resolve);
    });
  });
  document.dispatchEvent(new Event("souls:page-ready"));
  startAnimatedPreviewSwap(animatedImages);
}

document.addEventListener("DOMContentLoaded", async () => {
  updateIndexGridMetrics();
  await Promise.race([
    loadImages(),
    new Promise((resolve) => {
      window.setTimeout(resolve, 2200);
    }),
  ]);
});

window.addEventListener(
  "resize",
  () => {
    updateIndexGridMetrics();
  },
  { passive: true }
);
