class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
    
    def borrow(self):
        if self.available:
            self.available = False
            print(f"El libro '{self.title}' ha sido prestado")
        else:
            print(f"El libro '{self.title}' no está disponible")
    
    def return_book(self):
        self.available = True
        print(f"El libro '{self.title}' ha sido devuelto")

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrow_books = []
    
    def borrow_book(self, book):
        if book.available:
            book.borrow()
            self.borrow_books.append(book)
        else:
            print(f"El libro '{book.title}' no está disponible")
    
    def return_book(self, book):
        if book in self.borrow_books:
            book.return_book()
            self.borrow_books.remove(book)
        else:
            print(f"El libro '{book.Title}' no está en la lista de prestados.")

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)
        print(f"El libro '{book.title}' ha sido agregado")
    
    def register_user(self, user):
        self.users.append(user)
        print(f"El usuario '{user.name}' ha sido registrado correctamente.")
    
    def show_available_books(self):
        print("\nLibros disponibles: ")
        for book in self.books:
            if book.available:
                print(f"{book.title} by {book.author}")

the_public_library = Library("The Public Library")

book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book4 = Book("One Hundred Years of Solitude", "Gabriel García Márquez")
book5 = Book("Moby Dick", "Herman Melville")
book6 = Book("Pride and Prejudice", "Jane Austen")
book7 = Book("War and Peace", "Leo Tolstoy")
book8 = Book("The Catcher in the Rye", "J.D. Salinger")
book9 = Book("Crime and Punishment", "Fyodor Dostoevsky")
book10 = Book("The Hobbit", "J.R.R. Tolkien")

the_public_library.add_book(book1)
the_public_library.add_book(book2)
the_public_library.add_book(book3)
the_public_library.add_book(book4)
the_public_library.add_book(book5)
the_public_library.add_book(book6)
the_public_library.add_book(book7)
the_public_library.add_book(book8)
the_public_library.add_book(book9)
the_public_library.add_book(book10)


user1 = User("Alice", "U001")
user2 = User("Bob", "U002")
user3 = User("Charlie", "U003")
user4 = User("Diana", "U004")
user5 = User("Eve", "U005")

the_public_library.register_user(user1)
the_public_library.register_user(user2)
the_public_library.register_user(user3)
the_public_library.register_user(user4)
the_public_library.register_user(user5)


# Mostrar libros
the_public_library.show_available_books()

#Realizar préstamo
print("\n")
user1.borrow_book(book2)
user1.borrow_book(book4)
user1.borrow_book(book6)

# Mostrar libros
the_public_library.show_available_books()

#Devoler Libro
print("\n")
user1.return_book(book2)
user1.return_book(book6)

# Mostrar libros
the_public_library.show_available_books()