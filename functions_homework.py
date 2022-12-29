'''Write a function that computes the volume of a sphere given its radius.

The volume of a sphere is given as 4/3πr^3'''

def vol(rad):
    π = 3.14
    return (4/3)*π*rad**3
vol(2)

'''Write a function that checks whether a number is in a given range (inclusive of high and low)
def ran_check(num,low,high):
    pass
# Check
ran_check(5,2,7)
5 is in the range between 2 and 7
If you only wanted to return a boolean:

def ran_bool(num,low,high):
    pass
ran_bool(3,1,10)
True
'''

def ran_check(num,low,high):
    if num in range(low,high+1):
        return f'{num} is in the range between {low} and {high}'
    else:
        return f'{num} is not in the range between {low} and {high}'
ran_check(5,2,7)

'''Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
Expected Output : 
No. of Upper case characters : 4
No. of Lower case Characters : 33

HINT: Two string methods that might prove useful: .isupper() and .islower()

pull uppercase letters add to a list, pull lower case add to list print len of lists

If you feel ambitious, explore the Collections module to solve this problem!'''

def up_low(s):
    counter = 0
    up_list = []
    low_list = []
    for chars in s:
        if chars.isupper() == True:
            up_list.append(chars)
        elif chars.islower() == True:
            low_list.append(chars)
        else:
            pass
        counter += 1
    return f'No. of Upper case characters : {len(up_list)} No. of Lower case characters : {len(low_list)}'

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)

# Alternative methods:

def up_low(s):
    d={"upper":0, "lower":0}
    for c in s:
        if c.isupper():
            d["upper"]+=1
        elif c.islower():
            d["lower"]+=1
        else:
            pass
    print("Original String : ", s)
    print("No. of Upper case characters : ", d["upper"])
    print("No. of Lower case Characters : ", d["lower"])
s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)

def up_low(s):
    uppercase = 0
    lowercase = 0
    for chars in s:
        if chars.isupper():
            uppercase += 1
        elif chars.islower():
            lowercase += 1
        else:
            pass
    print(f'No. of Upper case characters : {uppercase}') 
    print(f'No. of Lower case characters : {lowercase}')

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)

'''Write a Python function that takes a list and returns a new list with unique elements of the first list.

Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]
'''

def unique_list(lst):
    # Also possible to use list(set())
    x = []
    for a in lst:
        if a not in x:
            x.append(a)
    return x
unique_list([1,1,1,1,2,2,3,3,3,3,4,5])

# Alternate method:
def unique_list(lst):
    return list(set(lst))
unique_list([1,1,1,1,2,2,3,3,3,3,4,5])

'''Write a Python function to multiply all the numbers in a list.

Sample List : [1, 2, 3, -4]
Expected Output : -24'''

def multiply(numbers):
    product=1
    for num in numbers:
        product = product*num
    return product
multiply([2,2,3,-4])

'''Write a Python function that checks whether a word or phrase is palindrome or not.

Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam,kayak,racecar, or a phrase "nurses run". 
Hint: You may want to check out the .replace() method in a string to help out with dealing with spaces. 
Also google search how to reverse a string in Python, there are some clever ways to do it with slicing notation.

'''

def palindrome(s):
    s = s.replace(' ','')
    if s[0::] == s[::-1]:
        return True
    else:
        return False
palindrome('nurses run nurses run')

'''Hard:
Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)

Note : Panagrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"

Hint: You may want to use .replace() method to get rid of spaces.

Hint: Look at the string module

Hint: In case you want to use set comparisons'''

'Code mofification needed'
import string

def is_panagram(str1, alphabet=string.ascii_lowercase):
    str1 = str1.replace(' ','')
    if str1.lower() in alphabet:
        return 'Panagram'
    else:
        return 'Not Panagram'
s= "The quick brown fox jumps over the lazy dog"
is_panagram(s)

#Alternate methods:

import string
def ispangram(str1, alphabet=string.ascii_lowercase):
    for letter in alphabet:
        if letter in str1.replace(' ','').lower():
            continue
        else:
            return False
    return True
s= "The quick brown fox jumps over the lazy dog"
ispangram(s,string.ascii_lowercase)

'''You don't need to use the replace method -- you're only checking the letters in the alphabet, so any spaces, or punctuation in str1 won't matter.

One way to simplify it a bit, would be to use not in the if statement, so you wouldn't need to use continue or have an else clause.
'''

import string
 
def ispangram(str1, alphabet=string.ascii_lowercase):
    for letter in alphabet:
        if not letter in str1.lower():
            return False
    return True
s= "The quick brown fox jumps over the lazy dog"
ispangram(s,string.ascii_lowercase)

import string

def ispangram(str1, alphabet=string.ascii_lowercase): 
    # Create a set of the alphabet
    alphaset = set(alphabet)  
    
    # Remove spaces from str1
    str1 = str1.replace(" ",'')
    
    # Lowercase all strings in the passed in string
    # Recall we assume no punctuation 
    str1 = str1.lower()
    
    # Grab all unique letters in the string as a set
    str1 = set(str1)
    
    # Now check that the alpahbet set is same as string set
    return str1 == alphaset
ispangram("The quick brown fox jumps over the lazy dog")
