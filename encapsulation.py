# Encapsulation is the bundling of data (attributes) and methods (functions) with in a class, restricting
# access to some components to control interactions.

# Types of encapsulation 
#         1. Public members - Accessible from anywhere
#         2. Protected members - Accessible within the class and its subclass
#         3. Provate members - Accessible within only the class (Access requires getter and setter methods)

class Dog:
    def __init__(self, name, breed, age):
        self.name = name  # Public attribute
        self._breed = breed  # Protected attribute
        self.__age = age  # Private attribute

    # Public method
    def get_info(self):
        return f"Name: {self.name}, Breed: {self._breed}, Age: {self.__age}"

    # Getter and Setter for private attribute
    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age!")

# Example Usage
dog = Dog("Buddy", "Labrador", 3)

# Accessing public member
print(dog.name)  # Accessible

# Accessing protected member
print(dog._breed)  # Accessible but discouraged outside the class

# Accessing private member using getter
print(dog.get_age())

# Modifying private member using setter
dog.set_age(5)
print(dog.get_info())

class BankAccount:
    def __init__(self, account_holder, balance):
        self.__account_holder = account_holder  # Private attribute
        self.__balance = balance                # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New Balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}. Remaining Balance: {self.__balance}")
        else:
            print("Insufficient balance.")

    def get_balance(self):
        return self.__balance

# Usage
account = BankAccount("John Doe", 5000)
# print(account.__balance)  # Raises AttributeError
account.deposit(1500)
account.withdraw(3000)
print("Final Balance:", account.get_balance())
