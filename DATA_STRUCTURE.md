# Menu Management Guide

This document explains the data structure and how to edit the menu data easily.

---

## Project Structure

```
menu4/
├── index.html                 # Main menu display file
├── soho_items.json           # Soho restaurant menu items
├── istik_items.json          # Istik restaurant menu items
├── translations.json         # English translations for Arabic text
├── seed-data.html            # Backup/seed data file
├── admin/                    # Admin panel
│   └── index.html
└── assets/
    └── js/
        ├── firebase-client.js
        └── ...
```

---

## Main Data Files

### 1. **soho_items.json** (Soho Restaurant Menu)

Contains all menu items organized by categories.

**Structure:**

```json
{
  "CategoryNameInArabic": [
    {
      "name": "Item Name in Arabic",
      "name_en": "Item Name in English",
      "price": 250,
      "description": "Item description in Arabic (optional)"
    }
  ]
}
```

**Example - Pizza Category:**

```json
{
  "البيتزا": [
    {
      "name": "بيتزا مارجريتا",
      "name_en": "Margherita Pizza",
      "price": 230,
      "description": "صوص طماطم وجبنه موتزريلا وزعتر"
    },
    {
      "name": "بيتزا سي فود",
      "name_en": "Seafood Pizza",
      "price": 470,
      "description": "صوص طماطم وجبنه موتزريلا وجمبرى وكالمارى وكابوريا وزعتر وزيتون اخضر"
    }
  ]
}
```

---

### 2. **translations.json** (English Translations)

Contains English translations for item names, category names, and descriptions.

**Structure:**

```json
{
  "Arabic Text": "English Translation",
  "Arabic Text": "English Translation"
}
```

**Important Fields:**

- Item names (Arabic → English)
- Category names (Arabic → English)
- Descriptions (Arabic → English)

**Example:**

```json
{
  "البيتزا": "Pizza",
  "بيتزا مارجريتا": "Margherita Pizza",
  "صوص طماطم وجبنه موتزريلا وزعتر": "Tomato sauce, mozzarella cheese, and zaatar"
}
```

---

### 3. **istik_items.json**

Same structure as soho_items.json, but for a different restaurant (Istik).

---

## Category Configuration in index.html

Categories are registered in the `SOHO_CATS` object (around line 1632-1645).

**Structure:**

```javascript
const SOHO_CATS = {
  "🍕 Pizza": { ar: "البيتزا", icon: null },
  "🍔 Burgers": { ar: "البرجرات", icon: null },
  "🍟 Sides": { ar: "اكسترا", icon: null },
};
```

**Components:**

- `"🍕 Pizza"` = English name with emoji (key)
- `ar: "البيتزا"` = Arabic name for the category
- `icon: null` = Icon (usually null, can add custom icons)

---

## Step-by-Step: How to Edit Data

### ✅ ADD A NEW ITEM

**Step 1:** Open `soho_items.json`

**Step 2:** Find the category or create a new one:

```json
{
  "البيتزا": [
    { existing items... },
    {
      "name": "New Item in Arabic",
      "name_en": "New Item in English",
      "price": 250,
      "description": "Item description in Arabic"
    }
  ]
}
```

**Step 3:** Open `translations.json` and add translations:

```json
{
  "New Item in Arabic": "New Item in English",
  "Item description in Arabic": "Item description in English"
}
```

**Step 4:** Refresh the menu in browser

---

### ✅ EDIT AN EXISTING ITEM

**Step 1:** Open `soho_items.json`

**Step 2:** Find and update the item:

```json
{
  "name": "بيتزا مارجريتا",
  "name_en": "Margherita Pizza",
  "price": 250, // ← Change price
  "description": "New description" // ← Change description
}
```

**Step 3:** Update translations in `translations.json` if text changed

**Step 4:** Refresh browser

---

### ✅ ADD A NEW CATEGORY

**Step 1:** Open `soho_items.json` and add a new category:

```json
{
  "البيتزا": [...],
  "الجديد": [  // ← New category
    {
      "name": "item name",
      "name_en": "item english",
      "price": 100,
      "description": "description"
    }
  ]
}
```

**Step 2:** Open `index.html` and find `SOHO_CATS` (around line 1632)

**Step 3:** Add the category configuration:

```javascript
const SOHO_CATS = {
  "🍕 Pizza": { ar: "البيتزا", icon: null },
  "🆕 New Category": { ar: "الجديد", icon: null }, // ← Add this
  // ...
};
```

**Step 4:** Open `index.html` and find `SOHO_AR_TO_EN` (around line 1525)

**Step 5:** Add the mapping:

```javascript
const SOHO_AR_TO_EN = {
  البيتزا: "🍕 Pizza",
  الجديد: "🆕 New Category", // ← Add this
  // ...
};
```

**Step 6:** Add translations in `translations.json`:

```json
{
  "الجديد": "New Category",
  "item name": "item english"
}
```

**Step 7:** Refresh browser

---

### ✅ DELETE AN ITEM

**Step 1:** Open `soho_items.json`

**Step 2:** Remove the item object from the array:

```json
{
  "البيتزا": [
    { item 1 },
    { item 2 },
    // ← Delete item 3 completely
    { item 4 }
  ]
}
```

**Step 3:** (Optional) Remove translations from `translations.json`

**Step 4:** Refresh browser

---

### ✅ DELETE A CATEGORY

**Step 1:** Remove from `soho_items.json` - delete the entire category key and array

**Step 2:** Remove from `SOHO_CATS` in `index.html`

**Step 3:** Remove from `SOHO_AR_TO_EN` in `index.html`

**Step 4:** Remove translations from `translations.json`

**Step 5:** Refresh browser

---

## Field Reference

| Field         | Type   | Required?   | Example            | Notes                      |
| ------------- | ------ | ----------- | ------------------ | -------------------------- |
| `name`        | String | ✅ Yes      | "بيتزا مارجريتا"   | Arabic item name           |
| `name_en`     | String | ✅ Yes      | "Margherita Pizza" | English item name          |
| `price`       | Number | ✅ Yes      | 230                | Price in EGP (no text)     |
| `description` | String | ❌ Optional | "صوص طماطم..."     | Item description in Arabic |

---

## Important Notes

⚠️ **JSON Format Rules:**

- Always use double quotes `"` (not single quotes)
- Don't leave trailing commas after last item
- Objects need curly braces `{ }`
- Arrays need square brackets `[ ]`
- Use `,` between items but NOT after the last one

⚠️ **File Locations:**

- Edit `soho_items.json` for Soho restaurant
- Edit `istik_items.json` for Istik restaurant
- Always update `translations.json` for new text

⚠️ **Don't Touch:**

- `index.html` functions (unless adding new categories)
- Firebase config
- Admin panel code

---

## Bilingual Display

**How it works:**

1. Menu reads Arabic names from `soho_items.json`
2. When user switches to English, it looks up translations in `translations.json`
3. If no translation found, shows Arabic text

**Example:**

```
Arabic mode: "بيتزا مارجريتا"
English mode: "Margherita Pizza" (from translations.json)
```

---

## Common Mistakes & Fixes

| Mistake                     | Fix                                                    |
| --------------------------- | ------------------------------------------------------ |
| Item doesn't appear         | Check JSON syntax with JSONLint.com                    |
| Wrong translation           | Add/update in translations.json                        |
| Missing comma               | Check all items have `,` between them                  |
| Category doesn't show       | Add to SOHO_CATS and SOHO_AR_TO_EN                     |
| Price shows as 0            | Make sure price is a number, not a string              |
| Description doesn't display | Check it's in "description" field, not as separate key |

---

## Testing Changes

After editing JSON files:

1. Save the file
2. Refresh browser (Ctrl+F5 or Cmd+Shift+R)
3. Switch language to Arabic and English
4. Check that:
   - ✅ Item appears in correct category
   - ✅ Price displays correctly
   - ✅ Description shows up
   - ✅ English translation appears when switched

---

## Quick Reference: File Editing Order

When adding/editing items, follow this order:

1. **Edit soho_items.json** ← Add item with name, name_en, price, description
2. **Edit translations.json** ← Add translations for name_en and description
3. **Edit index.html** ← Only if adding NEW category (add to SOHO_CATS & SOHO_AR_TO_EN)
4. **Refresh browser** ← Test changes

---

## Contact / Questions

If something breaks:

1. Check JSON syntax with JSONLint.com
2. Look at browser console (F12) for errors
3. Compare with working items in the JSON
4. Restore from backup if needed
