import json
import re

# Load the menu with descriptions
with open('menu_final.json', 'r', encoding='utf-8') as f:
    menu_data = json.load(f)

# Create a mapping of Arabic names to descriptions
ar_to_desc = {}
for category, items in menu_data['soho'].items():
    for item in items:
        ar_name = item['name']
        ar_to_desc[ar_name] = {
            'ar': item.get('desc', ''),
            'en': item.get('descEn', '')
        }

for category, items in menu_data['istiknanah'].items():
    for item in items:
        ar_name = item['name']
        ar_to_desc[ar_name] = {
            'ar': item.get('desc', ''),
            'en': item.get('descEn', '')
        }

print(f"✓ Loaded {len(ar_to_desc)} menu items with descriptions")

# Show some samples
print("\nSample descriptions:")
for i, (ar_name, descs) in enumerate(list(ar_to_desc.items())[:5]):
    print(f"\nAR: {ar_name}")
    print(f"  EN: {descs['en'][:70]}")
    print(f"  AR: {descs['ar'][:70]}")

# Save the mapping
with open('desc_mapping.json', 'w', encoding='utf-8') as f:
    json.dump(ar_to_desc, f, ensure_ascii=False, indent=2)

print(f"\n✓ Saved description mapping to desc_mapping.json")
