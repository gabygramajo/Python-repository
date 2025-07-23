from random import choice

def letra_valida(letra):
    return len(letra) == 1 and letra.isalpha()

def verificar_letra(palabra_elegida, palabra_oculta, letra, vidas):
    if letra in palabra_elegida:
        return completar_palabra(palabra_elegida, palabra_oculta, letra), vidas
    vidas -= 1
    return palabra_oculta, vidas

def completar_palabra(palabra_elegida, palabra_oculta, letra):
    for i, caracter in enumerate(palabra_elegida):
        if caracter == letra:
            palabra_oculta[i] = letra
    return palabra_oculta

def elegir_palabra():
    palabras = ["animal", "auto", "guitarra", "casa"]
    palabra_elegida = choice(palabras).upper()
    palabra_oculta = ["_" for _ in palabra_elegida]

    return palabra_elegida, palabra_oculta

def finalizar_juego(vidas, letra, palabra_elegida, palabra_oculta):
    if "_" not in palabra_oculta:
        print(f"¡¡¡Felicidades, lograste adivinar la palabra oculta \"{palabra_elegida}\"!!!")
        return True
    if vidas == 0:
        print(f"Perdiste, se te acabaron las vidas, la palabra era: {palabra_elegida}")
        return True

    return False

def iniciar_juego():
    print("### ADIVINA LA PALABRA ###")
    vidas = 6
    letras_intentadas = set()
    palabra_elegida, palabra_oculta = elegir_palabra()

    while True:

        print(f"La palabra oculta contiene {len(palabra_oculta)} letras:\n\t\t{"".join(palabra_oculta)}")
        letra = input(f"\nTienes {vidas} vidas\nIngresa una letra (axit=0): ").upper()

        if not letra_valida(letra) and letra != "0":
            print("Por favor, ingresa solo una letra.")
            continue

        if letra not in letras_intentadas:
            letras_intentadas.add(letra)
        else:
            print("Ya intentaste esa letra. Vuelve a probar")
            continue



        palabra_oculta, vidas = verificar_letra(palabra_elegida, palabra_oculta, letra, vidas)

        if finalizar_juego(vidas, letra, palabra_elegida, palabra_oculta) or letra == "0":
            print("### FIN DEL JUEGO ###")
            break

# inicio
iniciar_juego()
