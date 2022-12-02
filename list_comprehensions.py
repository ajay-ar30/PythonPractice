# quickly create lists
# good alternative in cases like using for loop along with .append() to create lists
# computational time same
# readability of code can get impacted when they get too complex

#make list of every letter in string
mystring = 'hello'
mylist = []
for letter in mystring:
    mylist.append(letter)
print(mylist)

# comprehension:
mylist2 = [item.upper() for item in mystring]
print(mylist2)

squarednumlist = [num**2 for num in range(0,11)]
print(squarednumlist)

evenlist = [num for num in range(0,11) if num%2==0]
print(evenlist)

celsius = [1, 10, 25, 36]
fahrenheit = [str((9/5)*temp + 32)+chr(176) for temp in celsius]
print(f'Temp in fahrenheit is {fahrenheit} fahrenheit')

results = [x if x %2==0 else 'ODD' for x in range(0,11)]
print(results)

# comprehension with nested loop:

xy_product = [x*y for x in [2,4,6] for y in [100,200,300]]
print(xy_product)