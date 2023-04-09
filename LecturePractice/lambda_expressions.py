# map function: apply a function to all items in an iterable
# accepts a function and iterable as arguments. 
# User created func not called - only used as argument - map(function,iterable)

def square(nums):
    return nums**2

mynums = [1,2,3,4,5]
for item in map(square,mynums):
    print(item)
print(list(map(square,mynums)))

def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'EVEN'
    else:
        return mystring[0]

print(list(map(splicer,'Arvind')))
names = ['Adam', 'Stacy', 'Ronald']
print(list(map(splicer,names)))

# filter function: filter(function,iterable)

'''Construct an iterator from those elements of iterable for which function returns true. 
Iterable may be either a sequence, a container which supports iteration, or an iterator. 
If function is None, the identity function is assumed, that is, all elements of iterable that are false are removed.'''

def check_even(num):
    return num%2 == 0

mynums = [1,2,3,4,5,6]
print(list(filter(check_even,mynums)))

# lambda expressions: quickly create anonymous functions - reference once and never use again
# Above function can be written as -

lambda num: num%2 == 0
mynums2 = [1,2,3,4,5,6]
print(list(filter(lambda num: num%2 == 0, mynums2)))

# LEGB(Local, Enclosing func locals, Global, Built-in) Rule: specifies order by which python is going to look for variables in

'''LEGB Rule

Local — Names assigned in any way within a function (def or lambda), and not declared global in that function

Enclosing-function — Names assigned in the local scope of any and all statically enclosing functions (def or lambda), from inner to outer

Global (module) — Names assigned at the top-level of a module file, or by executing a global statement in a def within the file

Built-in (Python) — Names preassigned in the built-in names module: open, range, SyntaxError, etc

So, in the case of

code1
class Foo:
    code2
    def spam():
        code3
        for code4:
            code5
            x()
The for loop does not have its own namespace. In LEGB order, the scopes would be

L: Local in def spam (in code3, code4, and code5)
E: Any enclosing functions (if the whole example were in another def)
G: Were there any x declared globally in the module (in code1)?
B: Any builtin x in Python.
x will never be found in code2'''

x = 50

def func():
    # global keyword modifies value of x globally
    global x

    print(f'Value of x is {x}')

    # Local reassignment on a global variable - 

    x = 'NEW VALUE'
    print(f'Just locally changed value of global x to {x}')
print(x)
func()
print(x)

# Avoid using global keyword unless absolutely necessary
