# Abstraction hides the internal implementation while exposing necessary functionality and focuses on 
# what to do instead of how to do?

# Types of abstraction :
        # 1. Partial abstraction - Abstract class contains both abstract and concrete methods
        # 2. Full abstraction - Abstract class contains only abstract methods (Like interfaces).

# Abstraction is typically achieved through the abstract classes and abstract methods.

# Key concepts of data abstraction

    # Abstract class   : Classes that cannot be instantiated and are meant to be subclassed
    # Abstract Methods : Methods that are defined in an abstract class but lacks implement and must be implemented by subclass
    # Encapsulation    : Hiding internal states and requiring all interaction to be performed through well defined interfaces 
    #                    (often combined with abstraction)


# Defining the abstract base class using ABS (Abstract Base Class) module in python

from abc import ABC, abstractmethod
import math

class shape(ABC):

    @abstractmethod
    def area(self):
        # Just abstract method without implementation
        pass

    @abstractmethod
    def perimeter(self):
        # Just abstract method without implementation
        pass

# Subclass rectangle that implements shape

class Rectangle(shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2*(self.width + self.height)

# Subclass circle that implements shape

class Circle(shape):

    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius**2
    
    def perimeter(self):
        return 2* math.pi * self.radius
    
# Now client code to work with the shapes

def print_shape_details(shape):

    print(f"area      : {shape.area()}")
    print(f"Perimeter : {shape.perimeter()}")

rect = Rectangle(5,10)
circle = Circle(4)

print("Rectangle details :")
print_shape_details(rect)
print("Circle Details :")
print_shape_details(circle)
