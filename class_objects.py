class Dog:
    species = "canine" # class attribute

    # Self represents the instance of the class. By using self we can access attributes and methods of the class in python

    def __init__(self,name,age):
        self.name = name # Instance attribute
        self.age = age # Instance attribute

# Object is the instance of the class. And consists of state(Rrpresented by attributes and properties of an object), 
# behaviour(represented by methods of an objectResponse of an object to oather object) and identity.

# Creating object

dog1 = Dog('Buddy',3)
print(dog1.name)
print(dog1.age)
print(dog1.species)

# Modifying instance of the class (Instance variables)
dog1.name = "king"
# Printing the modified attribute of a object instance
print(dog1.name)



