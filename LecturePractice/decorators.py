'''Decorators can be thought of as functions which modify the functionality of another function. 
They help to make your code shorter and more "Pythonic".'''

def hello():
    return "Hello"

greet = hello

del hello

greet()

def hello(name='Ajay'):
    print("The hello function has been executed")

    def greet():
        return "\t This is greet() function inside hello"
    
    def welcome():
        return "\t This is welcome() function inside hello"
    
    print(greet())
    print(welcome())
    print("This is the end of the hello function")

hello()
#Scope of greet and welcome only in hello function. Cannot call them separately. Can just call hello which calls them.
def hello2(name='Ajay'):
    print("The hello function has been executed")

    def greet2():
        return "\t This is greet() function inside hello"
    
    def welcome2():
        return "\t This is welcome() function inside hello"
    
    print(greet2())
    print(welcome2())
    print("Will return a function based on name")

    if name == 'Ajay':
        return greet2()
    else:
        return welcome2()
hello2('Abdul')

def hello3():
    return 'Hi Ajay'

def other(func):
    print('Other code would go here')
    print(func())
other(hello3)

def new_decorator(original_func):
    #extra functionality that you want to decorate original func with.
    def wrap_func():
        print("Some extra code before original function")
        original_func()
        print("Some extra code after original func")
    return wrap_func

def func_needs_decorator():
    print("I want to be decorated")

decorated_func = new_decorator(func_needs_decorator)
decorated_func()
# Instead of calling decorated_func as done above can use the decorator syntax with @- 
@new_decorator
def func_needs_decorator():
    print("I want to be decorated")
func_needs_decorator()