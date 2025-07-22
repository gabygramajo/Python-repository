def contar_primos(numero):
    primos = []

    for num in range(2, numero + 1):
        es_primo = True
        # Si "num" tiene algún divisor (distinto de 1 y de "num"), al menos uno de ellos estará en el rango de 2 a √num (raiz cuadrada)
        ultimo_posible_divisor = int(num ** 0.5) + 1

        for divisor in range(2, ultimo_posible_divisor):
            if num % divisor == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(num)

    return f"Números primos encontrados: {len(primos)} : {primos}"

print(contar_primos(1))
print(contar_primos(31))