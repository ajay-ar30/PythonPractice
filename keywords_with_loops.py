# keywords with loops: break, continue, pass
# break - breaks out of the current closest enclosing loop
# continue - goes to the top of the closest enclosing loop
# pass - does nothing at all

x = [1,2,3]
for item in x:
    # using it as a filler to avoid getting an error
    pass

mystring = 'LAs Vegas'
for letter in mystring:
    if letter == 'a':
        continue
    print(letter)
    
for letter in mystring:
    if letter == 'a':
        # Will print all letters b4 'a' and break out of loop when 'a' encountered
        break
    print(letter)

x = 0
while x < 5:
    if x == 2:
        break
    print(x)
    x += 1