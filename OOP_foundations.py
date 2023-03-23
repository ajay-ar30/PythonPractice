'''
class name in CamelCase. Function inside an object or inside class call is called a method. self keyword used. User defined objects are created using the class keyword. 
The class is a blueprint that defines the nature of a future object. From classes we can construct instances. An instance is a specific object created from a particular class. 


Methods are functions defined inside the body of a class. They are used to perform operations with the attributes of our objects. 
Methods are a key concept of the OOP paradigm. They are essential to dividing responsibilities in programming, especially in large applications.
You can basically think of methods as functions acting on an Object that take the Object itself into account through its self argument.

'''

class NameOfClass():
    def __init__(self, param1, param2): #create instance of an object. Called whenever you create an instance of a class
        self.param1 = param1 #linking to actual object using self keyword
        self.param2 = param2
    
    def some_method(self):
        #perform some action
        print(self.param1)

class Sample():
    pass

my_sample = Sample() #instance of class
print(type(my_sample))

class Dog():
    #Class object atribute: Same for any instance of class. Basically factual info.
    classification = 'mammal' #not using self keyword. It will be true regardless of class instance
    def __init__(self,breed,name,spots):
        #We take in the argument
        #Assign it using self.attribute_name
        self.breed = breed
        self.name = name
        #Expecting boolean True/False
        self.spots = spots
        #Operations/Actions -> Methods
    def bark(self,number):
        print(f"Woof! My name is {self.name} and number is {number}") #not adding self with number as number is to be provided in method call

my_dog = Dog(breed='BullDog', name = 'Bronco', spots = True) #instance of class
print(my_dog.bark(1))

my_dog2 = Dog('Lab','dawg',False)
print(my_dog2.bark(2))

class Circle():
    #class object attribute
    pi = 3.14
    def __init__(self,radius = 1):
        self.radius = radius
        self.area = radius * radius * self.pi #can also use Circle.pi
    def get_circumference(self):
        return self.radius * Circle.pi * 2
    
class_instance = Circle(30) #overwrites existing value of radius
print(class_instance.area)
print(class_instance.get_circumference())