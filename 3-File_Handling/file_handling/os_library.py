import os
current_path = os.getcwd()
print(f'Current path: {current_path}')

os.chdir('D:\\ggabr\\Documents')
file = open('documento_prueba.txt', 'r')
print(file.read())
file.close()