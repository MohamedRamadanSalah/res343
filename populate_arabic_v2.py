import json
import re

# Load the menu data with full Arabic descriptions
with open('menu_final.json', 'r', encoding='utf-8') as f:
    menu_data = json.load(f)

# Create mapping of item names to Arabic descriptions
item_desc_map = {}

for category, items in menu_data['soho'].items():
    for item in items:
        ar_name = item['name'].strip()
        ar_desc = item.get('desc', '').strip()
        if ar_desc:
            item_desc_map[ar_name] = ar_desc

for category, items in menu_data['istiknanah'].items():
    for item in items:
        ar_name = item['name'].strip()
        ar_desc = item.get('desc', '').strip()
        if ar_desc:
            item_desc_map[ar_name] = ar_desc

print(f"✓ Mapped {len(item_desc_map)} items with Arabic descriptions")

# Read the HTML file
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Process each item
replacement_count = 0
for ar_name, ar_desc in item_desc_map.items():
    # Escape quotes in description
    escaped_desc = ar_desc.replace('"', '\\"')
    
    # Look for this specific item structure and replace empty desc
    # Pattern: ar: { name: "exact_name", desc: "" }
    old_pattern = f'ar: {{ name: "{ar_name}", desc: "" }}'
    new_pattern = f'ar: {{ name: "{ar_name}", desc: "{escaped_desc}" }}'
    
    if old_pattern in html:
        html = html.replace(old_pattern, new_pattern)
        replacement_count += 1

print(f"✓ Updated {replacement_count} menu item descriptions")

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✓ Saved updated HTML")

# Verify by finding a few items with descriptions
print("\nSample of updated items:")
lines = html.split('\n')
for i, line in enumerate(lines):
    if 'ar: { name:' in line and 'desc: "' in line and 'desc: ""' not in line:
        print(f"Line {i+1}: {line.strip()[:100]}...")
        if i > 1850 and i < 1950:  # Just show a few from the first section
            break
