class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def parent1_print(self):
        print(f'Dog name is {self.name}, {self.age}')
    
class Friendly:

    def __init__(self, is_friendly):
        self.is_friendly = is_friendly

    def greet(self):
        print(f"Dog is friendly {self.is_friendly}")

class GoldenRetriever(Dog, Friendly):

    def __init__(self, name, age, is_friendly):
        # we have to initialize the instance attribute explicitly
        Dog.__init__(self, name, age)
        Friendly.__init__(self, is_friendly)

    def sound(delf):
        print("Retriever do woof")
    
golden_object = GoldenRetriever('Charlie',11,"yes")
golden_object.sound()
golden_object.greet()
golden_object.parent1_print()


# Super () keyword can be used to call the parent class and to resolve method resolution order (MRO)
class Animal:
    def __init__(self, name):
        self.name = name
        print("Animal Initialized")

class Friendly:
    def __init__(self, is_friendly):
        self.is_friendly = is_friendly
        print("Friendly Initialized")

class Trainable:
    def __init__(self, is_trainable):
        self.is_trainable = is_trainable
        print("Trainable Initialized")

class Dog(Animal, Friendly, Trainable):
    def __init__(self, name, is_friendly, is_trainable):
        # Use super to handle MRO and initialize all parent classes
        super().__init__(name)  # This calls Animal's __init__
        Friendly.__init__(self, is_friendly)  # Call Friendly explicitly
        Trainable.__init__(self, is_trainable)  # Call Trainable explicitly
        print("Dog Initialized")
    
    def details(self):
        return f"{self.name} - Friendly: {self.is_friendly}, Trainable: {self.is_trainable}"

# Create an instance of Dog
dog = Dog("Buddy", True, False)
print(dog.details())

#################################################################################################

# The below code shows the complex hierarchy

class Animal:
    def __init__(self, name, **kwargs):
        super().__init__(**kwargs)  # Pass remaining arguments to the next class in MRO
        self.name = name
        print("Animal Initialized")

class Friendly:
    def __init__(self, is_friendly, **kwargs):
        super().__init__(**kwargs)
        self.is_friendly = is_friendly
        print("Friendly Initialized")

class Trainable:
    def __init__(self, is_trainable, **kwargs):
        super().__init__(**kwargs)
        self.is_trainable = is_trainable
        print("Trainable Initialized")

class Dog(Animal, Friendly, Trainable):
    def __init__(self, name, is_friendly, is_trainable):
        super().__init__(name=name, is_friendly=is_friendly, is_trainable=is_trainable)
        print("Dog Initialized")
    
    def details(self):
        return f"{self.name} - Friendly: {self.is_friendly}, Trainable: {self.is_trainable}"

# Create an instance of Dog
dog = Dog("Buddy", True, False)
print(dog.details())
# Print the flow of init method execution
print(Dog.mro())

