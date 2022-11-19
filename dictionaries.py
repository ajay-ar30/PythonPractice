# unordered mappings for storing objects - key-value pairs; dont need to know index location
# cannot be sorted , item additions happen wherever dictionary deems necessary

prices_lookup = {'apple': 3.25, 'banana': 4.10, 'chocolate': 5.50}
print('Price of apple is {}'.format(prices_lookup['apple']))

# can hold other lists or dictionaries
d = {'k1': 22, 'k2': ['a','b','c', 'd', 'e'], 'k3': {'insidekey': 56}}

print('Value of k1 is {}, 2nd element from k2 is {}, inside key from k3 is {}'.format(d['k1'], d['k2'][1], d['k3']['insidekey']))
print('Uppercase value of 2nd element from k2 is {} '.format(d['k2'][1].upper()))
print('Popped element from index 2 of list from key k2 is {}'.format(d['k2'].pop(2)))
print('Updated value of list from key k2 is {}'.format(d['k2']))

# Adding new key-value pair or modifying existing:

d['k4'] = 450
d['k1'] = 35

print('Updated dictionary after adding new/modifying existing values is {}'.format(d))

# dictionary methods - output will be enclosed in circular braces called tuples

print('Keys of dictionary are {}'.format(d.keys()))
print('Values of dictionary keys are {}'.format(d.values()))
print('Items of dictionary are {}'.format(d.items()))

#Python has a built-in method of doing a self subtraction or addition (or multiplication or division).
# setting object to itself minus 250
d['k4'] -= 250
print(d['k4'])
