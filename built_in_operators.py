# range(start,stop,step)
# it is a generator - a function that will generate info but not save all of it to memory
for num in range(0,11,2):
    print(num)
print('List of numbers in range is {}'.format(list(range(0,11,2))))

index_count = 0
for letter in 'abcdef':
    print('Letter at index {} is {}'.format(index_count, letter))
    index_count += 1

