def my_generator():
    yield "a"
    yield "b"
    yield "c"
    
for value in my_generator():
    print(value)

"""
a
b
c
"""

# Fibonacci
def fibonacci(limit):
    a, b = 0, 1
    while a < limit: 
        yield a
        a, b = b, a+b
        
for num in fibonacci(10):
    print(num)

"""
0
1
1
2
3
5
8
"""