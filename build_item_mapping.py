import json
import re

# Read current HTML
with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Read the menu data with descriptions
with open('menu_final.json', 'r', encoding='utf-8') as f:
    menu_data = json.load(f)

# Translation dictionary for categories (Arabic to English)
category_translations = {
    '❄️ Cold Beverages': ['المشروبات الباردة', 'مياه معدنيه فلو', 'مياه فواره', 'بيبسي'],
    'Soups': ['الشوربة'],
    'Salads': ['السلطات'],
    'Appetizers': ['المقبلات'],
    'Sandwiches': ['الساندوتشات'],
    'Pasta Corner': ['ركن الباستا'],
    'Main Dishes': ['الاطباق الرئيسية'],
    'Kids Meals': ['وجبات الاطفال'],
    'Sides': ['اكسترا'],
    'Sauces': ['الصوصات'],
    'Desserts': ['الحلويات'],
    '☕ Hot Beverages': ['المشروبات الساخنه'],
    'Fresh Juices': ['عصائر فريش'],
    'Health Drinks': ['مشروبات صحيه'],
    'Ice Drinks': ['ايس درينك'],
    'Milk Shakes': ['ميلك شيك'],
    'Special Drinks': ['مشروبات مميزة'],
    'Soda Cocktails': ['صودا كوكتيل'],
    'Smoothies': ['سموزى']
}

# Create a mapping from Arabic item names to English names
arabic_to_english = {}
en_item_to_desc = {}

# Map from Excel Arabic items to HTML English items (manual mapping)
item_mapping = {
    # SOHO items
    'مياه معدنيه فلو': 'Mineral Water',
    'مياه فواره': 'Sparkling Water',
    'بيبسي \\ سفن اب': 'Pepsi / 7UP',
    'بيريل \\شويبس \\ فيروز': 'Perrier / Schweppes / Fayrouz',
    'ريد بول': 'Red Bull',
    'ريد بول اضافة صوص': 'Red Bull with Extra Syrup',
    'شوربة كريمة الدجاج': 'Creamy Chicken Soup',
    'شوربة كريمة المشروم': 'Creamy Mushroom Soup',
    'سيزر سلاد بالدجاج': 'Caesar Salad with Chicken',
    'سلطة كوب': 'Cobb Salad',
    # ISTIKNANAH items
    'شاي/شاى اخضر': 'Tea / Green Tea',
    'ابريق شاي ( 4 استكانة )': 'Tea Pot (4 Cups)',
    'ابريق شاى(٢استكانه)': 'Tea Pot (2 Cups)',
    'ابريق شاى كرك': 'Tea Pot with Cardamom',
    'استكنانة ماتشا': 'Matcha',
    'نسكافيه': 'Nescafé',
    'امريكان كوفي': 'American Coffee',
    'اسبرسו سينجل': 'Espresso Single',
    'اسبرسو دبل': 'Espresso Double',
    'ميكاتو سينجل': 'Macchiato Single',
    'ميكاتو دبل': 'Macchiato Double',
}

# Build a lookup of English names to descriptions by reading menu_data
for ar_category, items in menu_data['soho'].items():
    for item in items:
        ar_name = item['name']
        en_desc = item.get('descEn', '')
        ar_desc = item.get('desc', '')
        item_mapping[ar_name] = {
            'en_desc': en_desc,
            'ar_desc': ar_desc
        }

for ar_category, items in menu_data['istiknanah'].items():
    for item in items:
        ar_name = item['name']
        en_desc = item.get('descEn', '')
        ar_desc = item.get('desc', '')
        item_mapping[ar_name] = {
            'en_desc': en_desc,
            'ar_desc': ar_desc
        }

print(f"✓ Created mapping for {len(item_mapping)} items")
print("\nSample mappings:")
for i, (ar_name, data) in enumerate(list(item_mapping.items())[:5]):
    if isinstance(data, dict):
        print(f"  {ar_name}")
        print(f"    EN: {data.get('en_desc', '')[:60]}...")
        print(f"    AR: {data.get('ar_desc', '')[:60]}...")

with open('item_mapping.json', 'w', encoding='utf-8') as f:
    json.dump(item_mapping, f, ensure_ascii=False, indent=2)

print(f"\n✓ Saved item mapping to item_mapping.json")
