import json
import re

# Load the menu data with full Arabic descriptions
with open('menu_final.json', 'r', encoding='utf-8') as f:
    menu_data = json.load(f)

# Create mapping of item names to Arabic descriptions
item_desc_map = {}

for category, items in menu_data['soho'].items():
    for item in items:
        ar_name = item['name']
        ar_desc = item.get('desc', '')
        item_desc_map[ar_name] = ar_desc

for category, items in menu_data['istiknanah'].items():
    for item in items:
        ar_name = item['name']
        ar_desc = item.get('desc', '')
        item_desc_map[ar_name] = ar_desc

print(f"✓ Mapped {len(item_desc_map)} items with Arabic descriptions")

# Read the HTML file
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find and replace all desc: "" with desc: "Arabic description"
# We need to replace within menu items where ar: { name: "Arabic name", desc: "" }

replacement_count = 0

# For each item in the map, find it in HTML and update description
for ar_name, ar_desc in item_desc_map.items():
    # Escape special regex characters
    escaped_name = re.escape(ar_name)
    
    # Pattern to find: ar: { name: "arabic_name", desc: "" }
    pattern = f'ar: \\{{ name: "{escaped_name}", desc: "" \\}}'
    replacement = f'ar: {{ name: "{ar_name}", desc: "{ar_desc.replace('"', '\\"')}" }}'
    
    if pattern in html:
        html = html.replace(pattern, replacement)
        replacement_count += 1

print(f"✓ Updated {replacement_count} menu item descriptions in HTML")

# Write back to HTML
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✓ Saved updated HTML with Arabic descriptions")

# Show sample
print("\nSample updated items:")
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()
    # Find a few items with descriptions
    import re
    items_with_desc = re.findall(r'ar: \{ name: "([^"]+)", desc: "([^"]{20,60})', content)
    for name, desc in items_with_desc[:5]:
        print(f"  • {name}: {desc}...")
