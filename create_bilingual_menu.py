#!/usr/bin/env python3
import json

# Create comprehensive bilingual menu with descriptions
bilingual_menu = {
    "soho": {
        "🥤 Cold Beverages": {
            "ar": "🥤 المشروبات الباردة",
            "items": [
                {
                    "en_name": "Still Mineral Water",
                    "ar_name": "مياه معدنية فلو",
                    "en_desc": "Pure & refreshing",
                    "ar_desc": "مياه معدنية طبيعية نقية منعشة",
                    "price": 35
                },
                {
                    "en_name": "Sparkling Water",
                    "ar_name": "مياه فوارة",
                    "en_desc": "Crisp bubbles",
                    "ar_desc": "مياه غازية منعشة بفقاعات حية",
                    "price": 55
                },
                {
                    "en_name": "Pepsi / 7Up",
                    "ar_name": "بيبسي / سفن اب",
                    "en_desc": "Classic soda",
                    "ar_desc": "مشروب غازي كلاسيكي لذيذ",
                    "price": 40
                },
                {
                    "en_name": "Perrier / Schweppes / Fayrouz",
                    "ar_name": "بيريل / شويبس / فيروز",
                    "en_desc": "Premium selection",
                    "ar_desc": "تشكيلة فاخرة من المشروبات المميزة",
                    "price": 45
                },
                {
                    "en_name": "Red Bull",
                    "ar_name": "ريد بول",
                    "en_desc": "Energy boost",
                    "ar_desc": "مشروب طاقة قوي يعطيك الحيوية",
                    "price": 85
                },
                {
                    "en_name": "Red Bull + Sauce Shot",
                    "ar_name": "ريد بول مع شوت صوص",
                    "en_desc": "Extra kick",
                    "ar_desc": "ريد بول بإضافة مميزة لطعم أقوى",
                    "price": 105
                }
            ]
        },
        "🍜 Soups": {
            "ar": "🍜 الشوربات",
            "items": [
                {
                    "en_name": "Creamy Chicken Soup",
                    "ar_name": "شوربة كريمة الدجاج",
                    "en_desc": "Velvety smooth chicken",
                    "ar_desc": "شوربة دجاج كريمية ناعمة وغنية بالنكهة المميزة",
                    "price": 89
                },
                {
                    "en_name": "Creamy Mushroom Soup",
                    "ar_name": "شوربة كريمة المشروم",
                    "en_desc": "Earthy & rich",
                    "ar_desc": "شوربة فطر كريمية لذيذة بطعم عميق وغني",
                    "price": 85
                }
            ]
        },
        "🥗 Salads": {
            "ar": "🥗 السلطات",
            "items": [
                {
                    "en_name": "Caesar Salad with Chicken",
                    "ar_name": "سلطة سيزر بالدجاج المشوى",
                    "en_desc": "Grilled chicken, romaine, croutons, parmesan",
                    "ar_desc": "سلطة سيزر بالدجاج المشوى مع الخس وقطع الكرتون وصوص السيزر والجبنة بارميزان",
                    "price": 169
                },
                {
                    "en_name": "Cobb Salad",
                    "ar_name": "سلطة كوب",
                    "en_desc": "Crispy chicken, egg, bacon, cheese, corn, beans, pico",
                    "ar_desc": "خس مقرمش مع الدجاج المقلى والبيض والبيكون والجبن المشكلة مع الذرة الحلوة والفاصولياء الحمراء والبيكو ديجالو",
                    "price": 209
                },
                {
                    "en_name": "Taco Salad",
                    "ar_name": "سلطة تاكو",
                    "en_desc": "Lettuce, tortilla strips, chicken, bacon, cheese, ranch, beans",
                    "ar_desc": "سلطة الخس وشرائح التورتيلا مع الدجاج المشوى وقطع البيكون والجبنة المكس مغطاة برانش صوص والذرة والفاصولياء الحمراء",
                    "price": 199
                }
            ]
        },
        "🍟 Appetizers": {
            "ar": "🍟 المقبلات",
            "items": [
                {
                    "en_name": "Chicken Strips",
                    "ar_name": "تشيكن استربس",
                    "en_desc": "Crispy outside, tender inside, honey mustard or buffalo",
                    "ar_desc": "قطع دجاج طرية من الداخل ومقرمشة من الخارج مع اختيارك من الصوصات (هنى مسطردة أو بافلو صوص)",
                    "price": 189
                },
                {
                    "en_name": "Chicken Wings",
                    "ar_name": "تشيكن وينجز",
                    "en_desc": "Fried wings with buffalo/BBQ/dynamite sauce",
                    "ar_desc": "أجنحة دجاج مقلية وتقدر تختار صوصك المفضل من البافلو أو الباربيكيو أو صوص الدينميت",
                    "price": 169
                },
                {
                    "en_name": "Mozzarella Sticks",
                    "ar_name": "أصابع الموزاريلا",
                    "en_desc": "Golden with marinara",
                    "ar_desc": "أصابع ذهبية مقرمشة تخفى بداخلها جبنة موزاريلا سايحة ولذيذة، تقدم ساخنة مع صوص الماريناردا",
                    "price": 99
                },
                {
                    "en_name": "Chili Cheese Fries",
                    "ar_name": "شيبس تشيز",
                    "en_desc": "Fries, cheese sauce, pico, jalapeños",
                    "ar_desc": "شيبس مع صوص الجبنة والسلطة الطازجة والهالبينو الحار",
                    "price": 129
                },
                {
                    "en_name": "Soho Chips",
                    "ar_name": "سوهو شيبس",
                    "en_desc": "Crispy chips + signature Soho sauce",
                    "ar_desc": "شيبس كريسبي مع صلصة سوهو الخاصة الجريئة واللذيذة",
                    "price": 110
                },
                {
                    "en_name": "Nacho Land",
                    "ar_name": "ناتشو لاند",
                    "en_desc": "Nachos, melted cheese, jalapeños, sour cream, pico",
                    "ar_desc": "ناتشو مقرمش مع الجبنة الذائبة والهالبينو والقشدة الحامضة والسلطة الطازجة",
                    "price": 149
                },
                {
                    "en_name": "Mac & Cheese",
                    "ar_name": "ماك أند تشيز",
                    "en_desc": "Creamy white sauce pasta, special cheese blend",
                    "ar_desc": "معكرونة طرية مع صوص كريمي ابيض وخليط جبن مميز",
                    "price": 159
                }
            ]
        },
        "🍔 Burgers & Sandwiches": {
            "ar": "🍔 البرجرات والساندويتشات",
            "items": [
                {
                    "en_name": "Brisket Star",
                    "ar_name": "برجر لحم مدخن",
                    "en_desc": "Smoked brisket, cheese sauce, crispy onions, BBQ, pickles, mayo",
                    "ar_desc": "لحم أبقار مدخن بشكل احترافي مع صوص جبن وبصل مقرمش وصوص باربيكيو وخيار مخلل وخردل",
                    "price": 269
                },
                {
                    "en_name": "Steak Sandwich",
                    "ar_name": "ساندويتش الستيك",
                    "en_desc": "Sliced steak, grilled veggies, Soho cheese, smoky sauce",
                    "ar_desc": "شرائح لحم ستيك طازة مع خضار مشوية وجبن سوهو خاص وصوص دخاني",
                    "price": 299
                },
                {
                    "en_name": "Classic Soho Chicken",
                    "ar_name": "الدجاج الكلاسيكي سوهو",
                    "en_desc": "Grilled/fried chicken, Soho sauce, cheddar, lettuce, tomato",
                    "ar_desc": "دجاج مشوي أو مقلي مع صوص سوهو الجريء والجبنة والخس والطماطم الطازجة",
                    "price": 279
                },
                {
                    "en_name": "Chicken Quesadilla",
                    "ar_name": "كويسيديلا الدجاج",
                    "en_desc": "Marinated chicken, grilled veggies, melted cheese, ranch",
                    "ar_desc": "دجاج مخلل طازج مع خضار مشوية وجبنة ذائبة وصوص رانتش ناعم",
                    "price": 289
                },
                {
                    "en_name": "Beef Quesadilla",
                    "ar_name": "كويسيديلا اللحم",
                    "en_desc": "Marinated beef strips, veggies, cheese, ranch",
                    "ar_desc": "شرائح لحم مخللة طازجة مع خضار مشوية وجبنة ذائبة وصوص رانتش",
                    "price": 299
                },
                {
                    "en_name": "Shrimp Quesadilla",
                    "ar_name": "كويسيديلا الجمبري",
                    "en_desc": "Spiced shrimp, grilled veggies, melted cheese, ranch",
                    "ar_desc": "جمبري حار مشوي مع خضار مشوية وجبنة ذائبة وصوص رانتش مميز",
                    "price": 289
                },
                {
                    "en_name": "Classic Burger",
                    "ar_name": "برجر كلاسيكي",
                    "en_desc": "Flame-grilled patty, lettuce, tomato, onion, mayo",
                    "ar_desc": "فطيرة لحم مشوية على اللهب مع خس وطماطم وبصل وخردل",
                    "price": 279
                },
                {
                    "en_name": "Classic Burger Basic",
                    "ar_name": "برجر كلاسيكي (أساسي)",
                    "en_desc": "120g patty, lettuce, tomato, onion, special sauce",
                    "ar_desc": "فطيرة لحم 120 غرام مشوية مع خس وطماطم وبصل وصوص مميز",
                    "price": 209
                },
                {
                    "en_name": "Soho Mushroom Burger",
                    "ar_name": "برجر سوهو بالفطر",
                    "en_desc": "Beef patty, cheese, grilled mushrooms, caramelized onion, smoky mayo",
                    "ar_desc": "لحم بقري مع جبنة وفطر مشوي وبصل بالكراميل وخردل دخاني",
                    "price": 309
                },
                {
                    "en_name": "Soho Mushroom Burger Basic",
                    "ar_name": "برجر سوهو بالفطر (أساسي)",
                    "en_desc": "120g patty, mushrooms, onion, smoky mayo, cheese",
                    "ar_desc": "فطيرة لحم 120 غرام مع فطر وبصل وخردل دخاني وجبنة",
                    "price": 239
                },
                {
                    "en_name": "Bacon Burger",
                    "ar_name": "برجر بيكون",
                    "en_desc": "Patty, cheddar, smoked bacon, caramelized onion, jalapeños, mayo",
                    "ar_desc": "لحم بقري مع جبنة تشيدر وبيكون مدخن وبصل بالكراميل وهالبينو وخردل",
                    "price": 269
                },
                {
                    "en_name": "Bacon Burger Basic",
                    "ar_name": "برجر بيكون (أساسي)",
                    "en_desc": "120g patty, bacon, cheese, jalapeños, mayo",
                    "ar_desc": "فطيرة لحم 120 غرام مع بيكون وجبنة وهالبينو وخردل",
                    "price": 199
                },
                {
                    "en_name": "Texas Burger",
                    "ar_name": "برجر تكساس",
                    "en_desc": "Smoked patty, crispy onion, cheddar, BBQ, smoky mayo",
                    "ar_desc": "لحم بقري مدخن مع بصل مقرمش وجبنة تشيدر وصوص باربيكيو وخردل دخاني",
                    "price": 299
                },
                {
                    "en_name": "Texas Burger Basic",
                    "ar_name": "برجر تكساس (أساسي)",
                    "en_desc": "120g smoked patty, crispy onion, cheddar, BBQ",
                    "ar_desc": "فطيرة لحم مدخن 120 غرام مع بصل مقرمش وجبنة تشيدر وصوص باربيكيو",
                    "price": 229
                }
            ]
        },
        "🍝 Pasta": {
            "ar": "🍝 المعكرونة",
            "items": [
                {
                    "en_name": "Fettuccine Alfredo",
                    "ar_name": "فيتوتشيني ألفريدو",
                    "en_desc": "Creamy sauce, mushrooms, grilled chicken, parmesan",
                    "ar_desc": "معكرونة فيتوتشيني بصوص كريمي ناعم مع فطر ودجاج مشوي وجبنة بارميزان",
                    "price": 279
                },
                {
                    "en_name": "Spaghetti Bolognese",
                    "ar_name": "سباغيتي بولونيز",
                    "en_desc": "Rich Italian meat sauce, parmesan",
                    "ar_desc": "سباغيتي إيطالية بصوص لحم غني وعميق وجبنة بارميزان مبشورة",
                    "price": 289
                },
                {
                    "en_name": "Shrimp Pasta",
                    "ar_name": "معكرونة جمبري",
                    "en_desc": "White or red sauce, shrimp, grilled veggies",
                    "ar_desc": "معكرونة طازة مع جمبري شهي وصوص أبيض أو أحمر وخضار مشوية حارة",
                    "price": 259
                }
            ]
        },
        "🥩 Main Courses": {
            "ar": "🥩 الأطباق الرئيسية",
            "items": [
                {
                    "en_name": "Chicken Fajita",
                    "ar_name": "فاهيتا الدجاج",
                    "en_desc": "Grilled chicken, peppers, onions, rice, tortillas + 2 sides",
                    "ar_desc": "دجاج مشوي مع فلفل وبصل وأرز وتورتيلا جزائرية مع اختيار طبقين جانبيين",
                    "price": 299
                },
                {
                    "en_name": "Beef Fajita",
                    "ar_name": "فاهيتا اللحم",
                    "en_desc": "Tender beef strips, peppers, onions, rice, tortillas + 2 sides",
                    "ar_desc": "شرائح لحم طرية مشوية مع فلفل وبصل وأرز وتورتيلا مع طبقين جانبيين",
                    "price": 339
                },
                {
                    "en_name": "Mixed Fajita",
                    "ar_name": "فاهيتا مختلطة",
                    "en_desc": "Chicken, beef & shrimp, peppers, onion, rice, tortillas + 2 sides",
                    "ar_desc": "دجاج ولحم وجمبري مشويين مع فلفل وبصل وأرز وتورتيلا مع طبقين جانبيين",
                    "price": 359
                },
                {
                    "en_name": "Escalope Schnitzel",
                    "ar_name": "إسكالوب شنيتزل",
                    "en_desc": "Thin breaded veal, crispy, white sauce + 2 sides",
                    "ar_desc": "لحم عجل رقيق مغطى بطبقة ذهبية مقرمشة مع صوص أبيض كريمي وطبقين جانبيين",
                    "price": 399
                },
                {
                    "en_name": "Crispy Chicken with Mushrooms",
                    "ar_name": "دجاج مقرمش مع الفطر",
                    "en_desc": "Crispy chicken, fresh mushrooms, creamy sauce + 2 sides",
                    "ar_desc": "دجاج مقرمش ذهبي مع فطر طازج وصوص كريمي لذيذ وطبقين جانبيين",
                    "price": 329
                },
                {
                    "en_name": "Ribeye Steak",
                    "ar_name": "ستيك ريب آي",
                    "en_desc": "Grilled ribeye, mushroom/pepper/BBQ sauce + 2 sides",
                    "ar_desc": "لحم ريب آي مشوي احترافي مع فطر أو فلفل أو صوص باربيكيو وطبقين جانبيين",
                    "price": 449
                }
            ]
        },
        "🍟 Sides": {
            "ar": "🍟 الأطباق الجانبية",
            "items": [
                {
                    "en_name": "French Fries",
                    "ar_name": "بطاطس مقلية",
                    "en_desc": "Golden & crispy",
                    "ar_desc": "بطاطس مقلية ذهبية مقرمشة من الخارج طرية من الداخل",
                    "price": 50
                },
                {
                    "en_name": "Mashed Potato",
                    "ar_name": "بطاطس مهروسة",
                    "en_desc": "Smooth buttery mash",
                    "ar_desc": "بطاطس ناعمة مهروسة مع الزبدة والقشدة",
                    "price": 70
                },
                {
                    "en_name": "Soho Rice",
                    "ar_name": "أرز سوهو",
                    "en_desc": "Seasoned aromatic rice",
                    "ar_desc": "أرز عطري مطبوخ مع توابل مميزة",
                    "price": 50
                },
                {
                    "en_name": "Coleslaw",
                    "ar_name": "كول سلو",
                    "en_desc": "Creamy cabbage slaw",
                    "ar_desc": "سلطة ملفوف كريمية طازجة منعشة",
                    "price": 50
                },
                {
                    "en_name": "Corn Cup",
                    "ar_name": "كوب ذرة",
                    "en_desc": "Sweet corn kernels",
                    "ar_desc": "حبات ذرة حلوة طازجة ولذيذة",
                    "price": 50
                },
                {
                    "en_name": "Sautéed Vegetables",
                    "ar_name": "خضار مطبوخة",
                    "en_desc": "Seasonal medley",
                    "ar_desc": "خضار موسمية مشوية بزيت الزيتون والثوم",
                    "price": 70
                },
                {
                    "en_name": "Side Mac & Cheese",
                    "ar_name": "ماك أند تشيز (جانبي)",
                    "en_desc": "Creamy pasta side",
                    "ar_desc": "معكرونة بصوص جبن كريمي غني",
                    "price": 70
                }
            ]
        },
        "👶 Kids Menu": {
            "ar": "👶 قائمة الأطفال",
            "items": [
                {
                    "en_name": "Kids Chicken Strips",
                    "ar_name": "تشيكن استربس اطفال",
                    "en_desc": "Crispy strips, fries, ketchup & juice",
                    "ar_desc": "قطع دجاج مقرمشة مع بطاطس مقلية و صوص و عصير طازج",
                    "price": 189
                },
                {
                    "en_name": "Kids Chicken Burger",
                    "ar_name": "برجر دجاج اطفال",
                    "en_desc": "Mini chicken burger, fries, juice",
                    "ar_desc": "برجر دجاج صغير مع بطاطس مقلية وعصير لذيذ",
                    "price": 189
                },
                {
                    "en_name": "Kids Beef Burger",
                    "ar_name": "برجر لحم اطفال",
                    "en_desc": "Mini beef patty, cheese, fries, juice",
                    "ar_desc": "برجر لحم صغير مع جبنة وبطاطس مقلية وعصير",
                    "price": 189
                }
            ]
        },
        "🍰 Desserts": {
            "ar": "🍰 الحلويات",
            "items": [
                {
                    "en_name": "Molten Cake",
                    "ar_name": "كيكة الشوكولاتة الذائبة",
                    "en_desc": "Warm chocolate lava cake",
                    "ar_desc": "كيكة شوكولاتة دافئة بمركز سائل شهي",
                    "price": 130
                },
                {
                    "en_name": "Cheesecake",
                    "ar_name": "تشيزكيك",
                    "en_desc": "Creamy NY style",
                    "ar_desc": "كيكة جبنة كريمية بالطريقة الأمريكية الأصلية",
                    "price": 125
                },
                {
                    "en_name": "Brownie",
                    "ar_name": "براوني",
                    "en_desc": "Rich fudge brownie",
                    "ar_desc": "حلوى براوني بالشوكولاتة الغنية واللذيذة",
                    "price": 130
                }
            ]
        },
        "🧂 Sauces (Extra)": {
            "ar": "🧂 الصلصات (إضافية)",
            "items": [
                {
                    "en_name": "Honey Mustard",
                    "ar_name": "خردل بالعسل",
                    "en_desc": "Sweet & tangy",
                    "ar_desc": "خليط العسل والخردل الحاد اللذيذ",
                    "price": 30
                },
                {
                    "en_name": "Buffalo Sauce",
                    "ar_name": "صوص بافلو",
                    "en_desc": "Spicy classic",
                    "ar_desc": "صوص بافلو الكلاسيكي الحار والشهي",
                    "price": 30
                },
                {
                    "en_name": "Blue Cheese",
                    "ar_name": "صوص الجبنة الزرقاء",
                    "en_desc": "Creamy bold",
                    "ar_desc": "صوص جبنة زرقاء كريمي غني بالطعم",
                    "price": 30
                },
                {
                    "en_name": "Ranch",
                    "ar_name": "صوص رانتش",
                    "en_desc": "Herb buttermilk",
                    "ar_desc": "صوص الأعشاب والألبان الكلاسيكي",
                    "price": 30
                },
                {
                    "en_name": "Cheese Sauce",
                    "ar_name": "صوص جبن",
                    "en_desc": "Velvety cheddar",
                    "ar_desc": "صوص جبنة تشيدر ناعم وكريمي",
                    "price": 30
                },
                {
                    "en_name": "Caesar",
                    "ar_name": "صوص سيزر",
                    "en_desc": "Classic dressing",
                    "ar_desc": "صوص سيزر الكلاسيكي الإيطالي",
                    "price": 30
                },
                {
                    "en_name": "Dynamite Sauce",
                    "ar_name": "صوص ديناميت",
                    "en_desc": "Fiery kick",
                    "ar_desc": "صوص ديناميت الناري المثير",
                    "price": 30
                },
                {
                    "en_name": "Pico de Gallo",
                    "ar_name": "صوص بيكو ديجالو",
                    "en_desc": "Fresh salsa",
                    "ar_desc": "سلطة بيكو ديجالو الطازجة المنعشة",
                    "price": 30
                }
            ]
        }
    },
    "istik": {
        "☕ Hot Drinks": {
            "ar": "☕ المشروبات الساخنة",
            "items": [
                {"en_name": "Tea","ar_name": "شاى","en_desc": "Classic or green infusion","ar_desc": "شاى كلاسيكي أو اخضر بالنعناع","price": 35},
                {"en_name": "Green Tea","ar_name": "شاى اخضر","en_desc": "Fresh mint brew","ar_desc": "شاى أخضر طازج مع النعناع","price": 35},
                {"en_name": "Tea Pot (2 cups)","ar_name": "ابريق شاى (استكانتين)","en_desc": "Serves two","ar_desc": "ابريق شاى يكفي لشخصين","price": 70},
                {"en_name": "Tea Pot (4 cups)","ar_name": "ابريق شاى (4 استكانات)","en_desc": "Sharing pot","ar_desc": "ابريق شاى يكفي لأربع أشخاص","price": 120},
                {"en_name": "Karak Tea Pot","ar_name": "ابريق شاى كرك","en_desc": "Spiced strong tea","ar_desc": "شاى كرك قوي ومحبب مع التوابل الدافئة","price": 140},
                {"en_name": "Matcha","ar_name": "ماتشا","en_desc": "Ceremonial matcha","ar_desc": "ماتشا ياباني اخضر البودرة الاصلية النقية","price": 100},
                {"en_name": "Nescafe","ar_name": "نسكافيه","en_desc": "Classic instant","ar_desc": "قهوة نسكافيه كلاسيكية سريعة التحضير","price": 60},
                {"en_name": "Americano","ar_name": "امريكان كوفي","en_desc": "Smooth black coffee","ar_desc": "قهوة سوداء ناعمة و مشبعة بالنكهة","price": 85},
                {"en_name": "Espresso Single","ar_name": "اسبرسو سينجل","en_desc": "Intense shot","ar_desc": "شوت إسبرسو قوي و مكثف","price": 80},
                {"en_name": "Espresso Double","ar_name": "اسبرسو دبل","en_desc": "Double shot","ar_desc": "شوتين إسبرسو قويين للحب الحقيقي للقهوة","price": 90},
                {"en_name": "Macchiato Single","ar_name": "ميكاتو سينجل","en_desc": "Espresso stained with milk","ar_desc": "إسبرسو مع قطرات من الحليب الدافئ","price": 85},
                {"en_name": "Macchiato Double","ar_name": "ميكاتو دبل","en_desc": "Double espresso macchiato","ar_desc": "ميكاتو بشوتين إسبرسو قويين مع الحليب","price": 95},
                {"en_name": "Mocha","ar_name": "موكا","en_desc": "Chocolate & espresso","ar_desc": "خليط القهوة والشوكولاتة الدافئ اللذيذ","price": 110},
                {"en_name": "Cappuccino","ar_name": "كابيتشينو","en_desc": "Perfect foam","ar_desc": "قهوة كابيتشينو بالرغوة الناعمة المثالية","price": 100},
                {"en_name": "Cafe Latte","ar_name": "كافيه لاتيه","en_desc": "Creamy steamed milk","ar_desc": "قهوة لاتيه بالحليب المبخر والكريمي","price": 100},
                {"en_name": "Hot Chocolate","ar_name": "شوكولاتة ساخنة","en_desc": "Rich dark cocoa","ar_desc": "شوكولاتة ساخنة غنية بطعم الكاكاو الداكن","price": 110},
                {"en_name": "Hot Cider","ar_name": "عصير تفاح ساخن","en_desc": "Warm spiced apple","ar_desc": "عصير تفاح دافئ مع التوابل الدافئة","price": 90},
                {"en_name": "Turkish Coffee Single","ar_name": "قهوة تركي سينجل","en_desc": "Traditional unfiltered","ar_desc": "قهوة تركية أصلية بطريقة تقليدية أصيلة","price": 70},
                {"en_name": "Turkish Coffee Double","ar_name": "قهوة تركي دبل","en_desc": "Double strength","ar_desc": "قهوة تركية ضعيفة مضاعفة","price": 80},
                {"en_name": "French Coffee","ar_name": "قهوة فرنسية","en_desc": "Smooth dark roast","ar_desc": "قهوة فرنسية محمصة بشكل مثالي","price": 85},
                {"en_name": "Sahlab with Nuts","ar_name": "سحلب بالمكسرات","en_desc": "Creamy orchid drink, topped nuts","ar_desc": "سحلب كريمي مع المكسرات والزبيب والشوكولاتة","price": 85},
                {"en_name": "Flat White","ar_name": "فلات وايت","en_desc": "Velvety microfoam","ar_desc": "قهوة بالحليب المبخر الناعم جداً","price": 90},
                {"en_name": "Ginger Infusion","ar_name": "مشروب الزنجبيل","en_desc": "Fresh zesty ginger","ar_desc": "مشروب زنجبيل طازج دافئ ومنعش","price": 50},
                {"en_name": "Arabic Coffee Pot (Dallah)","ar_name": "قهوة عربية (ركوة)","en_desc": "Cardamom-infused, serves 3-4","ar_desc": "القهوة العربية الأصلية بالهيل تخدم 3-4 أشخاص","price": 210},
                {"en_name": "Hot Istikanah","ar_name": "شراب إستكنانة","en_desc": "House signature hot blend","ar_desc": "المشروب الساخن الخاص بإستكنانة بالنكهات المركبة","price": 125},
                {"en_name": "Spanish Latte","ar_name": "لاتيه إسباني","en_desc": "Sweetened condensed milk latte","ar_desc": "قهوة لاتيه بالحليب المكثف المحلى","price": 115},
                {"en_name": "Herbal Cocktail","ar_name": "مشروب الأعشاب","en_desc": "Soothing herbs blend","ar_desc": "مشروب أعشاب هادئ دافئ مهدئ","price": 55}
            ]
        },
        "🥛 Cold Drinks": {
            "ar": "🥛 المشروبات الباردة",
            "items": [
                {
                    "en_name": "Iced Coffee",
                    "ar_name": "قهوة باردة",
                    "en_desc": "Chilled espresso with ice",
                    "ar_desc": "قهوة إسبرسو باردة على الثلج منعشة جداً",
                    "price": 95
                },
                {
                    "en_name": "Iced Latte",
                    "ar_name": "لاتيه بارد",
                    "en_desc": "Silky cold milk coffee",
                    "ar_desc": "لاتيه بارد ناعم بالحليب البارد",
                    "price": 100
                },
                {
                    "en_name": "Cold Brew",
                    "ar_name": "قهوة مغلية باردة",
                    "en_desc": "Smooth cold coffee concentrate",
                    "ar_desc": "قهوة مغلية بارداً لنكهة عميقة ناعمة",
                    "price": 85
                }
            ]
        },
        "🧃 Fresh Juices": {
            "ar": "🧃 العصائر الطازجة",
            "items": [
                {
                    "en_name": "Orange Juice",
                    "ar_name": "عصير برتقال",
                    "en_desc": "Freshly squeezed",
                    "ar_desc": "عصير برتقال طازج معصور من حبات البرتقال الطبيعية",
                    "price": 65
                },
                {
                    "en_name": "Mango Juice",
                    "ar_name": "عصير مانجو",
                    "en_desc": "Tropical smooth",
                    "ar_desc": "عصير مانجو ناعم استوائي لذيذ جداً",
                    "price": 70
                },
                {
                    "en_name": "Strawberry Juice",
                    "ar_name": "عصير فراولة",
                    "en_desc": "Berry fresh blend",
                    "ar_desc": "عصير فراولة طازج بطعم كلاسيكي على التوت",
                    "price": 70
                },
                {
                    "en_name": "Mixed Fruits",
                    "ar_name": "عصير فواكه مختلطة",
                    "en_desc": "Rainbow blend",
                    "ar_desc": "عصير فواكه متعددة الألوان والنكهات",
                    "price": 75
                }
            ]
        },
        "🍰 Pastries & Bakes": {
            "ar": "🍰 المعجنات والخبز",
            "items": [
                {
                    "en_name": "Croissant",
                    "ar_name": "كرواسان",
                    "en_desc": "Buttery flaky pastry",
                    "ar_desc": "كرواسان بالزبدة طبقاته ناعمة ومقرمشة",
                    "price": 55
                },
                {
                    "en_name": "Chocolate Croissant",
                    "ar_name": "كرواسان بالشوكولاتة",
                    "en_desc": "Chocolate filled delight",
                    "ar_desc": "كرواسان بالشوكولاتة الداخلية اللذيذة",
                    "price": 60
                },
                {
                    "en_name": "Pain au Chocolat",
                    "ar_name": "خبز بالشوكولاتة",
                    "en_desc": "French chocolate bread",
                    "ar_desc": "خبز فرنسي بالشوكولاتة النقية الدافئة",
                    "price": 60
                }
            ]
        }
    }
}

# Save to JSON
with open('bilingual_menu.json', 'w', encoding='utf-8') as f:
    json.dump(bilingual_menu, f, ensure_ascii=False, indent=2)

print("Bilingual menu created successfully!")
print(f"Total Soho categories: {len(bilingual_menu['soho'])}")
print(f"Total Istik categories: {len(bilingual_menu['istik'])}")
