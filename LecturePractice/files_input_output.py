myfile = open('myfile.txt')

# file reading - cursor will go to EOF on first read and needs to be taken back to start to read again.
print('Contents of file are',myfile.read())
# seek(0) method needs to be called after each read to reset cursor to start
myfile.seek(0)
# convert each line in file to a list of string objects
print('List of lines from file is ',myfile.readlines())
#Need to close after opened and used to avoid getting errors if accessed and to be modified in another application
myfile.close()
# two backslashes needed so python doesnt confuse it as escape character
myfile2 = open("C:\\Users\\aarora\\Desktop\\abc.txt")
print('List of lines from file is ',myfile2.readlines())
myfile2.seek(0)
myfile2.close()

# Not required to explicitly call close() to close file if with keyword is used to open
with open('myfile.txt') as my_new_file:
    print('Contents of file are',my_new_file.read())
    my_new_file.seek(0)
    print('Contents of file are',my_new_file.read())
    my_new_file.seek(0)
    print('List of lines from file is ',my_new_file.readlines())

# can specify file modes; default is r(read). Others - w(write), x(create new and open in write), a(append - add on to files)
# w(write),w+(write and read) - will overwrite existing file or create new if doesnt exist
# r+(read and write)

# mode = 'a' and 'r'
with open('myfile.txt',mode='a') as my_new_file2:
    my_new_file2.write('\nthis is the fourth line')

with open('myfile.txt', mode = 'r') as my_new_file3:
    print('Contents of file are',my_new_file3.read())
    my_new_file3.seek(0)
    print('Contents of file are',my_new_file3.read())
    my_new_file3.seek(0)
    print('List of lines from file is ',my_new_file3.readlines())

# mode = 'w'
with open('abcde.txt', mode='w') as f:
    f.write('First line')
    f.write('\nSecond line')
    f.write('\nThird line') 

with open('abcde.txt', mode='r') as readfile:
    print(readfile.read())        