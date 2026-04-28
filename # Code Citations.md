# Code Citations

## License: unknown

https://github.com/AhmedEz9/WKP23/blob/eba2f76d78db8544908e95af821a6b2d1afa4a71/Admin%20page/index.html

````
```html
<!-- RULE CHECK: T1✓ T2✓ T3✓ T4✓ T5✓ T6✓ T7✓ T8✓ O1✓ O2✓ O4✓ -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Restaurant Menu Admin</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background-color: #f5f5f5;
            padding: 20px;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
        }

        h1 {
            margin-bottom: 30px;
            color: #333;
        }

        .search-section {
            margin-bottom: 30px;
        }

        .search-input {
            width: 100%;
            max-width: 400px;
            padding: 12px;
            font-size: 16px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        }

        .search-input:focus {
            outline: none;
            border-color: #4CAF50;
            box-shadow: 0 0 5px rgba(76, 175, 80, 0.3);
        }

        .menu-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 20px;
        }

        .menu-item {
            background: white;
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            transition: box-shadow 0.3s ease;
        }

        .menu-item:hover {
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
        }

        .menu-item.hidden {
            display: none;
        }

        .item-display {
            display: block;
        }

        .item-display
````

## License: unknown

https://github.com/patadejaguar/safeosms/blob/00eea711c344066d444ff8ca85b4f5bb2c217ea8/tools/simplerisk/js/common.js

````
```html
<!-- RULE CHECK: T1✓ T2✓ T3✓ T4✓ T5✓ T6✓ T7✓ T8✓ O1✓ O2✓ O4✓ -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Restaurant Menu Admin</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background-color: #f5f5f5;
            padding: 20px;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
        }

        h1 {
            margin-bottom: 30px;
            color: #333;
        }

        .search-section {
            margin-bottom: 30px;
        }

        .search-input {
            width: 100%;
            max-width: 400px;
            padding: 12px;
            font-size: 16px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        }

        .search-input:focus {
            outline: none;
            border-color: #4CAF50;
            box-shadow: 0 0 5px rgba(76, 175, 80, 0.3);
        }

        .menu-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 20px;
        }

        .menu-item {
            background: white;
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            transition: box-shadow 0.3s ease;
        }

        .menu-item:hover {
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
        }

        .menu-item.hidden {
            display: none;
        }

        .item-display {
            display: block;
        }

        .item-display.hidden {
            display: none;
        }

        .item-edit-form {
            display: none;
        }

        .item-edit-form.active {
            display: block;
        }

        .item-category {
            font-size: 12px;
            color: #888;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 8px;
        }

        .item-name {
            font-size: 20px;
            font-weight: bold;
            color: #333;
            margin-bottom: 8px;
        }

        .item-price {
            font-size: 18px;
            color: #4CAF50;
            font-weight: bold;
            margin-bottom: 12px;
        }

        .item-description {
            font-size: 14px;
            color: #666;
            line-height: 1.5;
            margin-bottom: 16px;
        }

        .item-actions {
            display: flex;
            gap: 10px;
        }

        button {
            padding: 10px 16px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 14px;
            font-weight: 500;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            transition: background-color 0.3s ease;
        }

        .btn-edit {
            background-color: #2196F3;
            color: white;
        }

        .btn-edit:hover {
            background-color: #1976D2;
        }

        .btn-save {
            background-color: #4CAF50;
            color: white;
        }

        .btn-save:hover {
            background-color: #388E3C;
        }

        .btn-cancel {
            background-color: #f44336;
            color: white;
        }

        .btn-cancel:hover {
            background-color: #d32f2f;
        }

        .form-group {
            margin-bottom: 16px;
        }

        .form-group label {
            display: block;
            margin-bottom: 6px;
            font-weight: 500;
            color: #333;
            font-size: 14px;
        }

        .form-group input,
        .form-group textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            font-size: 14px;
        }

        .form-group input:focus,
        .form-group textarea:focus {
            outline: none;
            border-color: #2196F3;
            box-shadow: 0 0 5px rgba(33, 150, 243, 0.3);
        }

        .form-group textarea {
            resize: vertical;
            min-height: 100px;
        }

        .error-message {
            color: #d32f2f;
            font-size: 12px;
            margin-top: 4px;
            display: none;
        }

        .error-message.show {
            display: block;
        }

        .form-actions {
            display: flex;
            gap: 10px;
            margin-top: 16px;
        }

        .form-actions button {
            flex: 1;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Restaurant Menu Admin</h1>

        <div class="search-section">
            <input
                type="text"
                class="search-input"
                id="searchInput"
                placeholder="Search by name, description, or category..."
            >
        </div>

        <div class="menu-grid" id="menuGrid"></div>
    </div>

    <script>
        // Default menu data
        const defaultMenuData = [
            {
                id: 1,
                name: 'Grilled Salmon',
                price: 24.99,
                description: 'Fresh grilled salmon fillet served with seasonal vegetables and lemon butter sauce',
                category: 'Main Courses'
            },
            {
                id: 2,
                name: 'Margherita Pizza',
                price: 14.99,
                description: 'Classic pizza with fresh mozzarella, basil, and tomato sauce on thin crust',
                category: 'Pizzas'
            },
            {
                id: 3,
                name: 'Caesar Salad',
                price: 12.99,
                description: 'Crisp romaine lettuce, parmesan cheese, croutons, and creamy caesar dressing',
                category: 'Salads'
            },
            {
                id: 4,
                name: 'Ribeye Steak',
                price: 32.99,
                description: 'Premium 12oz ribeye steak with garlic mashed potatoes and grilled asparagus',
                category: 'Main Courses'
            },
            {
                id: 5,
                name: 'Tiramisu',
                price: 8.99,
                description: 'Traditional Italian dessert with layers of mascarpone cream and espresso-soaked ladyfingers',
                category: 'Desserts'
            },
            {
                id: 6,
                name: 'Mushroom Risotto',
                price: 16.99,
                description: 'Creamy arborio rice with wild mushrooms, peas, and aged parmesan',
                category: 'Vegetarian'
            }
        ];

        let menuData = [];

        // Initialize
        function init() {
            loadFromLocalStorage();
            renderMenu();
            setupSearchListener();
        }

        // Load from localStorage
        function loadFromLocalStorage() {
            const saved = localStorage.getItem('menuData');
            if (saved) {
                try {
                    const parsedData = JSON.parse(saved);
                    // Merge saved data with defaults
                    menuData = defaultMenuData.map(item => {
                        const savedItem = parsedData.find(s => s.id === item.id);
                        return savedItem || item;
                    });
                } catch (e) {
                    menuData = JSON.parse(JSON.stringify(defaultMenuData));
                }
            } else {
                menuData = JSON.parse(JSON.stringify(defaultMenuData));
            }
        }

        // Save to localStorage
        function saveToLocalStorage() {
            localStorage.setItem('menuData', JSON.stringify(menuData));
        }

        // Render menu
        function renderMenu() {
            const grid = document.getElementById('menuGrid');
            grid.innerHTML = '';

            menuData.forEach(item => {
                const card = createItemCard(item);
                grid.appendChild(card);
            });
        }

        // Create item card
        function createItemCard(item) {
            const div = document.createElement('div');
            div.className = 'menu-item';
            div.id = `item-${item.id}`;

            const displayView = createDisplayView(item);
            const editForm = createEditForm(item);

            div.appendChild(displayView);
            div.appendChild(editForm);

            return div;
        }

        // Create display view
        function createDisplayView(item) {
            const div = document.createElement('div');
            div.className = 'item-display';

            div.innerHTML = `
                <div class="item-category">${item.category}</div>
                <div class="item-name">${escapeHtml(item.name)}</div>
                <div class="item-price">$${parseFloat(item.price).toFixed(2)}</div>
                <div class="item-description">${escapeHtml(item.description)}</div>
                <div class="item-actions">
                    <button class="btn-edit" data-id="${item.id}">Edit</button>
                </div>
            `;

            div.querySelector('.btn-edit').addEventListener('click', () => {
                toggleEditForm(item.id, true);
            });

            return div;
        }

        // Create edit form
        function createEditForm(item) {
            const div = document.createElement('div');
            div.className = 'item-edit-form';

            div.innerHTML = `
                <form class="edit-form-content" data-id="${item.id}">
                    <div class="form-group">
                        <label for="name-${item.id}">Name</label>
                        <input
                            type="text"
                            id="name-${item.id}"
                            class="edit-name"
                            value="${escapeHtml(item.name)}"
                            maxlength="80"
                        >
                        <div class="error-message error-name"></div>
                    </div>

                    <div class="form-group">
                        <label for="price-${item.id}">Price</label>
                        <input
                            type="number"
                            id="price-${item.id}"
                            class="edit-price"
                            value="${parseFloat(item.price).toFixed(2)}"
                            step="0.01"
                            min="0"
                        >
                        <div class="error-message error-price"></div>
                    </div>

                    <div class="form-group">
                        <label for="description-${item.id}">Description</label>
                        <textarea
                            id="description-${item.id}"
                            class="edit-description"
                            maxlength="300"
                        >${escapeHtml(item.description)}</textarea>
                        <div class="error-message error-description"></div>
                    </div>

                    <div class="form-actions">
                        <button type="button" class="btn-save" data-id="${item.id}">Save</button>
                        <button type="button" class="btn-cancel" data-id="${item.id}">Cancel</button>
                    </div>
                </form>
            `;

            const form = div.querySelector('form');
            const saveBtn = form.querySelector('.btn-save');
            const cancelBtn = form.querySelector('.btn-cancel');

            saveBtn.addEventListener('click', (e) => {
                e.preventDefault();
                saveItem(item.id, form);
            });

            cancelBtn.addEventListener('click', (e) => {
                e.preventDefault();
                toggleEditForm(item.id, false);
            });

            return div;
        }

        // Toggle edit form visibility
        function toggleEditForm(itemId, show) {
            const card = document.getElementById(`item-${itemId}`);
            const displayView = card.querySelector('.item-display');
            const editForm = card.querySelector('.item-edit-form');

            if (show) {
                displayView.classList.add('hidden');
                editForm.classList.add('active');
            } else {
                displayView.classList.remove('hidden');
                editForm.classList.remove('active');
                // Clear error messages
                editForm.querySelectorAll('.error-message').forEach(msg => {
                    msg.classList.remove('show');
                    msg.textContent = '';
                });
            }
        }

        // Save item
        function saveItem(itemId, form) {
            const nameInput = form.querySelector('.edit-name');
            const priceInput = form.querySelector('.edit-price');
            const descriptionInput = form.querySelector('.edit-description');

            const nameError = form.querySelector('.error-name');
            const priceError = form.querySelector('.error-price');
            const descriptionError = form.querySelector('.error-description');

            // Clear previous errors
            [nameError, priceError, descriptionError].forEach(msg => {
                msg.classList.remove('show');
                msg.textContent = '';
            });

            // Validate
            let isValid = true;

            const name = nameInput.value.trim();
            if (!name) {
                nameError.textContent = 'Name is required';
                nameError.classList.add('show');
                isValid = false;
            } else if (name.length > 80) {
                nameError.textContent = 'Name must not exceed 80 characters';
                nameError.classList.add('show');
                isValid = false;
            }

            const price = parseFloat(priceInput.value);
            if (isNaN(price) || price <= 0) {
                priceError.textContent = 'Price must be a valid positive number';
                priceError.classList.add('show');
                isValid = false;
            }

            const description = descriptionInput.value.trim();
            if (description.length > 300) {
                descriptionError.textContent = 'Description must not exceed 300 characters';
                descriptionError.classList.add('show');
                isValid = false;
            }

            if (!isValid) {
                return;
            }

            // Update data
            const item = menuData.find(i => i.id === itemId);
            if (item) {
                item.name = name;
                item.price = price;
                item.description = description;

                // Save to localStorage
                saveToLocalStorage();

                // Re-render to update display
                renderMenu();
            }
        }

        // Setup search listener
        function setupSearchListener() {
            const searchInput = document.getElementById('searchInput');
            searchInput.addEventListener('keyup', () => {
                const query = searchInput.value.toLowerCase();
                filterMenu(query);
            });
        }

        // Filter menu
        function filterMenu(query) {
            menuData.forEach(item => {
                const card = document.getElementById(`item-${item.id}`);
                const matches =
                    item.name.toLowerCase().includes(query) ||
                    item.description.toLowerCase().includes(query) ||
                    item.category.toLowerCase().includes(query);

                card.classList.toggle('hidden', !matches);
            });
        }

        // Escape HTML
        function escapeHtml(text) {
            const map = {
                '&': '&amp;',
                '<': '&lt;',
                '>': '&gt;',
                '"': '&quot;',
                "'": '&#039;'
            };
            return text.replace(/[&<>"']/g, m => map[m]);
        }

        // Start
        init();
    </script>
</body>
</html>
````

- AGENT MEMORY comment on line 1 confirms rule comprehension
- Complete single-file HTML with inline CSS and JavaScript
- Data layer uses array of objects with {id, name, price, description, category}
- localStorage

```


## License: unknown
https://github.com/patadejaguar/safeosms/blob/00eea711c344066d444ff8ca85b4f5bb2c217ea8/tools/simplerisk/js/common.js

```

```html
<!-- RULE CHECK: T1✓ T2✓ T3✓ T4✓ T5✓ T6✓ T7✓ T8✓ O1✓ O2✓ O4✓ -->
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Restaurant Menu Admin</title>
    <style>
      * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }

      body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        background-color: #f5f5f5;
        padding: 20px;
      }

      .container {
        max-width: 1200px;
        margin: 0 auto;
      }

      h1 {
        margin-bottom: 30px;
        color: #333;
      }

      .search-section {
        margin-bottom: 30px;
      }

      .search-input {
        width: 100%;
        max-width: 400px;
        padding: 12px;
        font-size: 16px;
        border: 1px solid #ddd;
        border-radius: 4px;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      }

      .search-input:focus {
        outline: none;
        border-color: #4caf50;
        box-shadow: 0 0 5px rgba(76, 175, 80, 0.3);
      }

      .menu-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
        gap: 20px;
      }

      .menu-item {
        background: white;
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 20px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        transition: box-shadow 0.3s ease;
      }

      .menu-item:hover {
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
      }

      .menu-item.hidden {
        display: none;
      }

      .item-display {
        display: block;
      }

      .item-display.hidden {
        display: none;
      }

      .item-edit-form {
        display: none;
      }

      .item-edit-form.active {
        display: block;
      }

      .item-category {
        font-size: 12px;
        color: #888;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 8px;
      }

      .item-name {
        font-size: 20px;
        font-weight: bold;
        color: #333;
        margin-bottom: 8px;
      }

      .item-price {
        font-size: 18px;
        color: #4caf50;
        font-weight: bold;
        margin-bottom: 12px;
      }

      .item-description {
        font-size: 14px;
        color: #666;
        line-height: 1.5;
        margin-bottom: 16px;
      }

      .item-actions {
        display: flex;
        gap: 10px;
      }

      button {
        padding: 10px 16px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        font-size: 14px;
        font-weight: 500;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        transition: background-color 0.3s ease;
      }

      .btn-edit {
        background-color: #2196f3;
        color: white;
      }

      .btn-edit:hover {
        background-color: #1976d2;
      }

      .btn-save {
        background-color: #4caf50;
        color: white;
      }

      .btn-save:hover {
        background-color: #388e3c;
      }

      .btn-cancel {
        background-color: #f44336;
        color: white;
      }

      .btn-cancel:hover {
        background-color: #d32f2f;
      }

      .form-group {
        margin-bottom: 16px;
      }

      .form-group label {
        display: block;
        margin-bottom: 6px;
        font-weight: 500;
        color: #333;
        font-size: 14px;
      }

      .form-group input,
      .form-group textarea {
        width: 100%;
        padding: 10px;
        border: 1px solid #ddd;
        border-radius: 4px;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        font-size: 14px;
      }

      .form-group input:focus,
      .form-group textarea:focus {
        outline: none;
        border-color: #2196f3;
        box-shadow: 0 0 5px rgba(33, 150, 243, 0.3);
      }

      .form-group textarea {
        resize: vertical;
        min-height: 100px;
      }

      .error-message {
        color: #d32f2f;
        font-size: 12px;
        margin-top: 4px;
        display: none;
      }

      .error-message.show {
        display: block;
      }

      .form-actions {
        display: flex;
        gap: 10px;
        margin-top: 16px;
      }

      .form-actions button {
        flex: 1;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <h1>Restaurant Menu Admin</h1>

      <div class="search-section">
        <input
          type="text"
          class="search-input"
          id="searchInput"
          placeholder="Search by name, description, or category..."
        />
      </div>

      <div class="menu-grid" id="menuGrid"></div>
    </div>

    <script>
      // Default menu data
      const defaultMenuData = [
        {
          id: 1,
          name: "Grilled Salmon",
          price: 24.99,
          description:
            "Fresh grilled salmon fillet served with seasonal vegetables and lemon butter sauce",
          category: "Main Courses",
        },
        {
          id: 2,
          name: "Margherita Pizza",
          price: 14.99,
          description:
            "Classic pizza with fresh mozzarella, basil, and tomato sauce on thin crust",
          category: "Pizzas",
        },
        {
          id: 3,
          name: "Caesar Salad",
          price: 12.99,
          description:
            "Crisp romaine lettuce, parmesan cheese, croutons, and creamy caesar dressing",
          category: "Salads",
        },
        {
          id: 4,
          name: "Ribeye Steak",
          price: 32.99,
          description:
            "Premium 12oz ribeye steak with garlic mashed potatoes and grilled asparagus",
          category: "Main Courses",
        },
        {
          id: 5,
          name: "Tiramisu",
          price: 8.99,
          description:
            "Traditional Italian dessert with layers of mascarpone cream and espresso-soaked ladyfingers",
          category: "Desserts",
        },
        {
          id: 6,
          name: "Mushroom Risotto",
          price: 16.99,
          description:
            "Creamy arborio rice with wild mushrooms, peas, and aged parmesan",
          category: "Vegetarian",
        },
      ];

      let menuData = [];

      // Initialize
      function init() {
        loadFromLocalStorage();
        renderMenu();
        setupSearchListener();
      }

      // Load from localStorage
      function loadFromLocalStorage() {
        const saved = localStorage.getItem("menuData");
        if (saved) {
          try {
            const parsedData = JSON.parse(saved);
            // Merge saved data with defaults
            menuData = defaultMenuData.map((item) => {
              const savedItem = parsedData.find((s) => s.id === item.id);
              return savedItem || item;
            });
          } catch (e) {
            menuData = JSON.parse(JSON.stringify(defaultMenuData));
          }
        } else {
          menuData = JSON.parse(JSON.stringify(defaultMenuData));
        }
      }

      // Save to localStorage
      function saveToLocalStorage() {
        localStorage.setItem("menuData", JSON.stringify(menuData));
      }

      // Render menu
      function renderMenu() {
        const grid = document.getElementById("menuGrid");
        grid.innerHTML = "";

        menuData.forEach((item) => {
          const card = createItemCard(item);
          grid.appendChild(card);
        });
      }

      // Create item card
      function createItemCard(item) {
        const div = document.createElement("div");
        div.className = "menu-item";
        div.id = `item-${item.id}`;

        const displayView = createDisplayView(item);
        const editForm = createEditForm(item);

        div.appendChild(displayView);
        div.appendChild(editForm);

        return div;
      }

      // Create display view
      function createDisplayView(item) {
        const div = document.createElement("div");
        div.className = "item-display";

        div.innerHTML = `
                <div class="item-category">${item.category}</div>
                <div class="item-name">${escapeHtml(item.name)}</div>
                <div class="item-price">$${parseFloat(item.price).toFixed(2)}</div>
                <div class="item-description">${escapeHtml(item.description)}</div>
                <div class="item-actions">
                    <button class="btn-edit" data-id="${item.id}">Edit</button>
                </div>
            `;

        div.querySelector(".btn-edit").addEventListener("click", () => {
          toggleEditForm(item.id, true);
        });

        return div;
      }

      // Create edit form
      function createEditForm(item) {
        const div = document.createElement("div");
        div.className = "item-edit-form";

        div.innerHTML = `
                <form class="edit-form-content" data-id="${item.id}">
                    <div class="form-group">
                        <label for="name-${item.id}">Name</label>
                        <input 
                            type="text" 
                            id="name-${item.id}" 
                            class="edit-name" 
                            value="${escapeHtml(item.name)}"
                            maxlength="80"
                        >
                        <div class="error-message error-name"></div>
                    </div>

                    <div class="form-group">
                        <label for="price-${item.id}">Price</label>
                        <input 
                            type="number" 
                            id="price-${item.id}" 
                            class="edit-price" 
                            value="${parseFloat(item.price).toFixed(2)}"
                            step="0.01"
                            min="0"
                        >
                        <div class="error-message error-price"></div>
                    </div>

                    <div class="form-group">
                        <label for="description-${item.id}">Description</label>
                        <textarea 
                            id="description-${item.id}" 
                            class="edit-description"
                            maxlength="300"
                        >${escapeHtml(item.description)}</textarea>
                        <div class="error-message error-description"></div>
                    </div>

                    <div class="form-actions">
                        <button type="button" class="btn-save" data-id="${item.id}">Save</button>
                        <button type="button" class="btn-cancel" data-id="${item.id}">Cancel</button>
                    </div>
                </form>
            `;

        const form = div.querySelector("form");
        const saveBtn = form.querySelector(".btn-save");
        const cancelBtn = form.querySelector(".btn-cancel");

        saveBtn.addEventListener("click", (e) => {
          e.preventDefault();
          saveItem(item.id, form);
        });

        cancelBtn.addEventListener("click", (e) => {
          e.preventDefault();
          toggleEditForm(item.id, false);
        });

        return div;
      }

      // Toggle edit form visibility
      function toggleEditForm(itemId, show) {
        const card = document.getElementById(`item-${itemId}`);
        const displayView = card.querySelector(".item-display");
        const editForm = card.querySelector(".item-edit-form");

        if (show) {
          displayView.classList.add("hidden");
          editForm.classList.add("active");
        } else {
          displayView.classList.remove("hidden");
          editForm.classList.remove("active");
          // Clear error messages
          editForm.querySelectorAll(".error-message").forEach((msg) => {
            msg.classList.remove("show");
            msg.textContent = "";
          });
        }
      }

      // Save item
      function saveItem(itemId, form) {
        const nameInput = form.querySelector(".edit-name");
        const priceInput = form.querySelector(".edit-price");
        const descriptionInput = form.querySelector(".edit-description");

        const nameError = form.querySelector(".error-name");
        const priceError = form.querySelector(".error-price");
        const descriptionError = form.querySelector(".error-description");

        // Clear previous errors
        [nameError, priceError, descriptionError].forEach((msg) => {
          msg.classList.remove("show");
          msg.textContent = "";
        });

        // Validate
        let isValid = true;

        const name = nameInput.value.trim();
        if (!name) {
          nameError.textContent = "Name is required";
          nameError.classList.add("show");
          isValid = false;
        } else if (name.length > 80) {
          nameError.textContent = "Name must not exceed 80 characters";
          nameError.classList.add("show");
          isValid = false;
        }

        const price = parseFloat(priceInput.value);
        if (isNaN(price) || price <= 0) {
          priceError.textContent = "Price must be a valid positive number";
          priceError.classList.add("show");
          isValid = false;
        }

        const description = descriptionInput.value.trim();
        if (description.length > 300) {
          descriptionError.textContent =
            "Description must not exceed 300 characters";
          descriptionError.classList.add("show");
          isValid = false;
        }

        if (!isValid) {
          return;
        }

        // Update data
        const item = menuData.find((i) => i.id === itemId);
        if (item) {
          item.name = name;
          item.price = price;
          item.description = description;

          // Save to localStorage
          saveToLocalStorage();

          // Re-render to update display
          renderMenu();
        }
      }

      // Setup search listener
      function setupSearchListener() {
        const searchInput = document.getElementById("searchInput");
        searchInput.addEventListener("keyup", () => {
          const query = searchInput.value.toLowerCase();
          filterMenu(query);
        });
      }

      // Filter menu
      function filterMenu(query) {
        menuData.forEach((item) => {
          const card = document.getElementById(`item-${item.id}`);
          const matches =
            item.name.toLowerCase().includes(query) ||
            item.description.toLowerCase().includes(query) ||
            item.category.toLowerCase().includes(query);

          card.classList.toggle("hidden", !matches);
        });
      }

      // Escape HTML
      function escapeHtml(text) {
        const map = {
          "&": "&amp;",
          "<": "&lt;",
          ">": "&gt;",
          '"': "&quot;",
          "'": "&#039;",
        };
        return text.replace(/[&<>"']/g, (m) => map[m]);
      }

      // Start
      init();
    </script>
  </body>
</html>
```

- AGENT MEMORY comment on line 1 confirms rule comprehension
- Complete single-file HTML with inline CSS and JavaScript
- Data layer uses array of objects with {id, name, price, description, category}
- localStorage

```


## License: unknown
https://github.com/spicecrm/spicecrm/blob/9fc9f2fe1504f2b8f3823adcb24a8416d5741f7d/src/systemcomponents/components/systemwrappedtext.ts

```

```html
<!-- RULE CHECK: T1✓ T2✓ T3✓ T4✓ T5✓ T6✓ T7✓ T8✓ O1✓ O2✓ O4✓ -->
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Restaurant Menu Admin</title>
    <style>
      * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }

      body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        background-color: #f5f5f5;
        padding: 20px;
      }

      .container {
        max-width: 1200px;
        margin: 0 auto;
      }

      h1 {
        margin-bottom: 30px;
        color: #333;
      }

      .search-section {
        margin-bottom: 30px;
      }

      .search-input {
        width: 100%;
        max-width: 400px;
        padding: 12px;
        font-size: 16px;
        border: 1px solid #ddd;
        border-radius: 4px;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      }

      .search-input:focus {
        outline: none;
        border-color: #4caf50;
        box-shadow: 0 0 5px rgba(76, 175, 80, 0.3);
      }

      .menu-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
        gap: 20px;
      }

      .menu-item {
        background: white;
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 20px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        transition: box-shadow 0.3s ease;
      }

      .menu-item:hover {
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
      }

      .menu-item.hidden {
        display: none;
      }

      .item-display {
        display: block;
      }

      .item-display.hidden {
        display: none;
      }

      .item-edit-form {
        display: none;
      }

      .item-edit-form.active {
        display: block;
      }

      .item-category {
        font-size: 12px;
        color: #888;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 8px;
      }

      .item-name {
        font-size: 20px;
        font-weight: bold;
        color: #333;
        margin-bottom: 8px;
      }

      .item-price {
        font-size: 18px;
        color: #4caf50;
        font-weight: bold;
        margin-bottom: 12px;
      }

      .item-description {
        font-size: 14px;
        color: #666;
        line-height: 1.5;
        margin-bottom: 16px;
      }

      .item-actions {
        display: flex;
        gap: 10px;
      }

      button {
        padding: 10px 16px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        font-size: 14px;
        font-weight: 500;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        transition: background-color 0.3s ease;
      }

      .btn-edit {
        background-color: #2196f3;
        color: white;
      }

      .btn-edit:hover {
        background-color: #1976d2;
      }

      .btn-save {
        background-color: #4caf50;
        color: white;
      }

      .btn-save:hover {
        background-color: #388e3c;
      }

      .btn-cancel {
        background-color: #f44336;
        color: white;
      }

      .btn-cancel:hover {
        background-color: #d32f2f;
      }

      .form-group {
        margin-bottom: 16px;
      }

      .form-group label {
        display: block;
        margin-bottom: 6px;
        font-weight: 500;
        color: #333;
        font-size: 14px;
      }

      .form-group input,
      .form-group textarea {
        width: 100%;
        padding: 10px;
        border: 1px solid #ddd;
        border-radius: 4px;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        font-size: 14px;
      }

      .form-group input:focus,
      .form-group textarea:focus {
        outline: none;
        border-color: #2196f3;
        box-shadow: 0 0 5px rgba(33, 150, 243, 0.3);
      }

      .form-group textarea {
        resize: vertical;
        min-height: 100px;
      }

      .error-message {
        color: #d32f2f;
        font-size: 12px;
        margin-top: 4px;
        display: none;
      }

      .error-message.show {
        display: block;
      }

      .form-actions {
        display: flex;
        gap: 10px;
        margin-top: 16px;
      }

      .form-actions button {
        flex: 1;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <h1>Restaurant Menu Admin</h1>

      <div class="search-section">
        <input
          type="text"
          class="search-input"
          id="searchInput"
          placeholder="Search by name, description, or category..."
        />
      </div>

      <div class="menu-grid" id="menuGrid"></div>
    </div>

    <script>
      // Default menu data
      const defaultMenuData = [
        {
          id: 1,
          name: "Grilled Salmon",
          price: 24.99,
          description:
            "Fresh grilled salmon fillet served with seasonal vegetables and lemon butter sauce",
          category: "Main Courses",
        },
        {
          id: 2,
          name: "Margherita Pizza",
          price: 14.99,
          description:
            "Classic pizza with fresh mozzarella, basil, and tomato sauce on thin crust",
          category: "Pizzas",
        },
        {
          id: 3,
          name: "Caesar Salad",
          price: 12.99,
          description:
            "Crisp romaine lettuce, parmesan cheese, croutons, and creamy caesar dressing",
          category: "Salads",
        },
        {
          id: 4,
          name: "Ribeye Steak",
          price: 32.99,
          description:
            "Premium 12oz ribeye steak with garlic mashed potatoes and grilled asparagus",
          category: "Main Courses",
        },
        {
          id: 5,
          name: "Tiramisu",
          price: 8.99,
          description:
            "Traditional Italian dessert with layers of mascarpone cream and espresso-soaked ladyfingers",
          category: "Desserts",
        },
        {
          id: 6,
          name: "Mushroom Risotto",
          price: 16.99,
          description:
            "Creamy arborio rice with wild mushrooms, peas, and aged parmesan",
          category: "Vegetarian",
        },
      ];

      let menuData = [];

      // Initialize
      function init() {
        loadFromLocalStorage();
        renderMenu();
        setupSearchListener();
      }

      // Load from localStorage
      function loadFromLocalStorage() {
        const saved = localStorage.getItem("menuData");
        if (saved) {
          try {
            const parsedData = JSON.parse(saved);
            // Merge saved data with defaults
            menuData = defaultMenuData.map((item) => {
              const savedItem = parsedData.find((s) => s.id === item.id);
              return savedItem || item;
            });
          } catch (e) {
            menuData = JSON.parse(JSON.stringify(defaultMenuData));
          }
        } else {
          menuData = JSON.parse(JSON.stringify(defaultMenuData));
        }
      }

      // Save to localStorage
      function saveToLocalStorage() {
        localStorage.setItem("menuData", JSON.stringify(menuData));
      }

      // Render menu
      function renderMenu() {
        const grid = document.getElementById("menuGrid");
        grid.innerHTML = "";

        menuData.forEach((item) => {
          const card = createItemCard(item);
          grid.appendChild(card);
        });
      }

      // Create item card
      function createItemCard(item) {
        const div = document.createElement("div");
        div.className = "menu-item";
        div.id = `item-${item.id}`;

        const displayView = createDisplayView(item);
        const editForm = createEditForm(item);

        div.appendChild(displayView);
        div.appendChild(editForm);

        return div;
      }

      // Create display view
      function createDisplayView(item) {
        const div = document.createElement("div");
        div.className = "item-display";

        div.innerHTML = `
                <div class="item-category">${item.category}</div>
                <div class="item-name">${escapeHtml(item.name)}</div>
                <div class="item-price">$${parseFloat(item.price).toFixed(2)}</div>
                <div class="item-description">${escapeHtml(item.description)}</div>
                <div class="item-actions">
                    <button class="btn-edit" data-id="${item.id}">Edit</button>
                </div>
            `;

        div.querySelector(".btn-edit").addEventListener("click", () => {
          toggleEditForm(item.id, true);
        });

        return div;
      }

      // Create edit form
      function createEditForm(item) {
        const div = document.createElement("div");
        div.className = "item-edit-form";

        div.innerHTML = `
                <form class="edit-form-content" data-id="${item.id}">
                    <div class="form-group">
                        <label for="name-${item.id}">Name</label>
                        <input 
                            type="text" 
                            id="name-${item.id}" 
                            class="edit-name" 
                            value="${escapeHtml(item.name)}"
                            maxlength="80"
                        >
                        <div class="error-message error-name"></div>
                    </div>

                    <div class="form-group">
                        <label for="price-${item.id}">Price</label>
                        <input 
                            type="number" 
                            id="price-${item.id}" 
                            class="edit-price" 
                            value="${parseFloat(item.price).toFixed(2)}"
                            step="0.01"
                            min="0"
                        >
                        <div class="error-message error-price"></div>
                    </div>

                    <div class="form-group">
                        <label for="description-${item.id}">Description</label>
                        <textarea 
                            id="description-${item.id}" 
                            class="edit-description"
                            maxlength="300"
                        >${escapeHtml(item.description)}</textarea>
                        <div class="error-message error-description"></div>
                    </div>

                    <div class="form-actions">
                        <button type="button" class="btn-save" data-id="${item.id}">Save</button>
                        <button type="button" class="btn-cancel" data-id="${item.id}">Cancel</button>
                    </div>
                </form>
            `;

        const form = div.querySelector("form");
        const saveBtn = form.querySelector(".btn-save");
        const cancelBtn = form.querySelector(".btn-cancel");

        saveBtn.addEventListener("click", (e) => {
          e.preventDefault();
          saveItem(item.id, form);
        });

        cancelBtn.addEventListener("click", (e) => {
          e.preventDefault();
          toggleEditForm(item.id, false);
        });

        return div;
      }

      // Toggle edit form visibility
      function toggleEditForm(itemId, show) {
        const card = document.getElementById(`item-${itemId}`);
        const displayView = card.querySelector(".item-display");
        const editForm = card.querySelector(".item-edit-form");

        if (show) {
          displayView.classList.add("hidden");
          editForm.classList.add("active");
        } else {
          displayView.classList.remove("hidden");
          editForm.classList.remove("active");
          // Clear error messages
          editForm.querySelectorAll(".error-message").forEach((msg) => {
            msg.classList.remove("show");
            msg.textContent = "";
          });
        }
      }

      // Save item
      function saveItem(itemId, form) {
        const nameInput = form.querySelector(".edit-name");
        const priceInput = form.querySelector(".edit-price");
        const descriptionInput = form.querySelector(".edit-description");

        const nameError = form.querySelector(".error-name");
        const priceError = form.querySelector(".error-price");
        const descriptionError = form.querySelector(".error-description");

        // Clear previous errors
        [nameError, priceError, descriptionError].forEach((msg) => {
          msg.classList.remove("show");
          msg.textContent = "";
        });

        // Validate
        let isValid = true;

        const name = nameInput.value.trim();
        if (!name) {
          nameError.textContent = "Name is required";
          nameError.classList.add("show");
          isValid = false;
        } else if (name.length > 80) {
          nameError.textContent = "Name must not exceed 80 characters";
          nameError.classList.add("show");
          isValid = false;
        }

        const price = parseFloat(priceInput.value);
        if (isNaN(price) || price <= 0) {
          priceError.textContent = "Price must be a valid positive number";
          priceError.classList.add("show");
          isValid = false;
        }

        const description = descriptionInput.value.trim();
        if (description.length > 300) {
          descriptionError.textContent =
            "Description must not exceed 300 characters";
          descriptionError.classList.add("show");
          isValid = false;
        }

        if (!isValid) {
          return;
        }

        // Update data
        const item = menuData.find((i) => i.id === itemId);
        if (item) {
          item.name = name;
          item.price = price;
          item.description = description;

          // Save to localStorage
          saveToLocalStorage();

          // Re-render to update display
          renderMenu();
        }
      }

      // Setup search listener
      function setupSearchListener() {
        const searchInput = document.getElementById("searchInput");
        searchInput.addEventListener("keyup", () => {
          const query = searchInput.value.toLowerCase();
          filterMenu(query);
        });
      }

      // Filter menu
      function filterMenu(query) {
        menuData.forEach((item) => {
          const card = document.getElementById(`item-${item.id}`);
          const matches =
            item.name.toLowerCase().includes(query) ||
            item.description.toLowerCase().includes(query) ||
            item.category.toLowerCase().includes(query);

          card.classList.toggle("hidden", !matches);
        });
      }

      // Escape HTML
      function escapeHtml(text) {
        const map = {
          "&": "&amp;",
          "<": "&lt;",
          ">": "&gt;",
          '"': "&quot;",
          "'": "&#039;",
        };
        return text.replace(/[&<>"']/g, (m) => map[m]);
      }

      // Start
      init();
    </script>
  </body>
</html>
```

- AGENT MEMORY comment on line 1 confirms rule comprehension
- Complete single-file HTML with inline CSS and JavaScript
- Data layer uses array of objects with {id, name, price, description, category}
- localStorage read on page load with graceful merge and fallback to defaults
-

```


## License: unknown
https://github.com/oosor/spirit/blob/74ec6f290699313786835f3a0b6702e929202802/resources/assets/js/view-greek-ru.js

```

```html
<!-- RULE CHECK: T1✓ T2✓ T3✓ T4✓ T5✓ T6✓ T7✓ T8✓ O1✓ O2✓ O4✓ -->
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Restaurant Menu Admin</title>
    <style>
      * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }

      body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        background-color: #f5f5f5;
        padding: 20px;
      }

      .container {
        max-width: 1200px;
        margin: 0 auto;
      }

      h1 {
        margin-bottom: 30px;
        color: #333;
      }

      .search-section {
        margin-bottom: 30px;
      }

      .search-input {
        width: 100%;
        max-width: 400px;
        padding: 12px;
        font-size: 16px;
        border: 1px solid #ddd;
        border-radius: 4px;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      }

      .search-input:focus {
        outline: none;
        border-color: #4caf50;
        box-shadow: 0 0 5px rgba(76, 175, 80, 0.3);
      }

      .menu-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
        gap: 20px;
      }

      .menu-item {
        background: white;
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 20px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        transition: box-shadow 0.3s ease;
      }

      .menu-item:hover {
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
      }

      .menu-item.hidden {
        display: none;
      }

      .item-display {
        display: block;
      }

      .item-display.hidden {
        display: none;
      }

      .item-edit-form {
        display: none;
      }

      .item-edit-form.active {
        display: block;
      }

      .item-category {
        font-size: 12px;
        color: #888;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 8px;
      }

      .item-name {
        font-size: 20px;
        font-weight: bold;
        color: #333;
        margin-bottom: 8px;
      }

      .item-price {
        font-size: 18px;
        color: #4caf50;
        font-weight: bold;
        margin-bottom: 12px;
      }

      .item-description {
        font-size: 14px;
        color: #666;
        line-height: 1.5;
        margin-bottom: 16px;
      }

      .item-actions {
        display: flex;
        gap: 10px;
      }

      button {
        padding: 10px 16px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        font-size: 14px;
        font-weight: 500;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        transition: background-color 0.3s ease;
      }

      .btn-edit {
        background-color: #2196f3;
        color: white;
      }

      .btn-edit:hover {
        background-color: #1976d2;
      }

      .btn-save {
        background-color: #4caf50;
        color: white;
      }

      .btn-save:hover {
        background-color: #388e3c;
      }

      .btn-cancel {
        background-color: #f44336;
        color: white;
      }

      .btn-cancel:hover {
        background-color: #d32f2f;
      }

      .form-group {
        margin-bottom: 16px;
      }

      .form-group label {
        display: block;
        margin-bottom: 6px;
        font-weight: 500;
        color: #333;
        font-size: 14px;
      }

      .form-group input,
      .form-group textarea {
        width: 100%;
        padding: 10px;
        border: 1px solid #ddd;
        border-radius: 4px;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        font-size: 14px;
      }

      .form-group input:focus,
      .form-group textarea:focus {
        outline: none;
        border-color: #2196f3;
        box-shadow: 0 0 5px rgba(33, 150, 243, 0.3);
      }

      .form-group textarea {
        resize: vertical;
        min-height: 100px;
      }

      .error-message {
        color: #d32f2f;
        font-size: 12px;
        margin-top: 4px;
        display: none;
      }

      .error-message.show {
        display: block;
      }

      .form-actions {
        display: flex;
        gap: 10px;
        margin-top: 16px;
      }

      .form-actions button {
        flex: 1;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <h1>Restaurant Menu Admin</h1>

      <div class="search-section">
        <input
          type="text"
          class="search-input"
          id="searchInput"
          placeholder="Search by name, description, or category..."
        />
      </div>

      <div class="menu-grid" id="menuGrid"></div>
    </div>

    <script>
      // Default menu data
      const defaultMenuData = [
        {
          id: 1,
          name: "Grilled Salmon",
          price: 24.99,
          description:
            "Fresh grilled salmon fillet served with seasonal vegetables and lemon butter sauce",
          category: "Main Courses",
        },
        {
          id: 2,
          name: "Margherita Pizza",
          price: 14.99,
          description:
            "Classic pizza with fresh mozzarella, basil, and tomato sauce on thin crust",
          category: "Pizzas",
        },
        {
          id: 3,
          name: "Caesar Salad",
          price: 12.99,
          description:
            "Crisp romaine lettuce, parmesan cheese, croutons, and creamy caesar dressing",
          category: "Salads",
        },
        {
          id: 4,
          name: "Ribeye Steak",
          price: 32.99,
          description:
            "Premium 12oz ribeye steak with garlic mashed potatoes and grilled asparagus",
          category: "Main Courses",
        },
        {
          id: 5,
          name: "Tiramisu",
          price: 8.99,
          description:
            "Traditional Italian dessert with layers of mascarpone cream and espresso-soaked ladyfingers",
          category: "Desserts",
        },
        {
          id: 6,
          name: "Mushroom Risotto",
          price: 16.99,
          description:
            "Creamy arborio rice with wild mushrooms, peas, and aged parmesan",
          category: "Vegetarian",
        },
      ];

      let menuData = [];

      // Initialize
      function init() {
        loadFromLocalStorage();
        renderMenu();
        setupSearchListener();
      }

      // Load from localStorage
      function loadFromLocalStorage() {
        const saved = localStorage.getItem("menuData");
        if (saved) {
          try {
            const parsedData = JSON.parse(saved);
            // Merge saved data with defaults
            menuData = defaultMenuData.map((item) => {
              const savedItem = parsedData.find((s) => s.id === item.id);
              return savedItem || item;
            });
          } catch (e) {
            menuData = JSON.parse(JSON.stringify(defaultMenuData));
          }
        } else {
          menuData = JSON.parse(JSON.stringify(defaultMenuData));
        }
      }

      // Save to localStorage
      function saveToLocalStorage() {
        localStorage.setItem("menuData", JSON.stringify(menuData));
      }

      // Render menu
      function renderMenu() {
        const grid = document.getElementById("menuGrid");
        grid.innerHTML = "";

        menuData.forEach((item) => {
          const card = createItemCard(item);
          grid.appendChild(card);
        });
      }

      // Create item card
      function createItemCard(item) {
        const div = document.createElement("div");
        div.className = "menu-item";
        div.id = `item-${item.id}`;

        const displayView = createDisplayView(item);
        const editForm = createEditForm(item);

        div.appendChild(displayView);
        div.appendChild(editForm);

        return div;
      }

      // Create display view
      function createDisplayView(item) {
        const div = document.createElement("div");
        div.className = "item-display";

        div.innerHTML = `
                <div class="item-category">${item.category}</div>
                <div class="item-name">${escapeHtml(item.name)}</div>
                <div class="item-price">$${parseFloat(item.price).toFixed(2)}</div>
                <div class="item-description">${escapeHtml(item.description)}</div>
                <div class="item-actions">
                    <button class="btn-edit" data-id="${item.id}">Edit</button>
                </div>
            `;

        div.querySelector(".btn-edit").addEventListener("click", () => {
          toggleEditForm(item.id, true);
        });

        return div;
      }

      // Create edit form
      function createEditForm(item) {
        const div = document.createElement("div");
        div.className = "item-edit-form";

        div.innerHTML = `
                <form class="edit-form-content" data-id="${item.id}">
                    <div class="form-group">
                        <label for="name-${item.id}">Name</label>
                        <input 
                            type="text" 
                            id="name-${item.id}" 
                            class="edit-name" 
                            value="${escapeHtml(item.name)}"
                            maxlength="80"
                        >
                        <div class="error-message error-name"></div>
                    </div>

                    <div class="form-group">
                        <label for="price-${item.id}">Price</label>
                        <input 
                            type="number" 
                            id="price-${item.id}" 
                            class="edit-price" 
                            value="${parseFloat(item.price).toFixed(2)}"
                            step="0.01"
                            min="0"
                        >
                        <div class="error-message error-price"></div>
                    </div>

                    <div class="form-group">
                        <label for="description-${item.id}">Description</label>
                        <textarea 
                            id="description-${item.id}" 
                            class="edit-description"
                            maxlength="300"
                        >${escapeHtml(item.description)}</textarea>
                        <div class="error-message error-description"></div>
                    </div>

                    <div class="form-actions">
                        <button type="button" class="btn-save" data-id="${item.id}">Save</button>
                        <button type="button" class="btn-cancel" data-id="${item.id}">Cancel</button>
                    </div>
                </form>
            `;

        const form = div.querySelector("form");
        const saveBtn = form.querySelector(".btn-save");
        const cancelBtn = form.querySelector(".btn-cancel");

        saveBtn.addEventListener("click", (e) => {
          e.preventDefault();
          saveItem(item.id, form);
        });

        cancelBtn.addEventListener("click", (e) => {
          e.preventDefault();
          toggleEditForm(item.id, false);
        });

        return div;
      }

      // Toggle edit form visibility
      function toggleEditForm(itemId, show) {
        const card = document.getElementById(`item-${itemId}`);
        const displayView = card.querySelector(".item-display");
        const editForm = card.querySelector(".item-edit-form");

        if (show) {
          displayView.classList.add("hidden");
          editForm.classList.add("active");
        } else {
          displayView.classList.remove("hidden");
          editForm.classList.remove("active");
          // Clear error messages
          editForm.querySelectorAll(".error-message").forEach((msg) => {
            msg.classList.remove("show");
            msg.textContent = "";
          });
        }
      }

      // Save item
      function saveItem(itemId, form) {
        const nameInput = form.querySelector(".edit-name");
        const priceInput = form.querySelector(".edit-price");
        const descriptionInput = form.querySelector(".edit-description");

        const nameError = form.querySelector(".error-name");
        const priceError = form.querySelector(".error-price");
        const descriptionError = form.querySelector(".error-description");

        // Clear previous errors
        [nameError, priceError, descriptionError].forEach((msg) => {
          msg.classList.remove("show");
          msg.textContent = "";
        });

        // Validate
        let isValid = true;

        const name = nameInput.value.trim();
        if (!name) {
          nameError.textContent = "Name is required";
          nameError.classList.add("show");
          isValid = false;
        } else if (name.length > 80) {
          nameError.textContent = "Name must not exceed 80 characters";
          nameError.classList.add("show");
          isValid = false;
        }

        const price = parseFloat(priceInput.value);
        if (isNaN(price) || price <= 0) {
          priceError.textContent = "Price must be a valid positive number";
          priceError.classList.add("show");
          isValid = false;
        }

        const description = descriptionInput.value.trim();
        if (description.length > 300) {
          descriptionError.textContent =
            "Description must not exceed 300 characters";
          descriptionError.classList.add("show");
          isValid = false;
        }

        if (!isValid) {
          return;
        }

        // Update data
        const item = menuData.find((i) => i.id === itemId);
        if (item) {
          item.name = name;
          item.price = price;
          item.description = description;

          // Save to localStorage
          saveToLocalStorage();

          // Re-render to update display
          renderMenu();
        }
      }

      // Setup search listener
      function setupSearchListener() {
        const searchInput = document.getElementById("searchInput");
        searchInput.addEventListener("keyup", () => {
          const query = searchInput.value.toLowerCase();
          filterMenu(query);
        });
      }

      // Filter menu
      function filterMenu(query) {
        menuData.forEach((item) => {
          const card = document.getElementById(`item-${item.id}`);
          const matches =
            item.name.toLowerCase().includes(query) ||
            item.description.toLowerCase().includes(query) ||
            item.category.toLowerCase().includes(query);

          card.classList.toggle("hidden", !matches);
        });
      }

      // Escape HTML
      function escapeHtml(text) {
        const map = {
          "&": "&amp;",
          "<": "&lt;",
          ">": "&gt;",
          '"': "&quot;",
          "'": "&#039;",
        };
        return text.replace(/[&<>"']/g, (m) => map[m]);
      }

      // Start
      init();
    </script>
  </body>
</html>
```

- AGENT MEMORY comment on line 1 confirms rule comprehension
- Complete single-file HTML with inline CSS and JavaScript
- Data layer uses array of objects with {id, name, price, description, category}
- localStorage read on page load with graceful merge and fallback to defaults
-

```


## License: unknown
https://github.com/patadejaguar/safeosms/blob/00eea711c344066d444ff8ca85b4f5bb2c217ea8/tools/simplerisk/js/common.js

```

```html
<!-- RULE CHECK: T1✓ T2✓ T3✓ T4✓ T5✓ T6✓ T7✓ T8✓ O1✓ O2✓ O4✓ -->
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Restaurant Menu Admin</title>
    <style>
      * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }

      body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        background-color: #f5f5f5;
        padding: 20px;
      }

      .container {
        max-width: 1200px;
        margin: 0 auto;
      }

      h1 {
        margin-bottom: 30px;
        color: #333;
      }

      .search-section {
        margin-bottom: 30px;
      }

      .search-input {
        width: 100%;
        max-width: 400px;
        padding: 12px;
        font-size: 16px;
        border: 1px solid #ddd;
        border-radius: 4px;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      }

      .search-input:focus {
        outline: none;
        border-color: #4caf50;
        box-shadow: 0 0 5px rgba(76, 175, 80, 0.3);
      }

      .menu-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
        gap: 20px;
      }

      .menu-item {
        background: white;
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 20px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        transition: box-shadow 0.3s ease;
      }

      .menu-item:hover {
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
      }

      .menu-item.hidden {
        display: none;
      }

      .item-display {
        display: block;
      }

      .item-display.hidden {
        display: none;
      }

      .item-edit-form {
        display: none;
      }

      .item-edit-form.active {
        display: block;
      }

      .item-category {
        font-size: 12px;
        color: #888;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 8px;
      }

      .item-name {
        font-size: 20px;
        font-weight: bold;
        color: #333;
        margin-bottom: 8px;
      }

      .item-price {
        font-size: 18px;
        color: #4caf50;
        font-weight: bold;
        margin-bottom: 12px;
      }

      .item-description {
        font-size: 14px;
        color: #666;
        line-height: 1.5;
        margin-bottom: 16px;
      }

      .item-actions {
        display: flex;
        gap: 10px;
      }

      button {
        padding: 10px 16px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        font-size: 14px;
        font-weight: 500;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        transition: background-color 0.3s ease;
      }

      .btn-edit {
        background-color: #2196f3;
        color: white;
      }

      .btn-edit:hover {
        background-color: #1976d2;
      }

      .btn-save {
        background-color: #4caf50;
        color: white;
      }

      .btn-save:hover {
        background-color: #388e3c;
      }

      .btn-cancel {
        background-color: #f44336;
        color: white;
      }

      .btn-cancel:hover {
        background-color: #d32f2f;
      }

      .form-group {
        margin-bottom: 16px;
      }

      .form-group label {
        display: block;
        margin-bottom: 6px;
        font-weight: 500;
        color: #333;
        font-size: 14px;
      }

      .form-group input,
      .form-group textarea {
        width: 100%;
        padding: 10px;
        border: 1px solid #ddd;
        border-radius: 4px;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        font-size: 14px;
      }

      .form-group input:focus,
      .form-group textarea:focus {
        outline: none;
        border-color: #2196f3;
        box-shadow: 0 0 5px rgba(33, 150, 243, 0.3);
      }

      .form-group textarea {
        resize: vertical;
        min-height: 100px;
      }

      .error-message {
        color: #d32f2f;
        font-size: 12px;
        margin-top: 4px;
        display: none;
      }

      .error-message.show {
        display: block;
      }

      .form-actions {
        display: flex;
        gap: 10px;
        margin-top: 16px;
      }

      .form-actions button {
        flex: 1;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <h1>Restaurant Menu Admin</h1>

      <div class="search-section">
        <input
          type="text"
          class="search-input"
          id="searchInput"
          placeholder="Search by name, description, or category..."
        />
      </div>

      <div class="menu-grid" id="menuGrid"></div>
    </div>

    <script>
      // Default menu data
      const defaultMenuData = [
        {
          id: 1,
          name: "Grilled Salmon",
          price: 24.99,
          description:
            "Fresh grilled salmon fillet served with seasonal vegetables and lemon butter sauce",
          category: "Main Courses",
        },
        {
          id: 2,
          name: "Margherita Pizza",
          price: 14.99,
          description:
            "Classic pizza with fresh mozzarella, basil, and tomato sauce on thin crust",
          category: "Pizzas",
        },
        {
          id: 3,
          name: "Caesar Salad",
          price: 12.99,
          description:
            "Crisp romaine lettuce, parmesan cheese, croutons, and creamy caesar dressing",
          category: "Salads",
        },
        {
          id: 4,
          name: "Ribeye Steak",
          price: 32.99,
          description:
            "Premium 12oz ribeye steak with garlic mashed potatoes and grilled asparagus",
          category: "Main Courses",
        },
        {
          id: 5,
          name: "Tiramisu",
          price: 8.99,
          description:
            "Traditional Italian dessert with layers of mascarpone cream and espresso-soaked ladyfingers",
          category: "Desserts",
        },
        {
          id: 6,
          name: "Mushroom Risotto",
          price: 16.99,
          description:
            "Creamy arborio rice with wild mushrooms, peas, and aged parmesan",
          category: "Vegetarian",
        },
      ];

      let menuData = [];

      // Initialize
      function init() {
        loadFromLocalStorage();
        renderMenu();
        setupSearchListener();
      }

      // Load from localStorage
      function loadFromLocalStorage() {
        const saved = localStorage.getItem("menuData");
        if (saved) {
          try {
            const parsedData = JSON.parse(saved);
            // Merge saved data with defaults
            menuData = defaultMenuData.map((item) => {
              const savedItem = parsedData.find((s) => s.id === item.id);
              return savedItem || item;
            });
          } catch (e) {
            menuData = JSON.parse(JSON.stringify(defaultMenuData));
          }
        } else {
          menuData = JSON.parse(JSON.stringify(defaultMenuData));
        }
      }

      // Save to localStorage
      function saveToLocalStorage() {
        localStorage.setItem("menuData", JSON.stringify(menuData));
      }

      // Render menu
      function renderMenu() {
        const grid = document.getElementById("menuGrid");
        grid.innerHTML = "";

        menuData.forEach((item) => {
          const card = createItemCard(item);
          grid.appendChild(card);
        });
      }

      // Create item card
      function createItemCard(item) {
        const div = document.createElement("div");
        div.className = "menu-item";
        div.id = `item-${item.id}`;

        const displayView = createDisplayView(item);
        const editForm = createEditForm(item);

        div.appendChild(displayView);
        div.appendChild(editForm);

        return div;
      }

      // Create display view
      function createDisplayView(item) {
        const div = document.createElement("div");
        div.className = "item-display";

        div.innerHTML = `
                <div class="item-category">${item.category}</div>
                <div class="item-name">${escapeHtml(item.name)}</div>
                <div class="item-price">$${parseFloat(item.price).toFixed(2)}</div>
                <div class="item-description">${escapeHtml(item.description)}</div>
                <div class="item-actions">
                    <button class="btn-edit" data-id="${item.id}">Edit</button>
                </div>
            `;

        div.querySelector(".btn-edit").addEventListener("click", () => {
          toggleEditForm(item.id, true);
        });

        return div;
      }

      // Create edit form
      function createEditForm(item) {
        const div = document.createElement("div");
        div.className = "item-edit-form";

        div.innerHTML = `
                <form class="edit-form-content" data-id="${item.id}">
                    <div class="form-group">
                        <label for="name-${item.id}">Name</label>
                        <input 
                            type="text" 
                            id="name-${item.id}" 
                            class="edit-name" 
                            value="${escapeHtml(item.name)}"
                            maxlength="80"
                        >
                        <div class="error-message error-name"></div>
                    </div>

                    <div class="form-group">
                        <label for="price-${item.id}">Price</label>
                        <input 
                            type="number" 
                            id="price-${item.id}" 
                            class="edit-price" 
                            value="${parseFloat(item.price).toFixed(2)}"
                            step="0.01"
                            min="0"
                        >
                        <div class="error-message error-price"></div>
                    </div>

                    <div class="form-group">
                        <label for="description-${item.id}">Description</label>
                        <textarea 
                            id="description-${item.id}" 
                            class="edit-description"
                            maxlength="300"
                        >${escapeHtml(item.description)}</textarea>
                        <div class="error-message error-description"></div>
                    </div>

                    <div class="form-actions">
                        <button type="button" class="btn-save" data-id="${item.id}">Save</button>
                        <button type="button" class="btn-cancel" data-id="${item.id}">Cancel</button>
                    </div>
                </form>
            `;

        const form = div.querySelector("form");
        const saveBtn = form.querySelector(".btn-save");
        const cancelBtn = form.querySelector(".btn-cancel");

        saveBtn.addEventListener("click", (e) => {
          e.preventDefault();
          saveItem(item.id, form);
        });

        cancelBtn.addEventListener("click", (e) => {
          e.preventDefault();
          toggleEditForm(item.id, false);
        });

        return div;
      }

      // Toggle edit form visibility
      function toggleEditForm(itemId, show) {
        const card = document.getElementById(`item-${itemId}`);
        const displayView = card.querySelector(".item-display");
        const editForm = card.querySelector(".item-edit-form");

        if (show) {
          displayView.classList.add("hidden");
          editForm.classList.add("active");
        } else {
          displayView.classList.remove("hidden");
          editForm.classList.remove("active");
          // Clear error messages
          editForm.querySelectorAll(".error-message").forEach((msg) => {
            msg.classList.remove("show");
            msg.textContent = "";
          });
        }
      }

      // Save item
      function saveItem(itemId, form) {
        const nameInput = form.querySelector(".edit-name");
        const priceInput = form.querySelector(".edit-price");
        const descriptionInput = form.querySelector(".edit-description");

        const nameError = form.querySelector(".error-name");
        const priceError = form.querySelector(".error-price");
        const descriptionError = form.querySelector(".error-description");

        // Clear previous errors
        [nameError, priceError, descriptionError].forEach((msg) => {
          msg.classList.remove("show");
          msg.textContent = "";
        });

        // Validate
        let isValid = true;

        const name = nameInput.value.trim();
        if (!name) {
          nameError.textContent = "Name is required";
          nameError.classList.add("show");
          isValid = false;
        } else if (name.length > 80) {
          nameError.textContent = "Name must not exceed 80 characters";
          nameError.classList.add("show");
          isValid = false;
        }

        const price = parseFloat(priceInput.value);
        if (isNaN(price) || price <= 0) {
          priceError.textContent = "Price must be a valid positive number";
          priceError.classList.add("show");
          isValid = false;
        }

        const description = descriptionInput.value.trim();
        if (description.length > 300) {
          descriptionError.textContent =
            "Description must not exceed 300 characters";
          descriptionError.classList.add("show");
          isValid = false;
        }

        if (!isValid) {
          return;
        }

        // Update data
        const item = menuData.find((i) => i.id === itemId);
        if (item) {
          item.name = name;
          item.price = price;
          item.description = description;

          // Save to localStorage
          saveToLocalStorage();

          // Re-render to update display
          renderMenu();
        }
      }

      // Setup search listener
      function setupSearchListener() {
        const searchInput = document.getElementById("searchInput");
        searchInput.addEventListener("keyup", () => {
          const query = searchInput.value.toLowerCase();
          filterMenu(query);
        });
      }

      // Filter menu
      function filterMenu(query) {
        menuData.forEach((item) => {
          const card = document.getElementById(`item-${item.id}`);
          const matches =
            item.name.toLowerCase().includes(query) ||
            item.description.toLowerCase().includes(query) ||
            item.category.toLowerCase().includes(query);

          card.classList.toggle("hidden", !matches);
        });
      }

      // Escape HTML
      function escapeHtml(text) {
        const map = {
          "&": "&amp;",
          "<": "&lt;",
          ">": "&gt;",
          '"': "&quot;",
          "'": "&#039;",
        };
        return text.replace(/[&<>"']/g, (m) => map[m]);
      }

      // Start
      init();
    </script>
  </body>
</html>
```

- AGENT MEMORY comment on line 1 confirms rule comprehension
- Complete single-file HTML with inline CSS and JavaScript
- Data layer uses array of objects with {id, name, price, description, category}
- localStorage

```


## License: unknown
https://github.com/spicecrm/spicecrm/blob/9fc9f2fe1504f2b8f3823adcb24a8416d5741f7d/src/systemcomponents/components/systemwrappedtext.ts

```

```html
<!-- RULE CHECK: T1✓ T2✓ T3✓ T4✓ T5✓ T6✓ T7✓ T8✓ O1✓ O2✓ O4✓ -->
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Restaurant Menu Admin</title>
    <style>
      * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }

      body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        background-color: #f5f5f5;
        padding: 20px;
      }

      .container {
        max-width: 1200px;
        margin: 0 auto;
      }

      h1 {
        margin-bottom: 30px;
        color: #333;
      }

      .search-section {
        margin-bottom: 30px;
      }

      .search-input {
        width: 100%;
        max-width: 400px;
        padding: 12px;
        font-size: 16px;
        border: 1px solid #ddd;
        border-radius: 4px;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      }

      .search-input:focus {
        outline: none;
        border-color: #4caf50;
        box-shadow: 0 0 5px rgba(76, 175, 80, 0.3);
      }

      .menu-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
        gap: 20px;
      }

      .menu-item {
        background: white;
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 20px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        transition: box-shadow 0.3s ease;
      }

      .menu-item:hover {
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
      }

      .menu-item.hidden {
        display: none;
      }

      .item-display {
        display: block;
      }

      .item-display.hidden {
        display: none;
      }

      .item-edit-form {
        display: none;
      }

      .item-edit-form.active {
        display: block;
      }

      .item-category {
        font-size: 12px;
        color: #888;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 8px;
      }

      .item-name {
        font-size: 20px;
        font-weight: bold;
        color: #333;
        margin-bottom: 8px;
      }

      .item-price {
        font-size: 18px;
        color: #4caf50;
        font-weight: bold;
        margin-bottom: 12px;
      }

      .item-description {
        font-size: 14px;
        color: #666;
        line-height: 1.5;
        margin-bottom: 16px;
      }

      .item-actions {
        display: flex;
        gap: 10px;
      }

      button {
        padding: 10px 16px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        font-size: 14px;
        font-weight: 500;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        transition: background-color 0.3s ease;
      }

      .btn-edit {
        background-color: #2196f3;
        color: white;
      }

      .btn-edit:hover {
        background-color: #1976d2;
      }

      .btn-save {
        background-color: #4caf50;
        color: white;
      }

      .btn-save:hover {
        background-color: #388e3c;
      }

      .btn-cancel {
        background-color: #f44336;
        color: white;
      }

      .btn-cancel:hover {
        background-color: #d32f2f;
      }

      .form-group {
        margin-bottom: 16px;
      }

      .form-group label {
        display: block;
        margin-bottom: 6px;
        font-weight: 500;
        color: #333;
        font-size: 14px;
      }

      .form-group input,
      .form-group textarea {
        width: 100%;
        padding: 10px;
        border: 1px solid #ddd;
        border-radius: 4px;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        font-size: 14px;
      }

      .form-group input:focus,
      .form-group textarea:focus {
        outline: none;
        border-color: #2196f3;
        box-shadow: 0 0 5px rgba(33, 150, 243, 0.3);
      }

      .form-group textarea {
        resize: vertical;
        min-height: 100px;
      }

      .error-message {
        color: #d32f2f;
        font-size: 12px;
        margin-top: 4px;
        display: none;
      }

      .error-message.show {
        display: block;
      }

      .form-actions {
        display: flex;
        gap: 10px;
        margin-top: 16px;
      }

      .form-actions button {
        flex: 1;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <h1>Restaurant Menu Admin</h1>

      <div class="search-section">
        <input
          type="text"
          class="search-input"
          id="searchInput"
          placeholder="Search by name, description, or category..."
        />
      </div>

      <div class="menu-grid" id="menuGrid"></div>
    </div>

    <script>
      // Default menu data
      const defaultMenuData = [
        {
          id: 1,
          name: "Grilled Salmon",
          price: 24.99,
          description:
            "Fresh grilled salmon fillet served with seasonal vegetables and lemon butter sauce",
          category: "Main Courses",
        },
        {
          id: 2,
          name: "Margherita Pizza",
          price: 14.99,
          description:
            "Classic pizza with fresh mozzarella, basil, and tomato sauce on thin crust",
          category: "Pizzas",
        },
        {
          id: 3,
          name: "Caesar Salad",
          price: 12.99,
          description:
            "Crisp romaine lettuce, parmesan cheese, croutons, and creamy caesar dressing",
          category: "Salads",
        },
        {
          id: 4,
          name: "Ribeye Steak",
          price: 32.99,
          description:
            "Premium 12oz ribeye steak with garlic mashed potatoes and grilled asparagus",
          category: "Main Courses",
        },
        {
          id: 5,
          name: "Tiramisu",
          price: 8.99,
          description:
            "Traditional Italian dessert with layers of mascarpone cream and espresso-soaked ladyfingers",
          category: "Desserts",
        },
        {
          id: 6,
          name: "Mushroom Risotto",
          price: 16.99,
          description:
            "Creamy arborio rice with wild mushrooms, peas, and aged parmesan",
          category: "Vegetarian",
        },
      ];

      let menuData = [];

      // Initialize
      function init() {
        loadFromLocalStorage();
        renderMenu();
        setupSearchListener();
      }

      // Load from localStorage
      function loadFromLocalStorage() {
        const saved = localStorage.getItem("menuData");
        if (saved) {
          try {
            const parsedData = JSON.parse(saved);
            // Merge saved data with defaults
            menuData = defaultMenuData.map((item) => {
              const savedItem = parsedData.find((s) => s.id === item.id);
              return savedItem || item;
            });
          } catch (e) {
            menuData = JSON.parse(JSON.stringify(defaultMenuData));
          }
        } else {
          menuData = JSON.parse(JSON.stringify(defaultMenuData));
        }
      }

      // Save to localStorage
      function saveToLocalStorage() {
        localStorage.setItem("menuData", JSON.stringify(menuData));
      }

      // Render menu
      function renderMenu() {
        const grid = document.getElementById("menuGrid");
        grid.innerHTML = "";

        menuData.forEach((item) => {
          const card = createItemCard(item);
          grid.appendChild(card);
        });
      }

      // Create item card
      function createItemCard(item) {
        const div = document.createElement("div");
        div.className = "menu-item";
        div.id = `item-${item.id}`;

        const displayView = createDisplayView(item);
        const editForm = createEditForm(item);

        div.appendChild(displayView);
        div.appendChild(editForm);

        return div;
      }

      // Create display view
      function createDisplayView(item) {
        const div = document.createElement("div");
        div.className = "item-display";

        div.innerHTML = `
                <div class="item-category">${item.category}</div>
                <div class="item-name">${escapeHtml(item.name)}</div>
                <div class="item-price">$${parseFloat(item.price).toFixed(2)}</div>
                <div class="item-description">${escapeHtml(item.description)}</div>
                <div class="item-actions">
                    <button class="btn-edit" data-id="${item.id}">Edit</button>
                </div>
            `;

        div.querySelector(".btn-edit").addEventListener("click", () => {
          toggleEditForm(item.id, true);
        });

        return div;
      }

      // Create edit form
      function createEditForm(item) {
        const div = document.createElement("div");
        div.className = "item-edit-form";

        div.innerHTML = `
                <form class="edit-form-content" data-id="${item.id}">
                    <div class="form-group">
                        <label for="name-${item.id}">Name</label>
                        <input 
                            type="text" 
                            id="name-${item.id}" 
                            class="edit-name" 
                            value="${escapeHtml(item.name)}"
                            maxlength="80"
                        >
                        <div class="error-message error-name"></div>
                    </div>

                    <div class="form-group">
                        <label for="price-${item.id}">Price</label>
                        <input 
                            type="number" 
                            id="price-${item.id}" 
                            class="edit-price" 
                            value="${parseFloat(item.price).toFixed(2)}"
                            step="0.01"
                            min="0"
                        >
                        <div class="error-message error-price"></div>
                    </div>

                    <div class="form-group">
                        <label for="description-${item.id}">Description</label>
                        <textarea 
                            id="description-${item.id}" 
                            class="edit-description"
                            maxlength="300"
                        >${escapeHtml(item.description)}</textarea>
                        <div class="error-message error-description"></div>
                    </div>

                    <div class="form-actions">
                        <button type="button" class="btn-save" data-id="${item.id}">Save</button>
                        <button type="button" class="btn-cancel" data-id="${item.id}">Cancel</button>
                    </div>
                </form>
            `;

        const form = div.querySelector("form");
        const saveBtn = form.querySelector(".btn-save");
        const cancelBtn = form.querySelector(".btn-cancel");

        saveBtn.addEventListener("click", (e) => {
          e.preventDefault();
          saveItem(item.id, form);
        });

        cancelBtn.addEventListener("click", (e) => {
          e.preventDefault();
          toggleEditForm(item.id, false);
        });

        return div;
      }

      // Toggle edit form visibility
      function toggleEditForm(itemId, show) {
        const card = document.getElementById(`item-${itemId}`);
        const displayView = card.querySelector(".item-display");
        const editForm = card.querySelector(".item-edit-form");

        if (show) {
          displayView.classList.add("hidden");
          editForm.classList.add("active");
        } else {
          displayView.classList.remove("hidden");
          editForm.classList.remove("active");
          // Clear error messages
          editForm.querySelectorAll(".error-message").forEach((msg) => {
            msg.classList.remove("show");
            msg.textContent = "";
          });
        }
      }

      // Save item
      function saveItem(itemId, form) {
        const nameInput = form.querySelector(".edit-name");
        const priceInput = form.querySelector(".edit-price");
        const descriptionInput = form.querySelector(".edit-description");

        const nameError = form.querySelector(".error-name");
        const priceError = form.querySelector(".error-price");
        const descriptionError = form.querySelector(".error-description");

        // Clear previous errors
        [nameError, priceError, descriptionError].forEach((msg) => {
          msg.classList.remove("show");
          msg.textContent = "";
        });

        // Validate
        let isValid = true;

        const name = nameInput.value.trim();
        if (!name) {
          nameError.textContent = "Name is required";
          nameError.classList.add("show");
          isValid = false;
        } else if (name.length > 80) {
          nameError.textContent = "Name must not exceed 80 characters";
          nameError.classList.add("show");
          isValid = false;
        }

        const price = parseFloat(priceInput.value);
        if (isNaN(price) || price <= 0) {
          priceError.textContent = "Price must be a valid positive number";
          priceError.classList.add("show");
          isValid = false;
        }

        const description = descriptionInput.value.trim();
        if (description.length > 300) {
          descriptionError.textContent =
            "Description must not exceed 300 characters";
          descriptionError.classList.add("show");
          isValid = false;
        }

        if (!isValid) {
          return;
        }

        // Update data
        const item = menuData.find((i) => i.id === itemId);
        if (item) {
          item.name = name;
          item.price = price;
          item.description = description;

          // Save to localStorage
          saveToLocalStorage();

          // Re-render to update display
          renderMenu();
        }
      }

      // Setup search listener
      function setupSearchListener() {
        const searchInput = document.getElementById("searchInput");
        searchInput.addEventListener("keyup", () => {
          const query = searchInput.value.toLowerCase();
          filterMenu(query);
        });
      }

      // Filter menu
      function filterMenu(query) {
        menuData.forEach((item) => {
          const card = document.getElementById(`item-${item.id}`);
          const matches =
            item.name.toLowerCase().includes(query) ||
            item.description.toLowerCase().includes(query) ||
            item.category.toLowerCase().includes(query);

          card.classList.toggle("hidden", !matches);
        });
      }

      // Escape HTML
      function escapeHtml(text) {
        const map = {
          "&": "&amp;",
          "<": "&lt;",
          ">": "&gt;",
          '"': "&quot;",
          "'": "&#039;",
        };
        return text.replace(/[&<>"']/g, (m) => map[m]);
      }

      // Start
      init();
    </script>
  </body>
</html>
```

- AGENT MEMORY comment on line 1 confirms rule comprehension
- Complete single-file HTML with inline CSS and JavaScript
- Data layer uses array of objects with {id, name, price, description, category}
- localStorage read on page load with graceful merge and fallback to defaults
-

```


## License: unknown
https://github.com/oosor/spirit/blob/74ec6f290699313786835f3a0b6702e929202802/resources/assets/js/view-greek-ru.js

```

```html
<!-- RULE CHECK: T1✓ T2✓ T3✓ T4✓ T5✓ T6✓ T7✓ T8✓ O1✓ O2✓ O4✓ -->
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Restaurant Menu Admin</title>
    <style>
      * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }

      body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        background-color: #f5f5f5;
        padding: 20px;
      }

      .container {
        max-width: 1200px;
        margin: 0 auto;
      }

      h1 {
        margin-bottom: 30px;
        color: #333;
      }

      .search-section {
        margin-bottom: 30px;
      }

      .search-input {
        width: 100%;
        max-width: 400px;
        padding: 12px;
        font-size: 16px;
        border: 1px solid #ddd;
        border-radius: 4px;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      }

      .search-input:focus {
        outline: none;
        border-color: #4caf50;
        box-shadow: 0 0 5px rgba(76, 175, 80, 0.3);
      }

      .menu-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
        gap: 20px;
      }

      .menu-item {
        background: white;
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 20px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        transition: box-shadow 0.3s ease;
      }

      .menu-item:hover {
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
      }

      .menu-item.hidden {
        display: none;
      }

      .item-display {
        display: block;
      }

      .item-display.hidden {
        display: none;
      }

      .item-edit-form {
        display: none;
      }

      .item-edit-form.active {
        display: block;
      }

      .item-category {
        font-size: 12px;
        color: #888;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 8px;
      }

      .item-name {
        font-size: 20px;
        font-weight: bold;
        color: #333;
        margin-bottom: 8px;
      }

      .item-price {
        font-size: 18px;
        color: #4caf50;
        font-weight: bold;
        margin-bottom: 12px;
      }

      .item-description {
        font-size: 14px;
        color: #666;
        line-height: 1.5;
        margin-bottom: 16px;
      }

      .item-actions {
        display: flex;
        gap: 10px;
      }

      button {
        padding: 10px 16px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        font-size: 14px;
        font-weight: 500;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        transition: background-color 0.3s ease;
      }

      .btn-edit {
        background-color: #2196f3;
        color: white;
      }

      .btn-edit:hover {
        background-color: #1976d2;
      }

      .btn-save {
        background-color: #4caf50;
        color: white;
      }

      .btn-save:hover {
        background-color: #388e3c;
      }

      .btn-cancel {
        background-color: #f44336;
        color: white;
      }

      .btn-cancel:hover {
        background-color: #d32f2f;
      }

      .form-group {
        margin-bottom: 16px;
      }

      .form-group label {
        display: block;
        margin-bottom: 6px;
        font-weight: 500;
        color: #333;
        font-size: 14px;
      }

      .form-group input,
      .form-group textarea {
        width: 100%;
        padding: 10px;
        border: 1px solid #ddd;
        border-radius: 4px;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        font-size: 14px;
      }

      .form-group input:focus,
      .form-group textarea:focus {
        outline: none;
        border-color: #2196f3;
        box-shadow: 0 0 5px rgba(33, 150, 243, 0.3);
      }

      .form-group textarea {
        resize: vertical;
        min-height: 100px;
      }

      .error-message {
        color: #d32f2f;
        font-size: 12px;
        margin-top: 4px;
        display: none;
      }

      .error-message.show {
        display: block;
      }

      .form-actions {
        display: flex;
        gap: 10px;
        margin-top: 16px;
      }

      .form-actions button {
        flex: 1;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <h1>Restaurant Menu Admin</h1>

      <div class="search-section">
        <input
          type="text"
          class="search-input"
          id="searchInput"
          placeholder="Search by name, description, or category..."
        />
      </div>

      <div class="menu-grid" id="menuGrid"></div>
    </div>

    <script>
      // Default menu data
      const defaultMenuData = [
        {
          id: 1,
          name: "Grilled Salmon",
          price: 24.99,
          description:
            "Fresh grilled salmon fillet served with seasonal vegetables and lemon butter sauce",
          category: "Main Courses",
        },
        {
          id: 2,
          name: "Margherita Pizza",
          price: 14.99,
          description:
            "Classic pizza with fresh mozzarella, basil, and tomato sauce on thin crust",
          category: "Pizzas",
        },
        {
          id: 3,
          name: "Caesar Salad",
          price: 12.99,
          description:
            "Crisp romaine lettuce, parmesan cheese, croutons, and creamy caesar dressing",
          category: "Salads",
        },
        {
          id: 4,
          name: "Ribeye Steak",
          price: 32.99,
          description:
            "Premium 12oz ribeye steak with garlic mashed potatoes and grilled asparagus",
          category: "Main Courses",
        },
        {
          id: 5,
          name: "Tiramisu",
          price: 8.99,
          description:
            "Traditional Italian dessert with layers of mascarpone cream and espresso-soaked ladyfingers",
          category: "Desserts",
        },
        {
          id: 6,
          name: "Mushroom Risotto",
          price: 16.99,
          description:
            "Creamy arborio rice with wild mushrooms, peas, and aged parmesan",
          category: "Vegetarian",
        },
      ];

      let menuData = [];

      // Initialize
      function init() {
        loadFromLocalStorage();
        renderMenu();
        setupSearchListener();
      }

      // Load from localStorage
      function loadFromLocalStorage() {
        const saved = localStorage.getItem("menuData");
        if (saved) {
          try {
            const parsedData = JSON.parse(saved);
            // Merge saved data with defaults
            menuData = defaultMenuData.map((item) => {
              const savedItem = parsedData.find((s) => s.id === item.id);
              return savedItem || item;
            });
          } catch (e) {
            menuData = JSON.parse(JSON.stringify(defaultMenuData));
          }
        } else {
          menuData = JSON.parse(JSON.stringify(defaultMenuData));
        }
      }

      // Save to localStorage
      function saveToLocalStorage() {
        localStorage.setItem("menuData", JSON.stringify(menuData));
      }

      // Render menu
      function renderMenu() {
        const grid = document.getElementById("menuGrid");
        grid.innerHTML = "";

        menuData.forEach((item) => {
          const card = createItemCard(item);
          grid.appendChild(card);
        });
      }

      // Create item card
      function createItemCard(item) {
        const div = document.createElement("div");
        div.className = "menu-item";
        div.id = `item-${item.id}`;

        const displayView = createDisplayView(item);
        const editForm = createEditForm(item);

        div.appendChild(displayView);
        div.appendChild(editForm);

        return div;
      }

      // Create display view
      function createDisplayView(item) {
        const div = document.createElement("div");
        div.className = "item-display";

        div.innerHTML = `
                <div class="item-category">${item.category}</div>
                <div class="item-name">${escapeHtml(item.name)}</div>
                <div class="item-price">$${parseFloat(item.price).toFixed(2)}</div>
                <div class="item-description">${escapeHtml(item.description)}</div>
                <div class="item-actions">
                    <button class="btn-edit" data-id="${item.id}">Edit</button>
                </div>
            `;

        div.querySelector(".btn-edit").addEventListener("click", () => {
          toggleEditForm(item.id, true);
        });

        return div;
      }

      // Create edit form
      function createEditForm(item) {
        const div = document.createElement("div");
        div.className = "item-edit-form";

        div.innerHTML = `
                <form class="edit-form-content" data-id="${item.id}">
                    <div class="form-group">
                        <label for="name-${item.id}">Name</label>
                        <input 
                            type="text" 
                            id="name-${item.id}" 
                            class="edit-name" 
                            value="${escapeHtml(item.name)}"
                            maxlength="80"
                        >
                        <div class="error-message error-name"></div>
                    </div>

                    <div class="form-group">
                        <label for="price-${item.id}">Price</label>
                        <input 
                            type="number" 
                            id="price-${item.id}" 
                            class="edit-price" 
                            value="${parseFloat(item.price).toFixed(2)}"
                            step="0.01"
                            min="0"
                        >
                        <div class="error-message error-price"></div>
                    </div>

                    <div class="form-group">
                        <label for="description-${item.id}">Description</label>
                        <textarea 
                            id="description-${item.id}" 
                            class="edit-description"
                            maxlength="300"
                        >${escapeHtml(item.description)}</textarea>
                        <div class="error-message error-description"></div>
                    </div>

                    <div class="form-actions">
                        <button type="button" class="btn-save" data-id="${item.id}">Save</button>
                        <button type="button" class="btn-cancel" data-id="${item.id}">Cancel</button>
                    </div>
                </form>
            `;

        const form = div.querySelector("form");
        const saveBtn = form.querySelector(".btn-save");
        const cancelBtn = form.querySelector(".btn-cancel");

        saveBtn.addEventListener("click", (e) => {
          e.preventDefault();
          saveItem(item.id, form);
        });

        cancelBtn.addEventListener("click", (e) => {
          e.preventDefault();
          toggleEditForm(item.id, false);
        });

        return div;
      }

      // Toggle edit form visibility
      function toggleEditForm(itemId, show) {
        const card = document.getElementById(`item-${itemId}`);
        const displayView = card.querySelector(".item-display");
        const editForm = card.querySelector(".item-edit-form");

        if (show) {
          displayView.classList.add("hidden");
          editForm.classList.add("active");
        } else {
          displayView.classList.remove("hidden");
          editForm.classList.remove("active");
          // Clear error messages
          editForm.querySelectorAll(".error-message").forEach((msg) => {
            msg.classList.remove("show");
            msg.textContent = "";
          });
        }
      }

      // Save item
      function saveItem(itemId, form) {
        const nameInput = form.querySelector(".edit-name");
        const priceInput = form.querySelector(".edit-price");
        const descriptionInput = form.querySelector(".edit-description");

        const nameError = form.querySelector(".error-name");
        const priceError = form.querySelector(".error-price");
        const descriptionError = form.querySelector(".error-description");

        // Clear previous errors
        [nameError, priceError, descriptionError].forEach((msg) => {
          msg.classList.remove("show");
          msg.textContent = "";
        });

        // Validate
        let isValid = true;

        const name = nameInput.value.trim();
        if (!name) {
          nameError.textContent = "Name is required";
          nameError.classList.add("show");
          isValid = false;
        } else if (name.length > 80) {
          nameError.textContent = "Name must not exceed 80 characters";
          nameError.classList.add("show");
          isValid = false;
        }

        const price = parseFloat(priceInput.value);
        if (isNaN(price) || price <= 0) {
          priceError.textContent = "Price must be a valid positive number";
          priceError.classList.add("show");
          isValid = false;
        }

        const description = descriptionInput.value.trim();
        if (description.length > 300) {
          descriptionError.textContent =
            "Description must not exceed 300 characters";
          descriptionError.classList.add("show");
          isValid = false;
        }

        if (!isValid) {
          return;
        }

        // Update data
        const item = menuData.find((i) => i.id === itemId);
        if (item) {
          item.name = name;
          item.price = price;
          item.description = description;

          // Save to localStorage
          saveToLocalStorage();

          // Re-render to update display
          renderMenu();
        }
      }

      // Setup search listener
      function setupSearchListener() {
        const searchInput = document.getElementById("searchInput");
        searchInput.addEventListener("keyup", () => {
          const query = searchInput.value.toLowerCase();
          filterMenu(query);
        });
      }

      // Filter menu
      function filterMenu(query) {
        menuData.forEach((item) => {
          const card = document.getElementById(`item-${item.id}`);
          const matches =
            item.name.toLowerCase().includes(query) ||
            item.description.toLowerCase().includes(query) ||
            item.category.toLowerCase().includes(query);

          card.classList.toggle("hidden", !matches);
        });
      }

      // Escape HTML
      function escapeHtml(text) {
        const map = {
          "&": "&amp;",
          "<": "&lt;",
          ">": "&gt;",
          '"': "&quot;",
          "'": "&#039;",
        };
        return text.replace(/[&<>"']/g, (m) => map[m]);
      }

      // Start
      init();
    </script>
  </body>
</html>
```

- AGENT MEMORY comment on line 1 confirms rule comprehension
- Complete single-file HTML with inline CSS and JavaScript
- Data layer uses array of objects with {id, name, price, description, category}
- localStorage read on page load with graceful merge and fallback to defaults
-

```

```
