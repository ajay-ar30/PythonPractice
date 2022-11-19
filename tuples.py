# represented by circular braces; slicing & indexing can be done.

t = ('One',2,3.0)
print('Element at index 1 is {}'.format(t[1]))

# two methods - count, index
# count() counts the no. of occurrences of an object
# index() gives the index of the first occurrence of the object
t1 = ('a','b','b','c','a')
print('The character at index {} occurred {} times'.format(t1.index('b'),t1.count('b')))

# similar to lists but are immutable - once element assigned at an index position it cannot be reassigned
# used when you dont want the values of objects in your program to be changed - data integrity maintained

# t1[0] = 'abcd' will return an error for tuples but not for lists

