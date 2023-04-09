# Warmup:

'''LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
lesser_of_two_evens(2,4) --> 2
lesser_of_two_evens(2,5) --> 5'''

def lesser_of_two_evens(a,b):
    if a > b and (a%2 == 0 and b%2 == 0):
        return b
    elif a > b and (a%2 != 0 or b%2 != 0):
        return a
    elif b > a and (a%2 == 0 and b%2 == 0):
        return a
    elif b > a and (a%2 != 0 or b%2 != 0):
        return b
    else:
        pass
lesser_of_two_evens(4,16)

'''ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
animal_crackers('Levelheaded Llama') --> True
animal_crackers('Crazy Kangaroo') --> False'''

def animal_crackers(text):
    text = text.split()
    while (len(text)==2):
        if(text[0][0]==text[1][0]):
            return True
        else:
            return False
    pass
animal_crackers('Crazy Cat')

'''MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
makes_twenty(20,10) --> True
makes_twenty(12,8) --> True
makes_twenty(2,3) --> False'''

def makes_twenty(n1,n2):
    if (n1+n2)==20 or n1==20 or n2==20:
        return True
    else:
        return False
makes_twenty(0,20)

# LEVEL 1 PROBLEMS:

'''OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
old_macdonald('macdonald') --> MacDonald

Note: 'macdonald'.capitalize() returns 'Macdonald'''

def old_macdonald(name):
    mylist = []
    for letter in range(len(name)):
        if letter == 0 or letter == 3:
            mylist.append(name[letter].upper())
        else:
            mylist.append(name[letter])
    return ''.join(mylist)
old_macdonald('bigmac')

'''MASTER YODA: Given a sentence, return a sentence with the words reversed
master_yoda('I am home') --> 'home am I'
master_yoda('We are ready') --> 'ready are We'

Note: The .join() method may be useful here. The .join() method allows you to join together strings in a list with some connector string. For example, some uses of the .join() method:
This means if you had a list of words you wanted to turn back into a sentence, you could just join them with a single space string:

>>> " ".join(['Hello','world'])
>>> "Hello world"'''

def master_yoda(text):
    mylist = []
    text = text.split()
    for word in text[::-1]:
        mylist.append(word)
    return ' '.join(mylist)
master_yoda('I am home')

'''ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
almost_there(90) --> True
almost_there(104) --> True
almost_there(150) --> False
almost_there(209) --> True

NOTE: abs(num) returns the absolute value of a number
'''
def almost_there(n):
    if (0 <= abs(100-n) <= 10) or (0 <= abs(200-n) <= 10):
        return (True, "{} is within 10 of 100 or 200".format(n))
    else:
        return (False, "{} is not within 10 of 100 or 200".format(n))
almost_there(209)

# LEVEL 2 PROBLEMS:

'''FIND 33:
Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False'''

def has_33(nums):
    for i in range(0, len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True    
    return False
has_33([3,1,3])

'''PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
paper_doll('Hello') --> 'HHHeeellllllooo'
paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'''

def paper_doll(text):
    mylist = []
    for letter in range(len(text)):
        mylist.append(text[letter]*3)
    return ''.join(mylist)
paper_doll('Hello')

'''BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. 
Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
blackjack(5,6,7) --> 18
blackjack(9,9,9) --> 'BUST'
blackjack(9,9,11) --> 19'''

def blackjack(a,b,c):
    if sum((a,b,c)) <= 21:
        return sum((a,b,c))
    elif sum((a,b,c)) <=31 and 11 in (a,b,c):
        return sum((a,b,c)) - 10
    else:
        return 'BUST'
blackjack(9,29,11)

'''SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 
and extending to the next 9 (every 6 will be followed by at least one 9). 
Return 0 for no numbers.
summer_69([1, 3, 5]) --> 9
summer_69([4, 5, 6, 7, 8, 9]) --> 9
summer_69([2, 1, 6, 9, 11]) --> 14'''
    
def summer_69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total
summer_69([4,5,6,7,8,9])

# Challenging PROBLEMS:

'''SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
 spy_game([1,2,4,0,0,7,5]) --> True
 spy_game([1,0,2,4,0,5,7]) --> True
 spy_game([1,7,2,0,4,5,0]) --> False'''

def spy_game(nums):

    code = [0,0,7,'x']
    
    for num in nums:
        if num == code[0]:
            code.pop(0)   # code.remove(num) also works
       
    return len(code) == 1 # returns boolean value once check for 007 complete and code list of len 1 remains
    
spy_game([1,7,2,0,4,5,0])
    
'''COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to 
and including a given number. 

count_primes(100) --> 25 By convention, 0 and 1 are not prime.'''

def count_primes(num):
    # check for 0,1 input
    if num < 2:
        return 0
    # 2 or greater
    # list to store prime numbers starting from 2
    primes = [2]
    # initialize counter going up to the input num
    x = 3
    # x going thru every number upto input num
    while x <= num:
        # check if x is prime
        for y in range (3,x,2):
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)
count_primes(56)

'''
PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter
print_big('a')

out:   *  
      * *
     *****
     *   *
     *   *
HINT: Consider making a dictionary of possible patterns, and mapping the alphabet to specific 5-line combinations of patterns.
For purposes of this exercise, it's ok if your dictionary stops at "E".
'''

def print_big(letter):
    patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}
    alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])