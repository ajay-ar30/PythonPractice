# ordered sequences hold a variety of objects, use [] and commas to separate objects in the list
# supports indexing and slicing; can be nested and have variety of methods that can be called off of them

my_list = ['abc', 123, 1.2345]

print(len(my_list))

print('List object at index 2 is {}'.format(my_list[2]))

print(f'List object at index 1 is {my_list[1]}')

print('List objects index 1 onwards are {}'.format(my_list[1:]))

another_list = ['four', 'five']
new_list = my_list + another_list

print('Concatenated list is {}'.format(new_list))

# lists are mutable - values at indices can be modified

new_list[0] = 'ABC ALL CAPS'

print('Modified final list is {}'.format(new_list))

# add item to end of list - 

new_list.append('six')

print('Final list with item appended at end is {}'.format(new_list))

#removing items - pop removes from end by default (index -1 ) but index to remove can be specified 

print('Popped item is {}'.format(new_list.pop()))
print('New list with removed item from end is {}'.format(new_list))

print('Popped item at index 2 is {}'.format(new_list.pop(2)))

# list sorting - .sort doesn't return any value by itself, does sorting in place, 
# to print sorted list print() method to be used
# can also use sorted(list_name) to sort a list
char_list = ['l', 'o', 'a', 'e']
num_list = [11, 9, 5, 3, 8]
char_list.sort()
sorted_char_list = char_list
num_list.sort()
sorted_num_list = num_list
print('Sorted character list from index 1 onwards is {}'.format(sorted_char_list[1:]))
print('Sorted num list from index 1 onwards is {}'.format(sorted_num_list[1:]))

# list reversal - 
print('Reversed list without reverse method is {}'.format(num_list[::-1]))
num_list.reverse()
reversed_num_list = num_list
print('Reversed num list with reverse method is {}'.format(num_list))

# Index nested list - 

nested_list = [1,1,[1,2]]
print('Second object from list at index 2 of nested list is', nested_list[2][1])
