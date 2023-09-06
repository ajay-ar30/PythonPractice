'''Generator functions allow us to write a function that can send back a value and then later resume to pick up where it left off. 
This type of function is a generator in Python, allowing us to generate a sequence of values over time. The main difference in syntax will be the use of a yield statement.

when a generator function is compiled they become an object that supports an iteration protocol. That means when they are called in your code they don't actually return a value and then exit. 
Instead, generator functions will automatically suspend and resume their execution and state around the last point of value generation. 

The main advantage here is that instead of having to compute an entire series of values up front, the generator computes one value and then suspends its activity awaiting the next instruction. 
This feature is known as state suspension and makes it memory efficient due to all set of values not being stored upfront as is done for e.g using .append() for existing list in memory.'''

#Example:

#normal function:

def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result

create_cubes(3)

# generator:

def create_squares(n):
    for x in range(n):
        yield x**2
for x in create_squares(5):
    print(x)
# can cast as list too - list(create_squares(5))

def gen_fibon(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        #tuple matching
        a,b=b,a+b
for number in gen_fibon(5):
    print(number) 

#next() and iter() built-in functions:
# The next() function allows us to access the next element in a sequence.

def simple_gen():
    for x in range(3):
        yield x
for num in simple_gen():
    print(num)
# Assign simple_gen 
g = simple_gen()

print(next(g))
print(next(g))

# iter():

s = 'hello'

#Iterate over string
#for let in s:
#    print(let)

s_iter = iter(s)

# Now we can use next() to access next values in iterable.

next(s_iter)
next(s_iter)

# Create a generator that generates the squares of numbers up to some number N.

def create_squares(n):
    for x in range(n):
        yield x**2
for x in create_squares(10):
    print(x)

# Create a generator that yields "n" random numbers between a low and high number (that are inputs).
# Note: Use the random library.     

import random

def rand_num(low,high,n):
    for i in range(n):
        yield random.randint(low,high)

for num in rand_num(1,10,12):
    print(num)

# Explain a use case for a generator using a yield statement where you would not want to use a normal function with a return statement.
'''If the output has the potential of taking up a large amount of memory and you only intend to iterate through it, you would want to use a generator.
 '''
#Can you explain what gencomp is in the code below?

my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)

# generator comprehension using list comprehension.

