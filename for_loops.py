# iterate over characters in a string, items in a list, keys in a dictionary etc. - basically go thru every item in an iterable object.
# syntax:

my_iterable = [1,2,3,4,5,6,7,8,9,10]
#item_name - placeholder for every item in the iterable; can also use _ in its place
for item_name in my_iterable: 
    # Check if number is even
    if item_name%2==0:
        print('{} is even'.format(item_name))
    else:
        print('{} is odd'.format(item_name))    

# using list_sum as a counter initialized by 0
my_list = [2,4,6,8,10,1,3,5,]
list_sum = 0
# iterating over sorted list starting from index 4 till end
for item in sorted(my_list[4:]):
    list_sum = list_sum + item
    print(f'Sum is: {list_sum}')

for each_item in my_list:
    list_sum = list_sum + each_item

print(f'Total sum of all items is: {list_sum}')

# iterating through a string typecasted as a set
mystring = 'Mississippi'
for letter in set(mystring):
    print(letter)

# tuple unpacking:

mylist = [(1,2),(5,6),(11,12),(3,4)]
# for tuple in list:
for (a,b) in sorted(mylist):
# can also type as for a,b in sorted(mylist)
    print(a)
    print(b)

# looping thru a dictionary: by default keys are printed
d = {'k1':'abc', 'k2': 123, 'k3': 4.56}
for item in d:
    print(item)

# to print value:
for key,value in d.items():
# can also do: for value in d.values()
    print(value)

# to print keys either use default way or replace d.items() by d.keys()  