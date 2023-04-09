#string interpolation - injecting a variable in a string
#two methods - .format(), f-strings(formatted string literals)

#.format() syntax - 'String here {} then also {}'.format('something1','something2')
print('This is a string {}'.format('inserted'))

print('The {} {} {}'.format('fox','brown','quick'))

print('The {2} {1} {0}'.format('fox','brown','quick'))

print('The {0} {1} {1}'.format('fox','brown','quick'))

#can also insert by keyword/variable assignment instead of index assignment - easy to work with

print('The {q} {b} {f}'.format(f='fox',b='brown',q='quick'))

#float number formatting -"{value:width.precision f}"

result = 100/777

print('The result was {r}'.format(r=result))

# width is for whitespace, precision is how many numbers after decimal you want

print('The result was {r:10.3f}'.format(r=result)) # rounds off when possible

print('The result was {r:2.5f}'.format(r=result))

# f-strings
name = 'ajay'
print(f'Hello, my name is {name}')

result = 26.76982
print(f'Value of result is {result:2.3f}') # rounds off when possible

print(f'Value of result is {result:2.4f}')

f='fox'
b='brown'
q='quick'

print(f'The {q} {b} {f}')