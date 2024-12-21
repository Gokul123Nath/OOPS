# Polymorphism allows methods to have same name but behave differently based on the object's context.
# This can be achieved through method overriding and method overloading

# Types of polymorphism
#     1. Compile time polymorphism - This is determined during the compilation time of the program. It allows methods or operators with
#                                    the same name to behave differently based on their input parameters or usage. It is referred to as
#                                    method or operator overloading
#     2. Run time polymorphism     - This type of polymorphism is determined during the execution of the program. This happens when a 
#                                    sub class provides different implementation for a method that is already defined in the parent class.
#                                    commonly known as method overriding.


# Runtime polymorphism or method overriding

class Dog:

    def sound(self):
        print("Dog barks")
    
class Labrador (Dog):

    def sound(self):
        print("Overridden method, labrador woofs")
    
obj = Labrador()
obj.sound()

#####################################################################################

# Complex program for method overriding

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return f"{self.name} makes a generic sound."

class Mammal(Animal):
    def __init__(self, name, has_fur):
        super().__init__(name)
        self.has_fur = has_fur

    def sound(self):
        base_sound = super().sound()  # Call the parent method
        fur_info = f"{self.name} {'has' if self.has_fur else 'does not have'} fur."
        return f"{base_sound} {fur_info}"

class Dog(Mammal):
    def __init__(self, name, has_fur, breed):
        super().__init__(name, has_fur)
        self.breed = breed

    def sound(self):
        base_sound = super().sound()  # Call the parent method
        return f"{base_sound} Also, {self.name} ({self.breed}) says Woof!"

# Usage
dog = Dog("Buddy", True, "Golden Retriever")
print(dog.sound())

# Method overloading or compile time polymorphism

class Calculator:
    def calculate(self, *args, operation=None, **kwargs):
        """
        A flexible method to perform different calculations based on input types and the operation.
        """
        if len(args) == 2 and operation in ['add', 'subtract', 'multiply', 'divide']:
            return self._basic_operations(args[0], args[1], operation)
        elif 'numbers' in kwargs and operation == 'sum_all':
            return self._sum_all(kwargs['numbers'])
        elif isinstance(args[0], str) and operation == 'length':
            return self._string_length(args[0])
        else:
            raise ValueError("Invalid arguments or operation not supported")

    def _basic_operations(self, a, b, operation):
        if operation == 'add':
            return a + b
        elif operation == 'subtract':
            return a - b
        elif operation == 'multiply':
            return a * b
        elif operation == 'divide':
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return a / b

    def _sum_all(self, numbers):
        if not all(isinstance(num, (int, float)) for num in numbers):
            raise ValueError("All elements must be numeric")
        return sum(numbers)

    def _string_length(self, text):
        return len(text)

# Usage
calc = Calculator()

# Case 1: Basic operations
print(calc.calculate(10, 5, operation='add'))         # Output: 15
print(calc.calculate(10, 5, operation='subtract'))    # Output: 5
print(calc.calculate(10, 5, operation='multiply'))    # Output: 50
print(calc.calculate(10, 5, operation='divide'))      # Output: 2.0

# Case 2: Summing all numbers
print(calc.calculate(operation='sum_all', numbers=[1, 2, 3, 4, 5]))  # Output: 15

# Case 3: String length calculation
print(calc.calculate("Hello, World!", operation='length'))  # Output: 13

