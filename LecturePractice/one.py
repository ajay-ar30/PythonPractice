def func():
    print("FUNC in ONE.PY")

print("TOP LEVEL in ONE.PY")

if __name__ == '__main__':
    print("ONE.PY is being run directly!")
else:
    print("ONE.PY is imported")

'''
Purpose of __name__ == __main__ technique:

Basically you are splitting your .py scripts into two sections: i) function, class and object definitions, ii) running a series of functions and methods.
Your anticipation is that if you are running the script x directly, you want to execute the functions but if you are just importing the script x, 
you are only interested in importing the definitions segment from script x to use with function execution in script y.

'''