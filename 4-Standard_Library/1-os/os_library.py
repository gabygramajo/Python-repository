import os

# Dir actual
cwd = os.getcwd()
#print(cwd)

# listar archivos txt
txt_file = [file for file in os.listdir('4-Standard_Library/1-os/files') if file.endswith('.txt')]
print(f"Archivos txt: \n{txt_file}")

# renombrar archivo
os.rename('main.txt', 'notes.txt')

print(f"\nArchivos txt: \n{txt_file}")
