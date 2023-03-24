'''
class name in CamelCase. Function inside an object or inside class call is called a method. self keyword used. User defined objects are created using the class keyword. 
The class is a blueprint that defines the nature of a future object. From classes we can construct instances. An instance is a specific object created from a particular class. 


Methods are functions defined inside the body of a class. They are used to perform operations with the attributes of our objects. 
Methods are a key concept of the OOP paradigm. They are essential to dividing responsibilities in programming, especially in large applications.
You can basically think of methods as functions acting on an Object that take the Object itself into account through its self argument.

Functions can take different arguments but methods belong to the Object that they act on.

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

'''
Inheritance - form new classes based on already defined classes. The newly formed classes are called derived classes, the classes that we derive from are called base classes. 
Important benefits of inheritance are code reuse and reduction of complexity of a program.The derived classes (descendants) override or extend the functionality of base classes(ancestors).

'''

class Animal(): # base class
    def __init__(self):
        print("Animal created")
    def who_am_i(self):
        print("I am an animal")
    def eat(self):
        print("I like to eat")

class Dog2(Animal): # Derived class. Instance of base class will also be created when you create instance of derived class
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")
    def who_am_i(self): # Can override previously created method
        return "I am a dog" 
    def walks(self): # Can add new methods
        return "I like to go for walks"

mydog2 = Dog2()
print(mydog2.who_am_i()) # will print overridden value
print(mydog2.walks())

'''
Polymorphism: In Python, polymorphism refers to the way in which different object classes can share the same method name, 
and those methods can be called from the same place even though a variety of different objects might be passed in.
'''

class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name+' says Woof!'
    
class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name+' says Meow!' 
    
niko = Dog('Niko')
felix = Cat('Felix')

print(niko.speak())
print(felix.speak())

for pet in [niko,felix]:
    print(type(pet))
    print(pet.speak())

def pet_speak(pet):
    return pet.speak()

pet_speak(niko)
pet_speak(felix)

'''Abstract class: A class that never expects to be instantiated. 
For example, we will never have an Animal object, only Dog and Cat objects, although Dogs and Cats are derived from Animals:'''

class Animal:
    def __init__(self, name):    # Constructor of the class
        self.name = name

    def speak(self):              # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")


class Dog(Animal):
    
    def speak(self):
        return self.name+' says Woof!'
    
class Cat(Animal):

    def speak(self):
        return self.name+' says Meow!'
    
fido = Dog('Fido')
isis = Cat('Isis')

print(fido.speak())
print(isis.speak())

'''Real life examples of polymorphism include:

opening different file types - different tools are needed to display Word, pdf and Excel files
adding different objects - the + operator performs arithmetic and concatenation'''

'''Special Methods: 
Classes in Python can implement certain operations with special method names. These methods are not actually called directly but by Python specific language syntax. 

For example let's create a Book class:'''

class Book:
    def __init__(self, title, author, pages):
        print("A book is created")
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: %s, author: %s, pages: %s" %(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book is destroyed")
book = Book("Python Rocks!", "Jose Portilla", 159)

#Special Methods
print(book)
print(len(book))
del book
#A book is created
#Title: Python Rocks!, author: Jose Portilla, pages: 159
#159
#A book is destroyed
'''The __init__(), __str__(), __len__() and __del__() methods
These special methods are defined by their use of underscores. They allow us to use Python specific functions on objects created through our class.'''