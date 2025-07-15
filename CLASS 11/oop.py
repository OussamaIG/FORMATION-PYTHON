#how to declare a class
class Dog:
    #Attributes
    species = "Golden Retreiver" #class attribute shared

    #Methodes
    
    #constructor
    def __init__(self, name, age):
        #unique for each instance
        self.name = name
        self.age = age
    
    #personal method
    def bark(self):
        print(f"{self.name} says : Woof !")
