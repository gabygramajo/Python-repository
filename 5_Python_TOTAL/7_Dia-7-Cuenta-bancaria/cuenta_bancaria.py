import random
from datetime import datetime

# Utilidades
def generar_numero_aleatorio() -> int:
    return random.randint(1000, 9999)

def obtener_fecha_y_hora_actual() -> str:
    ahora = datetime.now()
    fecha_y_hora_formateada = ahora.strftime("%d-%m-%Y %H:%M:%S")
    return fecha_y_hora_formateada

# Clases
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    registos = {}
    balance = 0

    def __init__(self, nombre, apellido):
        super().__init__(nombre, apellido)
        self.numero_de_cuenta = f"ARG{generar_numero_aleatorio()}{generar_numero_aleatorio()}"
        self.registos[generar_numero_aleatorio()] = "Cuenta creada satisfactoriamente."

    def obtener_nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    def obtener_numero_de_cuenta(self):
        return f"{self.numero_de_cuenta}"

    def obtener_balance(self):
        return self.balance

    def depositar(self, monto):
        if monto <= 0:
            print("Monto no válido.")
            return False
        self.balance += monto
        return True

    def validar_balance(self, monto):
        if monto > self.balance:
            print("El monto es mayor que tu balance.")
            return False

        self.balance -= monto
        return True

    def retirar(self, monto):
        if monto <= 0:
            return False

        return self.validar_balance(monto)

    def guardar_registro(self, fecha, accion, monto):
        self.registos[fecha] = f"{accion} ${monto}"

    def obtener_registros(self):
        return self.registos

    def __str__(self):
        return f"Info: {self.obtener_nombre_completo()}, numero de cuenta: {self.numero_de_cuenta}, balance: {self.balance}"

# Funciones del sistema

def crear_cliente(nombre, apellido):
    return Cliente(nombre, apellido)

def menu():
    return  int(input("""Ahora puedes: 
    [1] Depositar.
    [2] Retirar.
    [3] Consultar Balance. 
    [0] Salir.
    ¿Qué deseas hacer?: """))

def crear_registro(cliente, accion, monto):
    cliente.guardar_registro(obtener_fecha_y_hora_actual(), accion, monto)

def mostrar_registros(cliente):
    return cliente.obtener_registros()

def mostrar_balance(cliente):
    print(f"Tu cuenta tiene: ${cliente.obtener_balance()}")

def depositar_dinero(cliente):
    monto = float(input("Ingrese el monto que deseas depositar: $"))
    if cliente.depositar(monto):
        print(f"Transacción satisfactoria. Depositó ${monto} a su cuenta")
        crear_registro(cliente,"Transacción satisfactorea. Depositó", monto)

def retirar_dinero(cliente):
    monto = float(input("Ingrese el monto que deseas retirar: $"))
    if cliente.retirar(monto):
        print(f"Transacción satisfactoria. Retiró ${monto} de su cuenta")
        crear_registro(cliente, "Transacción satisfactorea. Retiró", monto)
    crear_registro(cliente, "Transacción erronea. trató de retirar", monto)
def main():
    opcion = int(input('Deseas abrir una cuenta en nuestro sistema? (1=si, 0=no): '))
    if opcion == 0:
        print("Lo sentimos. Contáctanos cuando desees sumarte y aprovechar todos nuestros beneficios como cliente.")
        return

    print("Haz tomado la mejor decisión..\nPor favor, para abrir una cuenta en nuestro sistema necesitamos que ingreses los siguientes datos:")
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    cliente = crear_cliente(nombre, apellido)
    print(f"Cliente: {cliente} creado satisfactoreamente.")

    print(f"Bienvenido al sistema, {cliente.obtener_nombre_completo()}.")
    while True:
        opcion = menu()

        if opcion == 0:
            print("Saliendo del sistema...")
            break
        elif opcion == 1:
            depositar_dinero(cliente)
        elif opcion == 2:
            retirar_dinero(cliente)
        elif opcion == 3:
            mostrar_balance(cliente)

    for fecha, registro  in mostrar_registros(cliente).items():
        print(f"Registro: {fecha} {registro}")

# Inicio
if __name__ == '__main__':
    print("### Bienvenido al Banco Américano ###")
    main()