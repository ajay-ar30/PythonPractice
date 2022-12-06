mylist = [1,2,3,4]
# insert object before specified index
mylist.insert(1,'new')

print(mylist)

# functions: blocks of code that can be executed multiple times without needing to re-write the code
# snake casing for function_names for better readability

def hello_user(name):
    print("Hello "+name)

hello_user("Ajay")

# return keyword to be used commonly; allows to assign output of function to a variable
# print function doesn't allow, can use both print & return in function body
# break out of loop once return encountered
def adding(num1,num2):
    return num1+num2

result = adding(3,5)
print('Sum is ', result)

# can add default value for arguments

def say_hello(name='Default name boi'):
    print(f'{name} put some respek on it')

say_hello()

def even_check(num):
    return num % 2 == 0
even_check(35)

def check_even_list(numlist):
    # placeholder list
    even_nums = []
    for num in numlist:
        if num%2 == 0:
            even_nums.append(num)
        else:
            pass
    return even_nums

check_even_list([1,2,4,3,5])

# tuple unpacking with functions:
work_hours = [('Abby',100),('Sam', 400),('Adam', 700)]

def employee_check(work_hours):
    current_max = 0
    employee_of_month = ''
    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass
    return (employee_of_month, current_max)
# unpacking
name,hours = employee_check(work_hours)
print(name)
print(hours)

# error thrown if another variable added after name, hours because function returns 2 values only
# can assign function call to 1 variable and print that variable to check how many values

'''-----------------------------------'''

'''Interactions between functions
Functions often use results from other functions, let's see a simple example through a guessing game. 
There will be 3 positions in the list, one of which is an 'O', a function will shuffle the list, another will take a player's guess, 
and finally another will check to see if it is correct. 
This is based on the classic carnival game of guessing which cup a red ball is under.'''

# custom shuffle function:
from random import shuffle
example_list = [1,2,3,4,5,6,7,8,9,10]
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

result = shuffle_list(example_list)
print('Shuffled list is ',result)

# guessing game:
my_game_list = ['','O','']
def shuffle_game_list(my_game_list):
    shuffle(mylist)
    return mylist
shuffle_game_list(mylist)

def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input("Pick a number: 0,1 or 2")
    return int(guess)
myindex = player_guess() 

def check_guess(mylist, guess):
    if mylist[guess] == 'O':
        print("Correct guess!")
    else:
        print("Wrong guess! List is:",mylist)
        
# Initial List
mylist1 = ['','O','']
# Shuffled List
mixed_list = shuffle_game_list(mylist1)
# User guess
guess = player_guess()
# Check guess
check_guess(mixed_list, guess)

# *args and **kwargs - arguments and keyword arguments (function parameters):
def myfunc(a,b):
    return sum((a,b))*.05

myfunc(40,60)

'''This function returns 5% of the sum of a and b. In this example, a and b are positional arguments; that is, 40 is assigned to a 
because it is the first argument, and 60 to b. To work with multiple positional arguments in the sum() function we had to pass them in as a tuple.

What if we want to work with more than two numbers? One way would be to assign a lot of parameters, and give each one a default value.'''

def myfunc(a=0,b=0,c=0,d=0,e=0):
    return sum((a,b,c,d,e))*.05

myfunc(40,60,20)

''' *args:

When a function parameter starts with an asterisk, it allows for an arbitrary number of arguments, and the function takes them in as a tuple 
of values. Rewriting the above function:'''

def myfunc(*args):
    return sum(args)*.05

myfunc(40,60,20)

''' The word "args" is itself arbitrary - any word will do so long as it's preceded by an asterisk. 
By convention always use *args for easy code understanding '''

def myfunc(*spam):
    return sum(spam)*.05

myfunc(40,60,20,50,70,80,90)

''' **kwargs - outputs a dictionary '''
def myfunc(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('Selected fruit is {}'.format(kwargs['fruit']))
    else:
        print('No fruits present')
myfunc(fruit='banana',vegs='spinach')

# *args and **kwargs combined:
def myfunc(*args,**kwargs):
    print(args)
    print(kwargs)
    print('Please give me {} {} and {} {}'.format(args[0],kwargs['food'],args[1],kwargs['fruit']))
myfunc(10,20,30,40,fruit='apples',food='eggs')

'''Define a function called myfunc that takes in a string, and returns a matching string where every even letter is uppercase, 
and every odd letter is lowercase. Assume that the incoming string only contains letters, and don't worry about numbers, spaces or punctuation. 
The output string can start with either an uppercase or lowercase letter, so long as letters alternate throughout the string.'''


# example: myfunc('Anthropomorphism')
# Output: 'aNtHrOpOmOrPhIsM'

def myfunc(name):
    mylist = []
    for letter in range(len(name)):
        if letter % 2 == 0:
            mylist.append(name[letter].upper())
        else:
            mylist.append(name[letter].lower())
    return ''.join(mylist)

myfunc('abracadabra')    

