def spell_text(text):
    for index, letter in enumerate(text):
        print(f"'{letter}'\t", end="")
    print()
        
def index_text(text):
    for index, letter in enumerate(text):
        print(f"'{index}'\t", end="")
    print()

text = "¡Hello World!"

print(f"text -> '{text}' ")
print(f"text len = {len(text)}")

spell_text(text)
index_text(text)

# Slicing
print(f"\n1) text[:] = {text[:]}")
print(f"\n2) text[:5] = {text[::-1]}")
print(f"\n3) text[0:13] = {text[0:13]}")
print(f"\n4) text[0:13:2] = {text[0:13:2]}")
print(f"\n5) text[::2] = {text[::2]}")
print(f"\n6) text[1:5] = {text[1:5]}")
print(f"\n7) text[7:] = {text[7:]}")
print(f"\n8) text[:5] = {text[:5]}")

palindrome = "oso"

print(f"\nThe word '{palindrome}' is palindrome? {palindrome[:] == palindrome[::-1]} \nbeacouse: palindrome[:] == palindrome[::-1]")

"""
Out>>
text -> '¡Hello World!' 
text len = 13
'¡'     'H'     'e'     'l'     'l'     'o'     ' '     'W'     'o'     'r'     'l'     'd'     '!'
'0'     '1'     '2'     '3'     '4'     '5'     '6'     '7'     '8'     '9'     '10'    '11'    '12'

1) text[:] = ¡Hello World!

2) text[:5] = !dlroW olleH¡

3) text[0:13] = ¡Hello World!

4) text[0:13:2] = ¡el ol!

5) text[::2] = ¡el ol!

6) text[1:5] = Hell

7) text[7:] = World!

8) text[:5] = ¡Hell

The word 'oso' is palindrome? True 
beacouse: palindrome[:] == palindrome[::-1]
"""