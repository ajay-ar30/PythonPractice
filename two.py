import one

print("Top Level in TWO.PY")

one.func()

if __name__ == '__main__':
    print("TWO.PY is being run directly!")
else:
    print("TWO.PY is imported")

'''Helps with code organization - function definitions at the top. function calling at the bottom'''
