import json

# Load the complete menu data
with open('menu_final.json', 'r', encoding='utf-8') as f:
    menu_data = json.load(f)

# Generate JavaScript code for SOHO menu
soho_js = "      const sohoMenu = {\n"
for category, items in menu_data['soho'].items():
    soho_js += f'        "{category}": [\n'
    for item in items:
        item_name = item['name'].replace('"', '\\"')
        desc = item.get('desc', '').replace('"', '\\"')
        desc_en = item.get('descEn', '').replace('"', '\\"')
        price = item['price']
        
        soho_js += f'''          {{
            name: "{item_name}",
            price: {price},
            desc: "{desc_en}",
            ar: {{
              name: "{item_name}",
              desc: "{desc}"
            }}
          }},
'''
    soho_js += "        ],\n"

soho_js += "      };"

# Generate JavaScript code for ISTIKNANAH menu
istik_js = "      const istikMenu = {\n"
for category, items in menu_data['istiknanah'].items():
    istik_js += f'        "{category}": [\n'
    for item in items:
        item_name = item['name'].replace('"', '\\"')
        desc = item.get('desc', '').replace('"', '\\"')
        desc_en = item.get('descEn', '').replace('"', '\\"')
        price = item['price']
        
        istik_js += f'''          {{
            name: "{item_name}",
            price: {price},
            desc: "{desc_en}",
            ar: {{
              name: "{item_name}",
              desc: "{desc}"
            }}
          }},
'''
    istik_js += "        ],\n"

istik_js += "      };"

# Save to file for inspection
with open('menu_js_output.js', 'w', encoding='utf-8') as f:
    f.write("// SOHO MENU\n")
    f.write(soho_js)
    f.write("\n\n// ISTIKNANAH MENU\n")
    f.write(istik_js)

print("✓ Generated JavaScript menu code")
print(f"✓ SOHO: {sum(len(items) for items in menu_data['soho'].values())} items")
print(f"✓ ISTIKNANAH: {sum(len(items) for items in menu_data['istiknanah'].values())} items")
print("✓ Saved preview to menu_js_output.js")

# Show first few lines of preview
lines = soho_js.split('\n')[:20]
print("\nPreview of SOHO menu structure:")
for line in lines:
    print(line)
