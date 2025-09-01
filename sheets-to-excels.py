import pandas as pd
import os

# Nama file Excel utama
input_file = "tabref_BKN_referensi BKN.xlsx"

# Folder output
output_dir = "xlsx"
os.makedirs(output_dir, exist_ok=True)

# Baca semua sheet
sheets = pd.read_excel(input_file, sheet_name=None)

# Loop setiap sheet dan simpan ke file baru
for sheet_name, df in sheets.items():
    # Nama file = nama sheet
    output_file = os.path.join(output_dir, f"{sheet_name}.xlsx")
    df.to_excel(output_file, index=False)
    print(f"✅ Sheet '{sheet_name}' disimpan ke {output_file}")
