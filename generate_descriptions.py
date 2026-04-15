import json

# Load menu with descriptions
with open('menu_with_descriptions.json', 'r', encoding='utf-8') as f:
    menu_data = json.load(f)

# Description templates for items without descriptions
descriptions = {
    # Beverages
    'مياه معدنيه فلو': {'en': 'Fresh mineral water', 'ar': 'مياه معدنية منعشة'},
    'مياه فواره': {'en': 'Sparkling water with bubbles', 'ar': 'مياه غازية منعشة'},
    'بيبسي \\ سفن اب': {'en': 'Ice-cold soft drink choices', 'ar': 'مشروبات غازية باردة'},
    'بيريل \\شويبس \\ فيروز': {'en': 'Premium carbonated beverages', 'ar': 'مشروبات غازية فاخرة'},
    'ريد بول': {'en': 'Energy drink - cold and refreshing', 'ar': 'مشروب الطاقة البارد والمنعش'},
    'ريد بول اضافة صوص': {'en': 'Red Bull with special sauce twist', 'ar': 'ريد بول مع نكهة صوص خاص'},
    
    # Soups
    'شوربة كريمة الدجاج': {'en': 'Creamy chicken soup with fresh herbs', 'ar': 'شوربة دجاج كريمية مع أعشاب طازة'},
    'شوربة كريمة المشروم': {'en': 'Creamy mushroom soup with aromatic spices', 'ar': 'شوربة الفطر الكريمية مع بهارات العطرية'},
    
    # Salads
    'سيزر سلاد بالدجاج': {'en': 'Classic Caesar salad with grilled chicken', 'ar': 'سلطة سيزر كلاسيكية مع الدجاج المشوى'},
    'سلطة كوب': {'en': 'Crispy salad with grilled chicken, croutons, and Parmesan', 'ar': 'سلطة سيزر بالدجاج المشوى مع الخس وقطع الكرتون وصوص السيزر والجبنة بارميزان'},
    
    # Appetizers
    'تشيكن استربس': {'en': 'Tender crispy chicken strips with your choice of sauce', 'ar': 'قطع دجاج مقرمشة طرية مع اختيارك من الصوصات'},
    'تشيكن وينجز': {'en': 'Tender chicken pieces with honey mustard or buffalo sauce', 'ar': 'قطع دجاج طرية من الداخل ومقرمشة من الخارج مع صوص مستردة بالعسل أو بافلو'},
    'اصابع الموزاريلا': {'en': 'Golden fried mozzarella sticks with melted cheese inside', 'ar': 'اصابع ذهبية مقرمشة تخفى بداخلها جبنة موزاريلا سائحة'},
    'شيبس تشيز': {'en': 'Crispy chips with cheese sauce, pico de gallo and jalapeños', 'ar': 'شيبس مع صوص الجبنة مع سلطة البيكو والهالبينو'},
    
    # Pasta
    'باستا الفريدو': {'en': 'Rich creamy Alfredo pasta with fresh mushrooms and grilled chicken', 'ar': 'باستا الفريدو غنية بصوص كريمي ومشروم طازج مع الدجاج المشوى'},
    'اسباجيتي بلونيز': {'en': 'Traditional Italian spaghetti with rich meat sauce', 'ar': 'سباجيتي بصلصة اللحم الغنية على الطريقة الإيطالية'},
}

# Generate descriptions for items
def generate_descriptions(menu_dict):
    for category, items in menu_dict.items():
        for item in items:
            item_name = item['name']
            
            # If no description, try to find one
            if not item.get('desc'):
                if item_name in descriptions:
                    item['desc'] = descriptions[item_name]['ar']
                    item['descEn'] = descriptions[item_name]['en']
                else:
                    # Generate generic description based on keywords
                    if 'برجر' in item_name:
                        item['desc'] = 'برجر مشوي طازج مع اختياراتك المفضلة'
                        item['descEn'] = 'Freshly grilled burger with your favorite toppings'
                    elif 'دجاج' in item_name or 'تشيكن' in item_name:
                        item['desc'] = 'قطع دجاج طازة مع صوصات منتقاة بعناية'
                        item['descEn'] = 'Fresh chicken pieces with carefully selected sauces'
                    elif 'سلاد' in item_name or 'سلطة' in item_name:
                        item['desc'] = 'سلطة طازة مع خضار منتقاة يومياً'
                        item['descEn'] = 'Fresh salad with daily selected vegetables'
                    elif 'ساندوتش' in item_name or 'sandwich' in item_name.lower():
                        item['desc'] = 'ساندويتش شهي مع حشوة لذيذة'
                        item['descEn'] = 'Delicious sandwich with tasty fillings'
                    else:
                        item['desc'] = 'طبق شهي من أطباقنا الخاصة'
                        item['descEn'] = 'A tasty dish from our special menu'
            else:
                # Add English version if only Arabic exists
                if 'descEn' not in item:
                    item['descEn'] = 'Specialty dish from SOHO'

# Add descriptions to menus
generate_descriptions(menu_data['soho'])
generate_descriptions(menu_data['istiknanah'])

# Save enhanced menu
with open('menu_final.json', 'w', encoding='utf-8') as f:
    json.dump(menu_data, f, ensure_ascii=False, indent=2)

print('✓ Generated descriptions for all items')
print('✓ Saved to menu_final.json')

# Show sample
soho_categories = menu_data['soho']
print('\n' + '='*100)
print('SAMPLE: SOHO - السلطات:')
for item in soho_categories.get('السلطات', []):
    print(f"\n  {item['name']} - {item['price']} EGP")
    print(f"    EN: {item.get('descEn', 'N/A')[:70]}...")
    print(f"    AR: {item.get('desc', 'N/A')[:70]}...")
