# unordered mappings for storing objects - key-value pairs; dont need to know index location
# cannot be sorted , item additions happen wherever dictionary deems necessary

prices_lookup = {'apple': 3.25, 'banana': 4.10, 'chocolate': 5.50}
print('Price of apple is {}'.format(prices_lookup['apple']))

# can hold other lists or dictionaries
d = {'k1': 22, 'k2': [0,4,1], 'k3': {'insidekey': 56}}

print('Value of k1 is {}, 2nd element from k2 is {}, inside key from k3 is {}'.format(d['k1'], d['k2'][1], d['k3']['insidekey']))
