import pandas as pd
import os

# Nama file Excel utama
input_file = "tabref_BKN_referensi BKN.xlsx"

# Folder output
output_dir = "csv"
os.makedirs(output_dir, exist_ok=True)

# Baca semua sheet
sheets = pd.read_excel(input_file, sheet_name=None)

# Loop setiap sheet dan simpan ke file CSV
for sheet_name, df in sheets.items():
    # Bersihkan nama sheet biar aman jadi nama file
    safe_name = "".join(c if c.isalnum() else "_" for c in sheet_name)
    output_file = os.path.join(output_dir, f"{safe_name}.csv")
    
    # Simpan ke CSV
    df.to_csv(output_file, index=False, encoding="utf-8-sig")
    print(f"✅ Sheet '{sheet_name}' disimpan ke {output_file}")
