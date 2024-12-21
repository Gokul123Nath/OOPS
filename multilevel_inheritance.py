class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_name(self):
        print(f"Displaying name = {self.name}")

class Labrador(Dog) : # single inheritance

    def sound(self):
        print("Labrador Woofs")
    
class GuideDog(Labrador): # Multilevel inheritance (inherits properties of all the parent classes)

    def guide (self):
        print(f'{self.name} guides the way')
    
lab1 = Labrador("my lab", 2) # Have to give all the attributes should be given to the parent class 
lab1.display_name()
lab1.sound()
print(lab1.name)
print(lab1.age)

guide_dog = GuideDog("guider", 2)
guide_dog.display_name()
guide_dog.sound()
guide_dog.guide()

###########################################################################################################
# Complex multilevel inheritance with super keyword

class Animal:
    def __init__(self, name):
        self.name = name
        print("Animal Initialized")
    
    def speak(self):
        return "Animal makes a sound"

class Mammal(Animal):
    def __init__(self, name, has_fur):
        # Call the parent class initializer
        super().__init__(name)
        self.has_fur = has_fur
        print("Mammal Initialized")
    
    def speak(self):
        return super().speak() + " and Mammal sound"

class Dog(Mammal):
    def __init__(self, name, has_fur, breed):
        # Call the immediate parent class initializer
        super().__init__(name, has_fur)
        self.breed = breed
        print("Dog Initialized")
    
    def speak(self):
        return super().speak() + f" and Dog barks"

# Usage
dog = Dog("Buddy", True, "Golden Retriever")
print(dog.speak())

