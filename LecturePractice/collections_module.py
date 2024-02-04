'''
Built-in python module.
Implements specialized container data types i.e. alternatives to python's built-in containers.
container meaning dictionary, tuple etc.
'''
from collections import Counter #Counter is dictionary sub-class that helps to count hashable objects

mylist = [1,1,1,1,'a','b','b',3,4,5,6,4,4,4,4]

c = Counter(mylist)

print(c,"\n")

sentence = 'How many times does each word appear in this sentence?'

Counter(sentence.split())

c2 = Counter(sentence.lower().split())

print(c2,"\n")

print(c.most_common(),"\n") # to check for most common item in the list. Result will be in the form of tuples.
print(c.most_common(2)) # N most common items

'''defaultdict

defaultdict is a dictionary-like object which provides all methods provided by a dictionary 
but takes a first argument (default_factory) as a default data type for the dictionary. 
Using defaultdict is faster than doing the same using dict.set_default method.

A defaultdict will never raise a KeyError. 
Any key that does not exist gets the value returned by the default factory.'''

from collections import defaultdict

d  = defaultdict(lambda:0) # lambda keyword to set default values.

print(d['AJAY'])

'''namedtuple

The standard tuple uses numerical indexes to access its members, for example:

t = (12,13,14)
t[0]
12

A namedtuple assigns names, as well as the numerical index, to each member.

Each kind of namedtuple is represented by its own class, 
created by using the namedtuple() factory function. 
The arguments are the name of the new class and a string containing the names of the elements.

example - Dog = namedtuple('Dog',['age','breed','name'])

You can basically think of namedtuples as a very quick way of creating a new object/class type 
with some attribute fields. '''

from collections import namedtuple
Dog = namedtuple('Dog',['age','breed','name'])

sam = Dog(age=2,breed='Lab',name='Sammy')

frank = Dog(age=2,breed='Shepard',name="Frankie")

'''
We construct the namedtuple by first passing the object type name (Dog) 
and then passing a string with the variety of fields as a string with spaces between the field names. 
We can then call on the various attributes.
'''

print(sam.age,frank.name)

git config --global user.email "you@example.com"
  git config --global user.name "Your Name"