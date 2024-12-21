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
