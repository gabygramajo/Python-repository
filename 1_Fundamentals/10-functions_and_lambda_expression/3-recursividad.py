def factorial(n):
    if (n == 0):
        return 1
    
    return n * factorial(n-1)

print(factorial(5))

def sumatoria(n):
    if n == 0:
        return n
    
    return n + sumatoria(n-1)

print(sumatoria(10))