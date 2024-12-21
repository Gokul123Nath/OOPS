class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return "Some generic sound"

class Dog(Animal):
    def sound(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def sound(self):
        return f"{self.name} says Meow!"

# Usage
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.sound())  # Output: Buddy says Woof!
print(cat.sound())  # Output: Whiskers says Meow!
