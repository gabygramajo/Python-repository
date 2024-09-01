frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
word = ""

for index, char in enumerate(frase[8::]):
    if index % 3 == 0:
        word += char

print(word)