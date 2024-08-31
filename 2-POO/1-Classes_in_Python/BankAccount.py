class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True
    
    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f"Se ha depositado {amount}. Saldo actual {self.balance}")
        else:
            print("No se puede depositar, la cuenta está inactiva.")
    
    def withdraw(self, amount):
        if self.is_active:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Se a retirado {amount}. Saldo actual {self.balance}")
    
    def deactivate_account(self):
        self.is_active = False
        print("La cuenta fue desactivada correctamente.")
    
    def activate_account(self):
        self.is_active = True
        print("La cuenta fue activada correctamente.")

account1 = BankAccount("Ana", 500)
account2 = BankAccount("Luis", 100)

account1.deposit(200)
#>> Se ha depositado 200. Saldo actual 700
account2.deposit(100)
#>> Se ha depositado 100. Saldo actual 200

account1.deactivate_account()
#>> La cuenta fue desactivada correctamente.
account1.deposit(50)
#>> No se puede depositar, la cuenta está inactiva.

account1.activate_account()
#>> La cuenta fue activada correctamente.
account1.deposit(50)
#>> Se ha depositado 50. Saldo actual 750