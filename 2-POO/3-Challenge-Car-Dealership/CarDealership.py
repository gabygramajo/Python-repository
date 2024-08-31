"""
Reto:
concesionaria 
- Se podra realizar la compra de un vehiculo (por el usuario)
- Se podra realizar la venta de un vehiculo (por la concesionaria)
- Gestionar lso vehiculos, listar los disponibles
"""

class Car:
    def __init__(self,car_brand, model, car_id):
        self.car_brand = car_brand    
        self.model = model    
        self.car_id = car_id
        self.available = True 
        
    def info(self):
        return f"{self.car_id} - {self.car_brand} {self.model}"
    
    def deactivate_car(self):
        if self.available:
            self.available = False
            return "Vehículo desactivado."
    
    def activate_car(self):
        if not self.available:
            self.available = True
            return "Vehículo activado."
            

class User:
    def __init__(self,name, user_id):
        self.name = name    
        self.user_id = user_id
        self.cars = []    
        self.activate = True
        
    def list_my_cars(self):
        if len(self.cars) == 0:
            print("No hay autos")
            return 0
        
        for car in self.cars:
            print(car.info())
    
    def add_car(self, car):
            self.cars.append(car)  
    
    def buy_car(self, car):
        if car.available:
            self.add_car(car)
            return f"El usuario {self.name} compró un {car.info()}"
        return f"El vehículo {car.info()} no está disponible."
    
    def sell_car(self, car, new_owner):
        if car in self.cars:
            new_owner.add_car(car)
            self.cars.remove(car)
            return f"{self.name} vendió un {car.info()} a {new_owner.name}"
        return f"El vehículo {car.info()} no está disponible."
        

class CarDealership:
    def __init__(self, name):
        self.name = name
        self.cars = []
        self.users = []
        
    def list_cars(self):
        if len(self.cars) == 0:
            print("No hay autos")
            return 0

        print("\nCars: ")
        for car in list(filter(lambda car: car.available, self.cars)):
            print(car.info())
    
    def list_users(self):
        if len(self.users) == 0:
            print("No hay autos")
            return 0
        
        print("\nUSers: ")
        for user in list(filter(lambda user: user.activate, self.users)):
            print(user.info())
    
    def add_car(self, car):
            self.cars.append(car)  
    
    def sell_car(self, car, new_owner):
        if car in self.cars:
            new_owner.add_car(car)
            self.cars.remove(car)
            return f"{self.name} vendió un {car.info()} a {new_owner.name}"
        return f"El vehículo {car.info()} no está disponible."

# create cars        
car1 = Car("Toyota", "Corolla", "C001")
car2 = Car("Ford", "Mustang", "C002")
car3 = Car("Chevrolet", "Camaro", "C003")
car4 = Car("Honda", "Civic", "C004")
car5 = Car("Mitsubichi", "Eclipse", "C005")

#Create Car dealership
car_dealership = CarDealership("Mendy - Car dealership")
car_dealership.add_car(car1)
car_dealership.add_car(car2)
car_dealership.add_car(car3)
car_dealership.add_car(car4)
car_dealership.add_car(car5)

#list cars
car_dealership.list_cars()

# crear users
user1 = User("Juan", "U001")
user2 = User("Marta", "U002")
user2 = User("Sasha", "U003")

# pay cars 

