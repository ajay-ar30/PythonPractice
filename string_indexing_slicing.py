#strings are ordered sequences

#indexing (forward or reverse): extracting one character from an index position

# forward -
mystring = "hello world"

# forward index "0,1,2,3,4" reverse "0,-4,-3,-2,-1"

print("Character at index 4 is",mystring[4])

#reverse indexing-

print("character at index -3 is",mystring[-3])

#slicing: grab a subsection of multiple characters (a slice of the string)

#syntax- [start:stop:step]

#start-numerical index for slice start
#stop-index you will go upto (but not include)
#step-size of jump you take

mystring2 = "abcdefghijk"

print("Sliced string from index 2 is", mystring2[2:])
print("Sliced string from index 0 to 3 is",mystring2[:3])
print("Sliced string from index 3 to 5 is",mystring2[3:6])
print("String from start to end using slicing is", mystring2[::])
print("String from start to end with jump size of 2 is",mystring2[::2])
print("Reversed string is",mystring2[::-1])

mystring3= "tinker"
print("Sliced string from index 1 to 4 is",mystring3[1:4])