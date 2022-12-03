#Use for, .split(), and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'
splitlist = st.split()
for letter in splitlist:
    if letter[0] == 's':
        print(letter)

# Use range() to print all the even numbers from 0 to 10.
for num in range(0,11):
    if num%2 == 0:
        print(num)

# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

mynumlist = [num for num in range(1,51) if num%3==0]
print(mynumlist)

# Go through the string below and if the length of a word is even print "even!"

st2 = 'Print every word in this sentence that has an even number of letters'
st2 = st2.split()
for text in st2:
    if len(text) % 2 == 0:
        print(text,":","even!")

# Write a program that prints the integers from 1 to 100. 
# But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". 
# For numbers which are multiples of both three and five print "FizzBuzz".

for num in range(1,101):
    if (num%3 == 0) and (num%5 == 0):
        print(num,"FizzBuzz")
    elif num%3 == 0:
        print(num,"Fizz")
    elif num%5 == 0:
        print(num,"Buzz")
    else:
        print(num)

# Use List Comprehension to create a list of the first letters of every word in the string below:

st = 'Create a list of the first letters of every word in this string'
st = st.split()
stringlist = [letter[0] for letter in st]
print(stringlist)
        
