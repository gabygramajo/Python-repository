import csv
path = "3-File_Handling/products.csv"

# Leer
def read_csv(path):
    with open(path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            print(row)
#read_csv(path)

# mostrar por columnas
def read_by_column_csv(path):
    with open(path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            print(f"Producto: {row['name']}, precio: ${row['price']}")
read_by_column_csv(path)