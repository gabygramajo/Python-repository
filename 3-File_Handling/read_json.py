import json

json_path = '3-File_Handling/products.json'

# leer json
with open(json_path, mode='r') as json_file:
    products = json.load(json_file)
    
# mostrar json
for product in products:
    # print(product)
    print(f"Products: {product['name']}, Price ${product['price']}")