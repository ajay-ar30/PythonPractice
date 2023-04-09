def ask_for_int():
    while True:
        try:
            result = int(input("Please provide a number"))
        except:
            print("That is not a number")
            continue
        else:
            print(f"Thank you for providing the number {result}")
            break
        finally:
            print("End of try/except/finally")
            print("I will execute no matter what")
ask_for_int()

'''
Problem 1
Handle the exception thrown by the code below by using try and except blocks.
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-1-c35f41ad7311> in <module>()
      1 for i in ['a','b','c']:
----> 2     print(i**2)

TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'

'''

try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print("Cannot calculate the square of string values")

'''
Problem 2
Handle the exception thrown by the code below by using try and except blocks. 
Then use a finally block to print 'All Done.'
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-2-6f985c4c80dd> in <module>()
      2 y = 0
      3 
----> 4 z = x/y

ZeroDivisionError: division by zero
'''

x = 5
y = 0

try:
    z = x/y
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("All done!")

'''
Problem 3
Write a function that asks for an integer and prints the square of it. 
Use a while loop with a try, except, else block to account for incorrect inputs.

Input an integer: null
An error occurred! Please try again!
Input an integer: 2
Thank you, your number squared is:  4
'''
def ask():
    while True:
        try:
            result = int(input("Input an integer:"))
        except ValueError:
            print("That is not an integer. Please try again")
            continue
        else:
            print(f"Thank you, your number squared is: {result**2}")
            break
ask()
