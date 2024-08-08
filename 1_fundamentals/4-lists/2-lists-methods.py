numeros = [1,2,3,4,5] 
print(numeros)

# min
print(min(numeros))
# out >> 1

# max
print(max(numeros))
# out >> 5

# suma
print(sum(numeros))
# out >> 15

# to list
new_list = list( range( sum(numeros) ) )
print(new_list)
# out >> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

# in / not in
print( 4 in new_list )
# out >> True
print( 4 not in new_list )
# out >> False 

fruits = ["Banana", "Watermelon"]
print(f"fruits {fruits}")
# out >> fruits ['Banana', 'Watermelon']
# append
fruits.append("Apple")
print(f"fruits {fruits}")
# out >>  fruits ['Banana', 'Watermelon', 'Apple']

# insert
fruits.insert(0, "Orange")
fruits.insert(2, "strawberry")
print(f"fruits {fruits}")
# out >>  fruits ['Orange', 'Banana', 'strawberry', 'Watermelon', 'Apple']

# pop()
removed1 = fruits.pop()
removed2 = fruits.pop(2)
print(f"fruits: {fruits} and it was eliminated {removed1, removed2}")
# out >> fruits: ['Orange', 'Banana', 'Watermelon'] and it was eliminated ('Apple', 'strawberry')

# remove()
removed2 = fruits.remove("Banana")
print(f"fruits: {fruits} and it was eliminated '{removed2}'")
# out >> fruits: ['Orange', 'Watermelon'] and it was eliminated 'None'

# index
print(f"Watermelon is in the index {fruits.index("Watermelon")}")
# out >> Watermelon is in the index 1

# count
print(f"Orange = {fruits.count('Orange')}")
# out >> Orange = 1

# reverse
fruits.reverse()
print(f"fruits revers: {fruits}")
# out >> fruits revers: ['Watermelon', 'Orange']

# sort()
fruits = ['Orange', 'Banana', 'strawberry', 'Watermelon', 'Apple']
fruits.sort()
print(f"1) ruits sort: {fruits}")
# >> 1) ruits sort: ['Apple', 'Banana', 'Orange', 'Watermelon', 'strawberry']
fruits.sort(reverse=True)
print(f"2) ruits reverse sort: {fruits}")
# >> 2) ruits reverse sort: ['strawberry', 'Watermelon', 'Orange', 'Banana', 'Apple']

# clear()
fruits = ['Orange', 'Banana', 'strawberry', 'Watermelon', 'Apple']
fruits.clear()
print(f"fruits clear: {fruits}")
# >> []