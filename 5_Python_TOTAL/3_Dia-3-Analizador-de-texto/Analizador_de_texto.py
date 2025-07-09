print("### ANALIZADOR DE TEXTO ###")
text = input("Ingresar texto: ").lower()
letters = []
analysis = {}
# texto de prueba: Ya somos el olvido que seremos. El lento e implacable rio del tiempo
print("\nGenial! Ahora ingresa 3 letras:")
letters.append(input("Letra 1°: ").lower())
letters.append(input("Letra 2°: ").lower())
letters.append(input("Letra 3°: ").lower())

#1
analysis["#1"] = f"Veces que aparece cada una de las letras: \n\t\"{letters[0]}\" = {text.count(letters[0])}\n\t\"{letters[1]}\" = {text.count(letters[1])}\n\t\"{letters[2]}\" = {text.count(letters[2])}."

#2
analysis["#2"] = f"El texto tiene un total de {len(text.split())} palabras."

#3
analysis["#3"] = f"El texto comienza con la letra \"{text[0]}\" y finaliza con la letra \"{text[-1]}\"."
#4
analysis["#4"] = f"Texto invertido: {text[::-1]}."

#5
analysis["#5"] = f"¿Contiene la palabra \"Python\"? {"Python".lower() in text}."

print(f"Realizando analisis...\nAnalisis Completo\n\n#1) {analysis["#1"]}\n#2) {analysis["#2"]}\n#3) {analysis["#3"]}\n#4) {analysis["#4"]}\n#5) {analysis["#5"]}")
