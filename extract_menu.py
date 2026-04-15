import openpyxl
import json
from collections import defaultdict

files = {
    'ISTIKNANAH FINAL MENU (2).xlsx': r'c:\Users\dell\Documents\menu4\ISTIKNANAH FINAL MENU (2).xlsx',
    'soho menu---.xlsx': r'c:\Users\dell\Documents\menu4\soho menu---.xlsx'
}

all_menus = {}

for file_label, file_path in files.items():
    try:
        wb = openpyxl.load_workbook(file_path)
        sheet = wb.active
        
        print(f"\n=== {file_label} ===")
        print(f"Sheet: {sheet.title}, Dimensions: {sheet.dimensions}")
        
        menu_data = defaultdict(list)
        current_category = None
        
        for idx, row in enumerate(sheet.iter_rows(min_row=1, max_row=1000), 1):
            values = [cell.value for cell in row]
            
            # Skip completely empty rows
            if not any(v is not None for v in values):
                continue
            
            col_a = values[0]
            col_b = values[1] if len(values) > 1 else None
            col_c = values[2] if len(values) > 2 else None
            col_d = values[3] if len(values) > 3 else None
            
            if col_a is not None:
                print(f"Row {idx}: {values[:4]}")
        
        all_menus[file_label] = dict(menu_data)
        
    except Exception as e:
        print(f"Error with {file_label}: {e}")
        import traceback
        traceback.print_exc()

print("\n" + "="*50)
print("Inspection complete")
