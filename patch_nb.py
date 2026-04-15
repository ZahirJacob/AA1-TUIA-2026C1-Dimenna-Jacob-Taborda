import json

with open('TP_regresion_AA1.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

new_lines = [
    "# Descartamos las columnas que no sean features\n",
    "X = df2.drop(['fare_amount', 'key', 'date', 'pickup_datetime'], axis=1)\n",
    "y = df2['fare_amount']\n",
    "\n",
    "# Verificamos que no queden NaNs antes de entrenar\n",
    "print('NaNs en X:', X.isnull().sum().sum())\n",
    "X = X.fillna(X.median(numeric_only=True))  # fallback por si queda algun NaN residual\n",
    "\n",
    "print('Features:', X.columns.tolist())",
]

for i, cell in enumerate(nb['cells']):
    if i == 55 and cell['cell_type'] == 'code':
        cell['source'] = new_lines
        print('Patched cell 55')
        break

with open('TP_regresion_AA1.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)

print('Done')
