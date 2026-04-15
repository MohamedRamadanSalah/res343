import pandas as pd
import json

# Read SOHO menu
soho_df = pd.read_excel('soho menu---.xlsx')
print('SOHO MENU')
print('Columns:', soho_df.columns.tolist())
print('Shape:', soho_df.shape)
print('\nFirst 5 rows:')
print(soho_df.head(5))

print('\n' + '='*100 + '\n')

# Read ISTIKNANAH menu
istik_df = pd.read_excel('ISTIKNANAH FINAL MENU (2).xlsx')
print('ISTIKNANAH MENU')
print('Columns:', istik_df.columns.tolist())
print('Shape:', istik_df.shape)
print('\nFirst 5 rows:')
print(istik_df.head(5))

# Save to JSON for processing
menu_data = {
    'soho': soho_df.to_dict('records'),
    'istiknanah': istik_df.to_dict('records')
}

with open('menu_data_raw.json', 'w', encoding='utf-8') as f:
    json.dump(menu_data, f, ensure_ascii=False, indent=2)

print('\n✓ Saved to menu_data_raw.json')
