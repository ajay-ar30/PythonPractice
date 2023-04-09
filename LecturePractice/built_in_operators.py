# range(start,stop,step)
# it is a generator - a function that will generate info but not save all of it to memory
for num in range(0,11,2):
    print(num)
print('List of even numbers in range is {}'.format(list(range(0,11,2))))

index_count = 0
for letter in 'abcdef':
    print('Letter at index {} is {}'.format(index_count, letter))
    index_count += 1

# enumerate: accepts any iterable, returns index and value at index, default output is in form of tuple with index and value
word = 'ABCDEFGH'
for index,letter in enumerate(word):
    print(index, letter)
    print('---')

# zip: zips together 2 or more lists. length of final output tuple = length of shortest list

mylist1 = [1,2,3,4]
mylist2 = ['a','b','c','d','e']
mylist3 = [6,7,8]

for element in zip(mylist1,mylist2,mylist3):
    print(element)

# min(), max():

print(min(mylist1))
print(max(mylist2))

# random library:
# shuffle function randomly shuffles around in a list; doesnt return anything, shuffles in-place, not iterable because NoneType
from random import shuffle
random_list = shuffle(mylist2)
print(random_list)

# randint: random integer between 2 numbers, not of NoneType
from random import randint
print(randint(2,65))

#User input: always accepts anything passed to it as a string, numbers need to be typecasted as needed
username = input('What is your name?')
age = int(input('Please enter your age'))
print(f'My name is {username} and I am {age} years old')