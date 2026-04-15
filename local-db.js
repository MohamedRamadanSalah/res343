// Local database using localStorage - works completely offline
class LocalDB {
  constructor() {
    this.menuKey = "restaurant_menus";
    this.initDefaults();
  }

  initDefaults() {
    if (!localStorage.getItem(this.menuKey)) {
      localStorage.setItem(this.menuKey, JSON.stringify(window.DEFAULT_MENUS || []));
    }
  }

  // Get all menu items
  getAll() {
    try {
      return JSON.parse(localStorage.getItem(this.menuKey)) || [];
    } catch (e) {
      console.error("Error reading menu items:", e);
      return [];
    }
  }

  // Add new item
  add(item) {
    try {
      const items = this.getAll();
      item.id = "item_" + Date.now();
      item.createdAt = new Date().toISOString();
      items.push(item);
      localStorage.setItem(this.menuKey, JSON.stringify(items));
      console.log("✅ Item added locally:", item.id);
      return item;
    } catch (e) {
      console.error("Error adding item:", e);
      return null;
    }
  }

  // Update existing item
  update(id, updates) {
    try {
      let items = this.getAll();
      const index = items.findIndex((item) => item.id === id);
      if (index !== -1) {
        items[index] = { ...items[index], ...updates };
        localStorage.setItem(this.menuKey, JSON.stringify(items));
        console.log("✅ Item updated locally:", id);
        return items[index];
      }
      return null;
    } catch (e) {
      console.error("Error updating item:", e);
      return null;
    }
  }

  // Delete item
  delete(id) {
    try {
      let items = this.getAll();
      items = items.filter((item) => item.id !== id);
      localStorage.setItem(this.menuKey, JSON.stringify(items));
      console.log("✅ Item deleted locally:", id);
      return true;
    } catch (e) {
      console.error("Error deleting item:", e);
      return false;
    }
  }

  // Filter items by menu type
  filterByMenu(menuType) {
    return this.getAll().filter((item) => item.menu === menuType);
  }

  // Filter items by category
  filterByCategory(category) {
    return this.getAll().filter((item) => item.category === category);
  }

  // Export as JSON for backup
  export() {
    return JSON.stringify(this.getAll(), null, 2);
  }

  // Import from JSON
  import(jsonString) {
    try {
      const items = JSON.parse(jsonString);
      if (!Array.isArray(items)) throw new Error("Invalid format");
      localStorage.setItem(this.menuKey, JSON.stringify(items));
      console.log("✅ Items imported:", items.length);
      return true;
    } catch (e) {
      console.error("Error importing items:", e);
      return false;
    }
  }
}

window.LocalDB = LocalDB;
