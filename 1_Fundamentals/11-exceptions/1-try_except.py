# https://www.pythoncheatsheet.org/cheatsheet/exception-handling
# https://docs.python.org/3/tutorial/errors.html
# https://www.w3schools.com/python/python_try_except.asp

try:
    divisor = int(input("Ingrese un número divisor: "))
    result = 100/divisor
    print(result)
except ZeroDivisionError as e:
    print("Error: ", e)
except ValueError as e:
    print("Error: ", e)
    
# gerarquía de excepciones
