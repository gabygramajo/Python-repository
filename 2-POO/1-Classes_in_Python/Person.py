class Person:
    
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        print(f"Name: {self.name}\nAge: {self.age}")

person1 = Person("Lucas", 56)
person2 = Person("Analía", 24)

person1.info()
"""
Name: Lucas
Age: 56
"""
person2.info()
"""
Name: Analía
Age: 24
"""