# update_csv.py
import os
import requests

# Configuración
sheet_id = os.environ.get("SHEET_ID")  # Define esto en Render
csv_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"
save_path = "/var/data/latest_sheet.csv"

# Descargar CSV
response = requests.get(csv_url)
if response.ok:
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    with open(save_path, "wb") as f:
        f.write(response.content)
    print("CSV actualizado correctamente.")
else:
    raise Exception("Error descargando el CSV")
