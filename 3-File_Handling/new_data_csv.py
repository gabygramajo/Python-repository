import csv
path = "3-File_Handling/products.csv"

new_product = {
    'name': 'Wireless charger',
    'price': 75,
    'quantity': 100,
    'brand': 'ChargerMaster',
    'category': 'Accessories',
    'entry_date': '2024-07-01'
}

with open(path, mode='a', newline='') as file:
    file.write('\n')
    csv_writer = csv.DictWriter(file, fieldnames = new_product.keys())
    csv_writer.writerow(new_product)