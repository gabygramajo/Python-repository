text = "Programming"

# max char
print(f"max char of '{text}' is '{max(text)}'")

# min char
print(f"min char of '{text}' is '{min(text)}'")


text = "Python is a Multi Paradigm Programming Language"
# join()
new_text = "-".join(text)
print(f"new text is '{new_text}'")

# split
new_text = text.split(' ')
print(f"new text is '{new_text}'")

# replace
new_text = text.replace('Python', 'Java')
print(f"new text is '{new_text}'")

# find
index = text.find("n")
print(f"text.find(\"n\") -> {index}")
index = text.rfind("n")
print(f"text.rfind(\"n\") -> {index}")