import json
json_path = '3-File_Handling/products.json'

new_product = {
    'name': 'Wireless charger',
    'price': 75,
    'quantity': 100,
    'brand': 'ChargerMaster',
    'category': 'Accessories',
    'entry_date': '2024-07-01'
}

with open(json_path, mode='r') as json_file:
    products = json.load(json_file)
    
products.append(new_product)

with open(json_path, mode='w') as json_file:
    json.dump(products, json_file, indent=4)