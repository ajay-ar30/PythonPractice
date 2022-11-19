# unordered collection of unique elements(cannot have an element more than once).
myset = set()
myset.add(1)
myset.add(2)
print('Set after adding elements is {}'.format(myset))

#can cast list to make a set
mylist = [3,3,3,3,3,3,3,0,0,0,0,0,2,2,2,2,2]
print('Converted set from list is {}'.format(set(mylist)))

#Booleans - operators that convey True or False statements

a = True
print('Boolean result for expression 1>2 is {}'.format(1>2))
b = None
print('Data type of variable b is {}'.format(type(b)))