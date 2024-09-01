# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

# Ruta del archivo
path = '3-File_Handling/cuento.txt'

# leer 'r'
# with open(path, 'r') as file:
#     for lines in file:
#         print(lines.strip())

# escribir 
with open(path, 'a') as file:
    file.write("\n\nWritten by ChatGPT")
# con 'a' de 'append' -> agrega al final 
# con 'w' de 'write' -> sobreescribe