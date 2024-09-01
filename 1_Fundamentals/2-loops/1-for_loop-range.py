# range
print("1) range(5) =", end=" ")
for num in range(5):
    print(num, end=" ")

# range (start, stop)
print("\n\n2) range(6, 13) =", end=" ")
for num in range(6, 13):
    print(num, end=" ")

# range (start, stop, step)
print("\n\n3) range(6, 13, 2) =", end=" ")
for num in range(6, 13, 2):
    print(num, end=" ")

# range (start, stop, step)
print("\n\n4) range(10, 0, -1) =", end=" ")
for num in range(10, 0, -1):
    print(num, end=" ")

# range (start, stop, step)
print("\n\n5) range(20, 0, -2) =", end=" ")
for num in range(20, 0, -2):
    print(num, end=" ")
    

print(f"\n\n6) range(5) to list = {list(range(5))}")

"""
Out>> 
1) range(5) = 0 1 2 3 4 

2) range(6, 13) = 6 7 8 9 10 11 12 

3) range(6, 13, 2) = 6 8 10 12 

4) range(10, 0, -1) = 10 9 8 7 6 5 4 3 2 1 

5) range(20, 0, -2) = 20 18 16 14 12 10 8 6 4 2 

6) range(5) to list = [0, 1, 2, 3, 4]
"""