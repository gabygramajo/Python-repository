import csv
file_path = "3-File_Handling/products.csv"
updated_file_path = "3-File_Handling/products_updated.csv"

new_product = {
    'name': 'Wireless charger',
    'price': 75,
    'quantity': 100,
    'brand': 'ChargerMaster',
    'category': 'Accessories',
    'entry_date': '2024-07-01'
}

with open(file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    # obtener columnas + nueva columna
    fieldnames = csv_reader.fieldnames + ['total_value']
    
    with open(updated_file_path, mode='w', newline='') as updated_file:
        csv_writer = csv.DictWriter(updated_file, fieldnames=fieldnames)
        # escribir los encabezados
        csv_writer.writeheader()
        for row in csv_reader:
            row['total_value'] = float(row['price']) * int(row['quantity'])
            csv_writer.writerow(row)