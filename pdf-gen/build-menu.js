// Soho menu PDF generator
// Reads soho_items.json + translations.json, normalizes the (messy) structure,
// builds an elegant RTL Arabic HTML menu, and renders it to PDF with puppeteer-core.

const fs = require("fs");
const path = require("path");

const ROOT = path.resolve(__dirname, "..");

const items = JSON.parse(fs.readFileSync(path.join(ROOT, "soho_items.json"), "utf8"));
const tr = JSON.parse(fs.readFileSync(path.join(ROOT, "translations.json"), "utf8"));

// ---- Restaurant contact ----
const PHONE = "01065770011";

// ---- Category metadata: Arabic key -> {en, order, note} ----
const CATS = {
  "المقبلات":          { en: "Appetizers", order: 1 },
  "الشوربة":           { en: "Soups", order: 2 },
  "السلطات":           { en: "Salads", order: 3 },
  "الساندوتشات":       { en: "Sandwiches & Burgers", order: 4 },
  "ركن الباستا":       { en: "Pasta", order: 5 },
  "الاطباق الرئيسية":  { en: "Main Dishes", order: 6 },
  "البيتزا":           { en: "Pizza", order: 7 },
  "وجبات الاطفال":     { en: "Kids Meals", order: 8 },
  "اكسترا":            { en: "Sides & Extras", order: 9 },
  "الصوصات":           { en: "Sauces", order: 10 },
  "الحلويات":          { en: "Desserts", order: 11 },
  "المشروبات الباردة": { en: "Cold Drinks", order: 12 },
};
const isCat = (k) => Object.prototype.hasOwnProperty.call(CATS, k.trim());

// ---- Normalize the messy JSON ----
// Structure: category keys map to item arrays. Stray "description" keys sit
// BETWEEN items and describe the previously-emitted item; their array holds
// the NEXT item(s).
const data = {}; // catKey -> [ {name, name_en, price, desc, desc_en} ]
let curCat = null;
let lastItem = null;

for (const [rawKey, arr] of Object.entries(items)) {
  const key = rawKey.trim();
  if (isCat(key)) {
    curCat = key;
    if (!data[curCat]) data[curCat] = [];
    for (const it of arr) {
      const obj = mkItem(it);
      data[curCat].push(obj);
      lastItem = obj;
    }
  } else {
    // description key for the previous item
    if (lastItem && !lastItem.desc) {
      lastItem.desc = rawKey.trim();
      lastItem.desc_en = tr[rawKey] || tr[rawKey.trim()] || "";
    }
    if (curCat) {
      for (const it of arr) {
        const obj = mkItem(it);
        data[curCat].push(obj);
        lastItem = obj;
      }
    }
  }
}

function mkItem(it) {
  const name = (it.name || "").trim();
  return {
    name,
    name_en: it.name_en || tr[it.name] || tr[name] || "",
    price: it.price,
    desc: it.description ? it.description.trim() : "",
    desc_en: it.description ? tr[it.description] || "" : "",
  };
}

// ---- Build ordered category list ----
const ordered = Object.keys(data)
  .filter((k) => data[k] && data[k].length)
  .sort((a, b) => (CATS[a].order || 99) - (CATS[b].order || 99));

// ---- Embed fonts as base64 ----
const FONTS = "C:\\Windows\\Fonts\\";
const b64 = (f) => fs.readFileSync(FONTS + f).toString("base64");
const fontFace = (family, file, weight = 400, style = "normal") =>
  `@font-face{font-family:'${family}';font-style:${style};font-weight:${weight};src:url(data:font/ttf;base64,${b64(file)}) format('truetype');}`;

const fontCss = [
  fontFace("Majalla", "majalla.ttf", 400),
  fontFace("Majalla", "majallab.ttf", 700),
  fontFace("Aldhabi", "aldhabi.ttf", 700),
  fontFace("Segoe UI", "segoeui.ttf", 400),
  fontFace("Segoe UI", "segoeuib.ttf", 700),
].join("\n");

// ---- Helpers ----
const esc = (s) =>
  String(s == null ? "" : s)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");

function itemHtml(it) {
  const en = it.name_en ? `<span class="i-en">${esc(it.name_en)}</span>` : "";
  const desc = it.desc ? `<div class="i-desc">${esc(it.desc)}</div>` : "";
  const price =
    it.price != null
      ? `<span class="i-price">${it.price}</span>`
      : `<span class="i-price">—</span>`;
  return `<div class="item">
    <div class="i-head">
      <div class="i-name">${esc(it.name)} ${en}</div>
      <span class="i-dots"></span>
      ${price}
    </div>
    ${desc}
  </div>`;
}

function categoryHtml(catKey) {
  const meta = CATS[catKey];
  const rows = data[catKey].map(itemHtml).join("\n");
  return `<section class="cat">
    <div class="cat-head">
      <div class="cat-ar">${esc(catKey)}</div>
      <div class="cat-en">${esc(meta.en)}</div>
      <div class="cat-rule"><span></span></div>
    </div>
    <div class="items">${rows}</div>
  </section>`;
}

const sections = ordered.map(categoryHtml).join("\n");

const html = `<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8">
<style>
${fontCss}
:root{
  --bg:#15110d;        /* deep espresso */
  --bg2:#1d1813;
  --panel:#211b15;
  --gold:#c9a24a;      /* warm gold */
  --gold-2:#e7c879;
  --cream:#f3ead7;
  --muted:#a99c84;
  --line:#3a3026;
}
*{box-sizing:border-box;margin:0;padding:0;}
html{background:var(--bg);}
body{background:transparent;color:var(--cream);
  font-family:'Majalla','Segoe UI',sans-serif;
  -webkit-print-color-adjust:exact;print-color-adjust:exact;}

/* Full bleed: margin:0 so the dark background reaches every edge AND so the
   fixed frame/background below cover the whole sheet (Chrome clips fixed
   elements to the @page content box, so any page margin would create white
   strips). Per-page top/bottom spacing is instead reserved by the repeating
   <thead>/<tfoot> spacer rows of the content table (see .doc). */
@page{size:A4;margin:0;}

/* Dark background + decorative frame, repeated on EVERY page via position:fixed
   (fixed elements re-paint on each printed sheet). */
.bg{position:fixed;inset:0;
  background:radial-gradient(130% 72% at 50% 0%,#211912 0%,var(--bg) 60%);z-index:-2;}
.frame{position:fixed;inset:6mm;border:1px solid rgba(201,162,74,.50);z-index:-1;}
.frame::before{content:"";position:absolute;inset:1.8mm;
  border:1px solid rgba(201,162,74,.22);}

/* Content table: thead/tfoot spacers repeat on every printed page, reserving
   uniform top/bottom breathing room so category titles never jam the edge or
   split across a page break. */
table.doc{width:100%;border-collapse:collapse;}
table.doc .pad-top{height:17mm;}
table.doc .pad-bot{height:15mm;vertical-align:bottom;}
.foot{padding-bottom:6mm;text-align:center;font-family:'Segoe UI',sans-serif;
  direction:ltr;font-size:12px;font-weight:700;letter-spacing:.22em;text-indent:.22em;
  color:var(--gold);opacity:.9;}
.foot .ic{font-weight:400;}
table.doc .body-cell{padding:0 13mm;vertical-align:top;}

/* ---------- COVER ----------
   Height is kept just UNDER a full page (not exactly 297mm): a block that
   exactly fills the page AND forces a break makes many viewers emit a trailing
   blank page. Slightly-under + break-after gives one clean break, no blank. */
.cover{display:flex;flex-direction:column;align-items:center;justify-content:center;
  text-align:center;height:293mm;break-after:page;}
.brand{font-family:'Segoe UI',sans-serif;font-weight:700;letter-spacing:.5em;
  direction:ltr;font-size:90px;color:var(--gold-2);text-indent:.5em;
  text-shadow:0 2px 18px rgba(201,162,74,.25);line-height:1;}
.brand-word{font-family:'Segoe UI',sans-serif;font-weight:400;letter-spacing:.62em;
  direction:ltr;font-size:30px;color:var(--cream);text-indent:.62em;margin-top:5mm;}
.brand-sub{font-family:'Aldhabi','Majalla',serif;font-size:40px;color:var(--cream);
  margin-top:7mm;}
.cover .est{font-family:'Segoe UI',sans-serif;letter-spacing:.45em;font-size:13px;
  direction:ltr;color:var(--muted);margin-top:8mm;text-indent:.45em;}
.diamond{display:flex;align-items:center;gap:10px;margin:9mm 0;color:var(--gold);}
.diamond .ln{width:38mm;height:0.45mm;border-radius:1px;
  background:linear-gradient(90deg,rgba(201,162,74,0),var(--gold));}
.diamond .ln.r{background:linear-gradient(270deg,rgba(201,162,74,0),var(--gold));}
.diamond .dot{font-size:14px;}
.cover .tag{font-family:'Aldhabi','Majalla',serif;font-size:26px;color:var(--gold-2);
  margin-top:2mm;}
.cover .contact{margin-top:12mm;display:flex;flex-direction:column;align-items:center;gap:3mm;}
.cover .contact .cc-label{font-family:'Aldhabi','Majalla',serif;font-size:20px;color:var(--muted);}
.cover .contact .cc-phone{font-family:'Segoe UI',sans-serif;font-weight:700;direction:ltr;
  font-size:26px;letter-spacing:.14em;color:var(--gold-2);text-indent:.14em;
  display:flex;align-items:center;gap:9px;}
.cover .contact .cc-phone .ic{font-size:20px;color:var(--gold);}

/* ---------- CATEGORY ---------- */
/* No break-inside:avoid on the whole category (a category can be taller than a
   page). Instead: keep the heading intact and glued to its first item. */
.cat{margin:0 0 9mm;}
.cat:first-child{margin-top:1mm;}
.cat-head{text-align:center;margin:0 0 6mm;break-inside:avoid;break-after:avoid;}
.cat-ar{font-family:'Aldhabi','Majalla',serif;font-size:34px;font-weight:700;
  color:var(--gold-2);line-height:1.1;}
.cat-en{font-family:'Segoe UI',sans-serif;letter-spacing:.42em;font-size:11px;
  direction:ltr;color:var(--muted);text-transform:uppercase;margin-top:2.5mm;text-indent:.42em;}
.cat-rule{display:flex;justify-content:center;margin-top:3.5mm;}
.cat-rule span{position:relative;width:46mm;height:1px;
  background:linear-gradient(90deg,transparent,var(--gold),transparent);}
.cat-rule span::after{content:"\\25C6";position:absolute;top:-7px;left:50%;
  transform:translateX(-50%);color:var(--gold);font-size:9px;
  background:var(--bg);padding:0 6px;}

/* ---------- ITEM ---------- */
.items{display:flex;flex-direction:column;gap:4.5mm;}
.item{break-inside:avoid;}
.i-head{display:flex;align-items:baseline;gap:8px;}
.i-name{font-family:'Majalla',sans-serif;font-weight:700;font-size:23px;
  color:var(--cream);white-space:nowrap;}
.i-en{font-family:'Segoe UI',sans-serif;font-weight:400;font-size:12px;
  color:var(--muted);letter-spacing:.04em;}
.i-dots{flex:1;border-bottom:1px dotted rgba(201,162,74,.45);transform:translateY(-4px);}
.i-price{font-family:'Segoe UI',sans-serif;font-weight:700;font-size:19px;
  color:var(--gold-2);white-space:nowrap;}
.i-price::after{content:" \\062C.\\0645";font-size:11px;color:var(--muted);font-weight:400;}
.i-desc{font-family:'Majalla',sans-serif;font-size:16.5px;color:var(--muted);
  line-height:1.5;margin-top:1mm;max-width:88%;}
</style></head>
<body>
<div class="bg"></div>
<div class="frame"></div>

<section class="cover">
  <div class="diamond"><span class="ln"></span><span class="dot">&#9670;</span><span class="ln r"></span></div>
  <div class="brand">SOHO</div>
  <div class="brand-word">BITES</div>
  <div class="brand-sub">سوهو بايتس</div>
  <div class="diamond"><span class="ln"></span><span class="dot">&#9670;</span><span class="ln r"></span></div>
  <div class="tag">مطعم &amp; جريل</div>
  <div class="est">R E S T A U R A N T &nbsp;&middot;&nbsp; G R I L L &nbsp;&middot;&nbsp; C A F E</div>
  <div class="contact">
    <div class="cc-label">للحجز والطلبات</div>
    <div class="cc-phone"><span class="ic">&#9742;</span>${PHONE}</div>
  </div>
</section>

<table class="doc">
  <thead><tr><td class="pad-top"></td></tr></thead>
  <tfoot><tr><td class="pad-bot"><div class="foot"><span class="ic">&#9742;</span>&nbsp; ${PHONE}</div></td></tr></tfoot>
  <tbody><tr><td class="body-cell">
${sections}
  </td></tr></tbody>
</table>

</body></html>`;

const outHtml = path.join(ROOT, "soho-menu.html");
fs.writeFileSync(outHtml, html, "utf8");
console.log("HTML written:", outHtml);
let n = 0;
for (const k of ordered) n += data[k].length;
console.log(`Categories: ${ordered.length} | Items: ${n}`);
