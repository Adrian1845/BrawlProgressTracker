import { c as createComponent, r as renderHead, a as renderSlot, b as renderTemplate, e as createAstro, m as maybeRenderHead, f as addAttribute, s as spreadAttributes, g as renderComponent } from '../chunks/astro/server_3mNmDSKn.mjs';
import 'kleur/colors';
import 'clsx';
/* empty css                                 */
export { renderers } from '../renderers.mjs';

const $$Astro$6 = createAstro();
const $$Layout = createComponent(($$result, $$props, $$slots) => {
  const Astro2 = $$result.createAstro($$Astro$6, $$props, $$slots);
  Astro2.self = $$Layout;
  const { title } = Astro2.props;
  return renderTemplate`<html lang="en"> <head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>${title}</title>${renderHead()}</head> <body> ${renderSlot($$result, $$slots["default"])} </body></html>`;
}, "E:/Python/BrawlProgressTracker/frontend/src/layouts/Layout.astro", void 0);

const $$Astro$5 = createAstro();
const $$SearchForm = createComponent(($$result, $$props, $$slots) => {
  const Astro2 = $$result.createAstro($$Astro$5, $$props, $$slots);
  Astro2.self = $$SearchForm;
  const { searchTag, errorMessage } = Astro2.props;
  return renderTemplate`${maybeRenderHead()}<div class="search-card" data-astro-cid-s6z2d6yt> <form id="search-form" onsubmit="return false;" data-astro-cid-s6z2d6yt> <label for="tag" data-astro-cid-s6z2d6yt>ENTER PLAYER TAG</label> <div class="form-group" data-astro-cid-s6z2d6yt> <input type="text" id="tag" placeholder="e.g. QJY2R0V"${addAttribute(searchTag ? `#${searchTag}` : "", "value")} required maxlength="10" data-astro-cid-s6z2d6yt> <button type="button" id="search-btn" data-astro-cid-s6z2d6yt>SEARCH</button> </div> </form> ${errorMessage && renderTemplate`<div class="error-banner" data-astro-cid-s6z2d6yt>${errorMessage}</div>`} </div>  `;
}, "E:/Python/BrawlProgressTracker/frontend/src/components/SearchForm.astro", void 0);

var __freeze$1 = Object.freeze;
var __defProp$1 = Object.defineProperty;
var __template$1 = (cooked, raw) => __freeze$1(__defProp$1(cooked, "raw", { value: __freeze$1(cooked.slice()) }));
var _a$1;
const $$Astro$4 = createAstro();
const $$AssetImage = createComponent(($$result, $$props, $$slots) => {
  const Astro2 = $$result.createAstro($$Astro$4, $$props, $$slots);
  Astro2.self = $$AssetImage;
  const {
    src,
    alt,
    fallbackSrc,
    hideOnError = true,
    ...imgProps
  } = Astro2.props;
  return renderTemplate(_a$1 || (_a$1 = __template$1(["", "<img", "", "", ' data-asset-image="true"', "", `> <script>
  const bindAssetImageFallbacks = () => {
    const images = document.querySelectorAll('img[data-asset-image="true"]:not([data-asset-image-bound="true"])');

    images.forEach((image) => {
      image.dataset.assetImageBound = 'true';

      const handleError = () => {
        if (image.dataset.assetFallbackApplied === 'true') {
          image.style.display = 'none';
          return;
        }

        const fallbackSrc = image.dataset.fallbackSrc;
        if (fallbackSrc && image.getAttribute('src') !== fallbackSrc) {
          image.dataset.assetFallbackApplied = 'true';
          image.src = fallbackSrc;
          return;
        }

        if (image.dataset.hideOnError === 'true') {
          image.style.display = 'none';
        }
      };

      image.addEventListener('error', handleError);

      if (image.complete && image.naturalWidth === 0) {
        handleError();
      }
    });
  };

  bindAssetImageFallbacks();
<\/script>`])), maybeRenderHead(), spreadAttributes(imgProps), addAttribute(src, "src"), addAttribute(alt, "alt"), addAttribute(fallbackSrc, "data-fallback-src"), addAttribute(hideOnError ? "true" : "false", "data-hide-on-error"));
}, "E:/Python/BrawlProgressTracker/frontend/src/components/AssetImage.astro", void 0);

var __freeze = Object.freeze;
var __defProp = Object.defineProperty;
var __template = (cooked, raw) => __freeze(__defProp(cooked, "raw", { value: __freeze(raw || cooked.slice()) }));
var _a;
const $$Astro$3 = createAstro();
const $$BrawlerCatalog = createComponent(($$result, $$props, $$slots) => {
  const Astro2 = $$result.createAstro($$Astro$3, $$props, $$slots);
  Astro2.self = $$BrawlerCatalog;
  const { brawlers, totalCount } = Astro2.props;
  return renderTemplate(_a || (_a = __template(["", '<section class="brawlers-section" data-astro-cid-w44v4w7i> <div class="section-title-wrapper" data-astro-cid-w44v4w7i> <div class="section-title-copy" data-astro-cid-w44v4w7i> <h3 data-astro-cid-w44v4w7i>\u{1F465} Brawlers Catalog</h3> <span class="count-tag" id="brawler-count" data-astro-cid-w44v4w7i>', ' Unlocked</span> </div> <div class="catalog-controls" aria-label="Brawler catalog filters" data-astro-cid-w44v4w7i> <label class="filter-label" for="brawler-search" data-astro-cid-w44v4w7i>Search</label> <input id="brawler-search" class="catalog-input" type="search" placeholder="Search brawlers" autocomplete="off" data-astro-cid-w44v4w7i> <label class="filter-label" for="brawler-sort" data-astro-cid-w44v4w7i>Sort by</label> <select id="brawler-sort" class="catalog-select" aria-label="Sort brawlers" data-astro-cid-w44v4w7i> <option value="trophies" data-astro-cid-w44v4w7i>Trophies</option> <option value="power" data-astro-cid-w44v4w7i>Power</option> <option value="rank" data-astro-cid-w44v4w7i>Rank</option> </select> </div> </div> <p class="catalog-empty" id="brawler-empty" hidden data-astro-cid-w44v4w7i>No brawlers match your search.</p> <div class="brawlers-grid" id="brawlers-grid" data-astro-cid-w44v4w7i> ', " </div> </section> <script>\n  const searchInput = document.getElementById('brawler-search');\n  const sortSelect = document.getElementById('brawler-sort');\n  const grid = document.getElementById('brawlers-grid');\n  const countTag = document.getElementById('brawler-count');\n  const emptyState = document.getElementById('brawler-empty');\n\n  if (searchInput && sortSelect && grid && countTag && emptyState) {\n    const cards = Array.from(grid.querySelectorAll('[data-brawler-card]'));\n\n    const sortCardValues = {\n      trophies: (card) => Number(card.dataset.trophies ?? 0),\n      power: (card) => Number(card.dataset.power ?? 0),\n      rank: (card) => Number(card.dataset.rank ?? 0),\n    };\n\n    const renderCards = () => {\n      const query = searchInput.value.trim().toLowerCase();\n      const sortBy = sortSelect.value;\n\n      const visibleCards = cards.filter((card) => {\n        const name = card.dataset.name ?? '';\n        const matchesQuery = !query || name.includes(query);\n        card.hidden = !matchesQuery;\n        card.toggleAttribute('aria-hidden', !matchesQuery);\n        card.classList.toggle('is-hidden', !matchesQuery);\n        return matchesQuery;\n      });\n\n      visibleCards.sort((a, b) => {\n        const aValue = sortCardValues[sortBy](a);\n        const bValue = sortCardValues[sortBy](b);\n        if (bValue !== aValue) {\n          return bValue - aValue;\n        }\n\n        return Number(a.dataset.originalIndex ?? 0) - Number(b.dataset.originalIndex ?? 0);\n      });\n\n      visibleCards.forEach((card) => grid.appendChild(card));\n      countTag.textContent =\n        visibleCards.length === cards.length\n          ? `${cards.length} Unlocked`\n          : `${visibleCards.length} / ${cards.length} Shown`;\n      emptyState.hidden = visibleCards.length > 0;\n    };\n\n    searchInput.addEventListener('input', renderCards);\n    sortSelect.addEventListener('change', renderCards);\n    renderCards();\n  }\n<\/script> "], ["", '<section class="brawlers-section" data-astro-cid-w44v4w7i> <div class="section-title-wrapper" data-astro-cid-w44v4w7i> <div class="section-title-copy" data-astro-cid-w44v4w7i> <h3 data-astro-cid-w44v4w7i>\u{1F465} Brawlers Catalog</h3> <span class="count-tag" id="brawler-count" data-astro-cid-w44v4w7i>', ' Unlocked</span> </div> <div class="catalog-controls" aria-label="Brawler catalog filters" data-astro-cid-w44v4w7i> <label class="filter-label" for="brawler-search" data-astro-cid-w44v4w7i>Search</label> <input id="brawler-search" class="catalog-input" type="search" placeholder="Search brawlers" autocomplete="off" data-astro-cid-w44v4w7i> <label class="filter-label" for="brawler-sort" data-astro-cid-w44v4w7i>Sort by</label> <select id="brawler-sort" class="catalog-select" aria-label="Sort brawlers" data-astro-cid-w44v4w7i> <option value="trophies" data-astro-cid-w44v4w7i>Trophies</option> <option value="power" data-astro-cid-w44v4w7i>Power</option> <option value="rank" data-astro-cid-w44v4w7i>Rank</option> </select> </div> </div> <p class="catalog-empty" id="brawler-empty" hidden data-astro-cid-w44v4w7i>No brawlers match your search.</p> <div class="brawlers-grid" id="brawlers-grid" data-astro-cid-w44v4w7i> ', " </div> </section> <script>\n  const searchInput = document.getElementById('brawler-search');\n  const sortSelect = document.getElementById('brawler-sort');\n  const grid = document.getElementById('brawlers-grid');\n  const countTag = document.getElementById('brawler-count');\n  const emptyState = document.getElementById('brawler-empty');\n\n  if (searchInput && sortSelect && grid && countTag && emptyState) {\n    const cards = Array.from(grid.querySelectorAll('[data-brawler-card]'));\n\n    const sortCardValues = {\n      trophies: (card) => Number(card.dataset.trophies ?? 0),\n      power: (card) => Number(card.dataset.power ?? 0),\n      rank: (card) => Number(card.dataset.rank ?? 0),\n    };\n\n    const renderCards = () => {\n      const query = searchInput.value.trim().toLowerCase();\n      const sortBy = sortSelect.value;\n\n      const visibleCards = cards.filter((card) => {\n        const name = card.dataset.name ?? '';\n        const matchesQuery = !query || name.includes(query);\n        card.hidden = !matchesQuery;\n        card.toggleAttribute('aria-hidden', !matchesQuery);\n        card.classList.toggle('is-hidden', !matchesQuery);\n        return matchesQuery;\n      });\n\n      visibleCards.sort((a, b) => {\n        const aValue = sortCardValues[sortBy](a);\n        const bValue = sortCardValues[sortBy](b);\n        if (bValue !== aValue) {\n          return bValue - aValue;\n        }\n\n        return Number(a.dataset.originalIndex ?? 0) - Number(b.dataset.originalIndex ?? 0);\n      });\n\n      visibleCards.forEach((card) => grid.appendChild(card));\n      countTag.textContent =\n        visibleCards.length === cards.length\n          ? \\`\\${cards.length} Unlocked\\`\n          : \\`\\${visibleCards.length} / \\${cards.length} Shown\\`;\n      emptyState.hidden = visibleCards.length > 0;\n    };\n\n    searchInput.addEventListener('input', renderCards);\n    sortSelect.addEventListener('change', renderCards);\n    renderCards();\n  }\n<\/script> "])), maybeRenderHead(), totalCount, brawlers.map((brawler, index) => renderTemplate`<div class="brawler-card" data-brawler-card${addAttribute(brawler.name.toLowerCase(), "data-name")}${addAttribute(brawler.power, "data-power")}${addAttribute(brawler.trophies, "data-trophies")}${addAttribute(brawler.rank, "data-rank")}${addAttribute(index, "data-original-index")} data-astro-cid-w44v4w7i> <div class="brawler-header" data-astro-cid-w44v4w7i> ${renderComponent($$result, "AssetImage", $$AssetImage, { "src": `/assets/brawlers/${brawler.id}.png`, "alt": brawler.name, "class": "brawler-avatar", "loading": "lazy", "fallbackSrc": `https://cdn.brawlify.com/brawlers/borderless/${brawler.id}.png`, "data-astro-cid-w44v4w7i": true })} <div class="brawler-title-group" data-astro-cid-w44v4w7i> <span class="brawler-name" data-astro-cid-w44v4w7i>${brawler.name}</span> <span class="brawler-power" data-astro-cid-w44v4w7i>Power ${brawler.power}</span> </div> <span class="brawler-rank" data-astro-cid-w44v4w7i>R ${brawler.rank}</span> </div> <div class="brawler-stats" data-astro-cid-w44v4w7i> <div class="stat" data-astro-cid-w44v4w7i> ${renderComponent($$result, "AssetImage", $$AssetImage, { "src": "/assets/UI/trophy.png", "class": "asset-icon-mini", "alt": "Trophies", "data-astro-cid-w44v4w7i": true })} <span class="brawler-trophies" data-astro-cid-w44v4w7i>${brawler.trophies}</span> </div> </div> </div>`));
}, "E:/Python/BrawlProgressTracker/frontend/src/components/BrawlerCatalog.astro", void 0);

const $$Astro$2 = createAstro();
const $$ProgressMetricGroupTracker = createComponent(($$result, $$props, $$slots) => {
  const Astro2 = $$result.createAstro($$Astro$2, $$props, $$slots);
  Astro2.self = $$ProgressMetricGroupTracker;
  const {
    title,
    metric,
    countLabel,
    goldLabel,
    ppLabel
  } = Astro2.props;
  const formatValue = (value) => value.toLocaleString();
  return renderTemplate`${maybeRenderHead()}<section class="group-card" data-astro-cid-7dnk25if> <h3 data-astro-cid-7dnk25if>${title}</h3> <div class="group-stack" data-astro-cid-7dnk25if> ${metric.count && renderTemplate`<div class="group-row group-row-count" data-astro-cid-7dnk25if> <div class="row-head" data-astro-cid-7dnk25if> <span class="row-label" data-astro-cid-7dnk25if>${countLabel ?? "Count"}</span> <span class="row-value" data-astro-cid-7dnk25if>${formatValue(metric.count.current)} / ${formatValue(metric.count.total_needed_for_max)}</span> </div> <div class="row-meta" data-astro-cid-7dnk25if> <span class="row-subtle" data-astro-cid-7dnk25if>${formatValue(metric.count.leftover_needed)} left</span> <span class="row-subtle" data-astro-cid-7dnk25if>${metric.count.percentage_completed}% complete</span> </div> <div class="progress-bar-container large" data-astro-cid-7dnk25if> <div class="progress-bar count-bar"${addAttribute(`width: ${metric.count.percentage_completed}%`, "style")} data-astro-cid-7dnk25if></div> </div> </div>`} ${metric.gold && renderTemplate`<div class="group-row" data-astro-cid-7dnk25if> <div class="row-head" data-astro-cid-7dnk25if> <span class="row-label" data-astro-cid-7dnk25if>${goldLabel ?? "Gold"}</span> <span class="row-value" data-astro-cid-7dnk25if> ${formatValue(metric.gold.current)} ${renderComponent($$result, "AssetImage", $$AssetImage, { "src": "/assets/UI/gold.png", "class": "asset-icon-mini", "alt": "Gold", "data-astro-cid-7dnk25if": true })} </span> </div> <div class="row-meta" data-astro-cid-7dnk25if> <span class="row-subtle" data-astro-cid-7dnk25if> ${formatValue(metric.gold.leftover_needed)} left
${renderComponent($$result, "AssetImage", $$AssetImage, { "src": "/assets/UI/gold.png", "class": "asset-icon-mini subtle-icon", "alt": "Gold needed", "data-astro-cid-7dnk25if": true })} </span> <span class="row-subtle" data-astro-cid-7dnk25if>${metric.gold.percentage_completed}% complete</span> </div> <div class="progress-bar-container large" data-astro-cid-7dnk25if> <div class="progress-bar gold-bar"${addAttribute(`width: ${metric.gold.percentage_completed}%`, "style")} data-astro-cid-7dnk25if></div> </div> </div>`} ${metric.pp && renderTemplate`<div class="group-row" data-astro-cid-7dnk25if> <div class="row-head" data-astro-cid-7dnk25if> <span class="row-label" data-astro-cid-7dnk25if>${ppLabel ?? "Power Points"}</span> <span class="row-value" data-astro-cid-7dnk25if> ${formatValue(metric.pp.current)} ${renderComponent($$result, "AssetImage", $$AssetImage, { "src": "/assets/UI/power-point.png", "class": "asset-icon-mini", "alt": "Power Points", "data-astro-cid-7dnk25if": true })} </span> </div> <div class="row-meta" data-astro-cid-7dnk25if> <span class="row-subtle" data-astro-cid-7dnk25if> ${formatValue(metric.pp.leftover_needed)} left
${renderComponent($$result, "AssetImage", $$AssetImage, { "src": "/assets/UI/power-point.png", "class": "asset-icon-mini subtle-icon", "alt": "Power Points needed", "data-astro-cid-7dnk25if": true })} </span> <span class="row-subtle" data-astro-cid-7dnk25if>${metric.pp.percentage_completed}% complete</span> </div> <div class="progress-bar-container large" data-astro-cid-7dnk25if> <div class="progress-bar pp-bar"${addAttribute(`width: ${metric.pp.percentage_completed}%`, "style")} data-astro-cid-7dnk25if></div> </div> </div>`} </div> </section> `;
}, "E:/Python/BrawlProgressTracker/frontend/src/components/ProgressMetricGroupTracker.astro", void 0);

const $$Astro$1 = createAstro();
const $$PlayerResults = createComponent(($$result, $$props, $$slots) => {
  const Astro2 = $$result.createAstro($$Astro$1, $$props, $$slots);
  Astro2.self = $$PlayerResults;
  const { data } = Astro2.props;
  if (!data || !data.profile) {
    return null;
  }
  const { profile, metrics_v2 } = data;
  const brawlersList = profile.brawlers || [];
  const sortedBrawlers = [...brawlersList].sort((a, b) => b.trophies - a.trophies);
  const profileIconSrc = profile.icon?.id ? `/assets/profile/icons/${profile.icon.id}.png` : "/assets/profile/icons/Unknown.png";
  const rankedTierId = typeof profile.rankedRank === "number" ? 58e6 + profile.rankedRank - 1 : null;
  const rankedBadgeSrc = rankedTierId !== null ? `/assets/profile/ranked/tiered/${rankedTierId}.png` : "/assets/profile/ranked/regular/Pro.png";
  const rankedBadgeFallback = profile.rankedRankName?.split(" ")[0] ? `/assets/profile/ranked/regular/${profile.rankedRankName.split(" ")[0]}.png` : "/assets/profile/ranked/regular/Pro.png";
  return renderTemplate`${maybeRenderHead()}<div class="results-container" data-astro-cid-r7vne55d> <header class="profile-header"${addAttribute(`border-color: ${profile.nameColor ? profile.nameColor.replace("0xff", "#") : "#2a2e37"}`, "style")} data-astro-cid-r7vne55d> <div class="avatar-stub" data-astro-cid-r7vne55d> ${renderComponent($$result, "AssetImage", $$AssetImage, { "src": profileIconSrc, "fallbackSrc": "/assets/profile/icons/Unknown.png", "class": "profile-icon", "alt": `${profile.name} profile icon`, "loading": "eager", "data-astro-cid-r7vne55d": true })} </div> <div class="profile-title" data-astro-cid-r7vne55d> <h2${addAttribute(`color: ${profile.nameColor ? profile.nameColor.replace("0xff", "#") : "#fff"}`, "style")} data-astro-cid-r7vne55d> ${profile.name} </h2> <div class="sub-badges" data-astro-cid-r7vne55d> <span class="player-tag" data-astro-cid-r7vne55d>${profile.tag}</span> ${profile.club?.name && renderTemplate`<span class="club-badge" data-astro-cid-r7vne55d>🦎 ${profile.club.name}</span>`} </div> </div> <div class="rank-badge" data-astro-cid-r7vne55d> <span class="lbl" data-astro-cid-r7vne55d>COMPETITIVE</span> <div class="rank-badge-row" data-astro-cid-r7vne55d> ${renderComponent($$result, "AssetImage", $$AssetImage, { "src": rankedBadgeSrc, "fallbackSrc": rankedBadgeFallback, "class": "rank-icon", "alt": `${profile.rankedRankName ?? "Rank"} badge`, "hideOnError": false, "data-astro-cid-r7vne55d": true })} <div class="rank-badge-copy" data-astro-cid-r7vne55d> <span class="val ranked-text" data-astro-cid-r7vne55d>${profile.rankedRankName ?? "Unranked"}</span> <span class="elo" data-astro-cid-r7vne55d>${profile.rankedElo?.toLocaleString() ?? "0"} ELO</span> </div> </div> </div> </header> <!-- PROGRESSION --> <section class="progression-grid" data-astro-cid-r7vne55d> ${renderComponent($$result, "ProgressMetricGroupTracker", $$ProgressMetricGroupTracker, { "title": "Max Level", "metric": metrics_v2.max_level, "goldLabel": "Gold to Max", "ppLabel": "Power Points to Max", "data-astro-cid-r7vne55d": true })} ${renderComponent($$result, "ProgressMetricGroupTracker", $$ProgressMetricGroupTracker, { "title": "Power 11", "metric": metrics_v2.power_11, "countLabel": "Power 11 Brawlers", "goldLabel": "Gold Invested", "ppLabel": "Power Points Invested", "data-astro-cid-r7vne55d": true })} ${renderComponent($$result, "ProgressMetricGroupTracker", $$ProgressMetricGroupTracker, { "title": "Gadgets", "metric": metrics_v2.gadgets, "countLabel": "Gadgets Owned", "goldLabel": "Gold Invested", "data-astro-cid-r7vne55d": true })} ${renderComponent($$result, "ProgressMetricGroupTracker", $$ProgressMetricGroupTracker, { "title": "Star Powers", "metric": metrics_v2.star_powers, "countLabel": "Star Powers Owned", "goldLabel": "Gold Invested", "data-astro-cid-r7vne55d": true })} ${renderComponent($$result, "ProgressMetricGroupTracker", $$ProgressMetricGroupTracker, { "title": "Gears", "metric": metrics_v2.gears, "countLabel": "Gears Owned", "goldLabel": "Gold Invested", "data-astro-cid-r7vne55d": true })} ${renderComponent($$result, "ProgressMetricGroupTracker", $$ProgressMetricGroupTracker, { "title": "Buffies", "metric": metrics_v2.buffies, "countLabel": "Buffies Owned", "goldLabel": "Gold Invested", "ppLabel": "Power Points Invested", "data-astro-cid-r7vne55d": true })} ${renderComponent($$result, "ProgressMetricGroupTracker", $$ProgressMetricGroupTracker, { "title": "Hypercharges", "metric": metrics_v2.hypercharges, "countLabel": "Hypercharges Owned", "goldLabel": "Gold Invested", "data-astro-cid-r7vne55d": true })} </section> <!-- GLOBAL STATS --> <section class="stats-grid" data-astro-cid-r7vne55d> <div class="stat-card" data-astro-cid-r7vne55d> ${renderComponent($$result, "AssetImage", $$AssetImage, { "src": "/assets/UI/trophy.png", "class": "asset-icon-card", "alt": "Trophies", "data-astro-cid-r7vne55d": true })} <div class="stat-info" data-astro-cid-r7vne55d> <span class="stat-label" data-astro-cid-r7vne55d>Current Trophies</span> <span class="stat-value" data-astro-cid-r7vne55d>${profile.trophies.toLocaleString()}</span> </div> </div> <div class="stat-card" data-astro-cid-r7vne55d> <span class="stat-icon" data-astro-cid-r7vne55d>🔥</span> <div class="stat-info" data-astro-cid-r7vne55d> <span class="stat-label" data-astro-cid-r7vne55d>Trophy Record</span> <span class="stat-value" data-astro-cid-r7vne55d>${profile.highestTrophies.toLocaleString()}</span> </div> </div> <div class="stat-card" data-astro-cid-r7vne55d> <span class="stat-icon" data-astro-cid-r7vne55d>⚔️</span> <div class="stat-info" data-astro-cid-r7vne55d> <span class="stat-label" data-astro-cid-r7vne55d>3vs3 Victories</span> <span class="stat-value" data-astro-cid-r7vne55d>${profile["3vs3Victories"].toLocaleString()}</span> </div> </div> </section> ${renderComponent($$result, "BrawlerCatalog", $$BrawlerCatalog, { "brawlers": sortedBrawlers, "totalCount": brawlersList.length, "data-astro-cid-r7vne55d": true })} </div> `;
}, "E:/Python/BrawlProgressTracker/frontend/src/components/PlayerResults.astro", void 0);

const fallbackApiBaseUrl = "http://127.0.0.1:8000";
const API_BASE_URL = (fallbackApiBaseUrl).replace(/\/$/, "");

const $$Astro = createAstro();
const $$Index = createComponent(async ($$result, $$props, $$slots) => {
  const Astro2 = $$result.createAstro($$Astro, $$props, $$slots);
  Astro2.self = $$Index;
  let playerData = null;
  let errorMessage = "";
  const rawTag = Astro2.url.searchParams.get("tag")?.trim() || "";
  const searchTag = rawTag.startsWith("#") ? rawTag.slice(1) : rawTag;
  if (searchTag) {
    try {
      const response = await fetch(`${API_BASE_URL}/api/player/${searchTag}`);
      if (!response.ok) {
        errorMessage = response.status === 404 ? `Player tag #${searchTag} not found.` : "Failed to communicate with the backend tracker engine.";
      } else {
        playerData = await response.json();
      }
    } catch (error) {
      errorMessage = "An unexpected connection error occurred.";
      console.error(error);
    }
  }
  return renderTemplate`${renderComponent($$result, "Layout", $$Layout, { "title": "Brawl Progress Tracker", "data-astro-cid-j7pv25f6": true }, { "default": async ($$result2) => renderTemplate` ${maybeRenderHead()}<main class="page-shell" data-astro-cid-j7pv25f6> <header class="page-hero" data-astro-cid-j7pv25f6> <h1 data-astro-cid-j7pv25f6>Brawl Tracker</h1> <p data-astro-cid-j7pv25f6>Progression Analyst</p> </header> ${renderComponent($$result2, "SearchForm", $$SearchForm, { "searchTag": searchTag, "errorMessage": errorMessage, "data-astro-cid-j7pv25f6": true })} ${playerData && renderTemplate`${renderComponent($$result2, "PlayerResults", $$PlayerResults, { "data": playerData, "data-astro-cid-j7pv25f6": true })}`} </main> ` })} `;
}, "E:/Python/BrawlProgressTracker/frontend/src/pages/index.astro", void 0);

const $$file = "E:/Python/BrawlProgressTracker/frontend/src/pages/index.astro";
const $$url = "";

const _page = /*#__PURE__*/Object.freeze(/*#__PURE__*/Object.defineProperty({
  __proto__: null,
  default: $$Index,
  file: $$file,
  url: $$url
}, Symbol.toStringTag, { value: 'Module' }));

const page = () => _page;

export { page };
