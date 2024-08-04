student_list = ["Catalina", "Lucas", "Miguel", "Luciana", "Sasha"]
print(f"\n1) student_list = {student_list}")

print(f"\n2) list(enumerate(student_list)) = {list(enumerate(student_list))}")

print("\n3) for + enumerate: ")
for index, name in enumerate(student_list):
    print(f"{index} - {name}")