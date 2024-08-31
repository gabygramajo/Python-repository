# https://www.pythoncheatsheet.org/cheatsheet/comprehensions

# suares 
squares = [x**2 for x in range(1, 11)]
print(f"squares = {squares}")

# Celsius yto Fahrenheit
celsius = [0, 10, 20, 30, 40]
fahrenheit = [(temp * 9/5) * 32 for temp in celsius]
print(f"Celcius: {celsius} to Fahrenheit: {fahrenheit}")

# even numbers
even_numbers = [ num for num in range(0, 21) if num%2 == 0]
print(f"even numbers (0, 20) -> {even_numbers}")

# transposed matix
matrix = [
    [10,20,30],
    [60,70,80],
    [90,100,200]
]

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

print(f"matrix -> {matrix}")
print(f"transposed -> {transposed}")
