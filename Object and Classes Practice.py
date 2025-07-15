# 1
# Create a class `Car` with attributes `brand` and `model`. Instantiate an object and print its attributes.
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        
    def __str__(self):
        return f"This is a {self.brand} {self.model}."

car1=Car("Toyota","Harrier")
car2=Car("BMW","M5")

print(car1)
print(car2)

# 2
# Define a class `Person` with attributes `name` and `age`, and a method `greet()` that returns a greeting message.
class Person:
    def __init__(self,name,age):
         self.name=name
         self.age=age
         
    def greet(self):
        return f"Thank you {self.name}"

p1=Person("Azad",19)
p2=Person("Shoppu",21)

print(p1.name,p1.age)
print(p2.name,p2.age)

p1.greet()
p2.greet()

# 3
# Build a class `Student` with a class variable `school` and an instance variable `name`.
# Create two objects and see how the variables behave.
class Student:
    School="ABC School"
    
    def __init__(self,name):
        self.name=name
        
    def __str__(self):
        return f"{self.name} studeis in {self.School}"
        
s1=Student("Alice")
s2=Student("Bob")

print(s1.name, s1.School)
print(s2.name, s2.School)

print(s1)
print(s2)

Student.School="Def School"

print(s1.name, s1.School)
print(s2.name, s2.School)

print(s1)
print(s2)

s2.School="XYZ School"

print(s1.name, s1.School)
print(s2.name, s2.School)

print(s1)
print(s2)

# 4
# Implement a class Bank Account with a private attribute __balance. Add methods to deposit, withdraw, and get balance.
class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def get_balance(self):
        print(f"Current balance: ${self.__balance}")
        return self.__balance

account = BankAccount(100)
account.deposit(50)
account.withdraw(30)
account.withdraw(200)
account.get_balance()
print(f"Current balance: ${account.get_balance()}")

# 5
#  a class with a private attribute, and access it using name mangling.
class Example:
    def __init__(self, value):
        self.__private_attr = value

    def get_private_attr(self):
        return self.__private_attr

obj = Example("Hidden Message")

print(f"Access via method: {obj.get_private_attr()}")

print(f"Access via name mangling: {obj._Example__private_attr}")

# OOP Story-Based Problem
class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name} studies in {Student.school}"

s1 = Student("Alice")
s2 = Student("Bob")
print(s1)
print(s2)

Student.school = "XYZ School"
print(s1)
print(s2)

class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def get_balance(self):
        return self.__balance

alice_account = BankAccount(100)
bob_account = BankAccount(200)

alice_account.deposit(50)
bob_account.withdraw(100)
print(f"Alice's balance: ${alice_account.get_balance()}")
print(f"Bob's balance: ${bob_account.get_balance()}")

class Example:
    def __init__(self, value):
        self.__private_attr = value

    def get_private_attr(self):
        return self.__private_attr

obj = Example("Hidden Message")

print(f"Access via method: {obj.get_private_attr()}")

print(f"Access via name mangling: {obj._Example__private_attr}")