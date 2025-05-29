from abc import ABC, abstractmethod

class BankAccount(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def checkbalance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance

class LoanAccount(BankAccount):
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance -= amount
        return self.balance

    def withdraw(self, amount):
        self.balance += amount
        return self.balance





# b = BankAccount()  # This will raise an error because BankAccount is abstract and cannot be instantiated


sa = SavingsAccount(100)
print(sa.deposit(50))  # Output: 150
print(sa.withdraw(20))  # Output: 120
print(sa.checkbalance())  # Output: 120