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

# custom shuffle function

from random import shuffle
example_list = [1,2,3,4,5,6,7,8,9,10]
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

result = shuffle_list(example_list)
print('Shuffled list is ',result)
