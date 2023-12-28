## *****1*****
# Complete the following questions: ____ Write a function that computes the volume of a sphere given its radius.
# The volume of a sphere is given as
# 4/3 (pi) (r)^3
##
from math import pi
import string

def vol(rad):
    return (4/3) * (pi) * (rad**3)



## *****2*****
# Write a function that checks whether a number is in a given range (inclusive of high and low)
##
def ran_check(num,low,high):
    if num in range(low,high+1):
        print(f'{num} is in range {low}, {high}')
    else:
        print(f'{num} is out of range')


## *****3*****
# If you only wanted to return a boolean:
##

def ran_bool(num,low,high):
    return num in range(low,high+1)


## *****4*****
# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
##

def up_low(s):
    upperCount = 0
    lowerCount = 0
    for letter in s:
        if letter.isupper():
            upperCount += 1
        if letter.islower():
            lowerCount += 1
    print(f'No. of Upper case characters : {upperCount}\nNo. of Lower case Characters : {lowerCount}')


## *****5*****
# Write a Python function that takes a list and returns a new list with unique elements of the first list.
##

def unique_list(lst):
    return list(set(lst))


## *****6*****
# Write a Python function to multiply all the numbers in a list.
##

def multiply(numbers):
    res = 1
    for num in numbers:
        res *= num
    print(f'Expected Output : {res}')



## *****7*****
# Write a Python function that checks whether a word or phrase is palindrome or not.
##

def palindrome(s):
    s = s.replace(" ", "")
    return s == s[::-1]


## *****8*****
# Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)
##

def ispangram(str1, alphabet=string.ascii_lowercase):
    # Create alphaset
    alphaset = set(alphabet)

    #replace empty spaces
    str1 = str1.replace(" ","")

    #Convert as set
    str1 = set(str1.lower())

    return str1 == alphaset


if __name__ == "__main__":
    ## *****1*****
    # print(vol(2))
    
    ## *****2*****
    # ran_check(15,2,7)
    
    ## *****3*****
    # print(ran_bool(3,1,10))
    
    ## *****4*****
    # up_low('Hello Mr. Rogers, how are you this fine Tuesday?')    
    
    ## *****5*****
    # sampLst = [1,1,1,1,2,2,3,3,3,3,4,5]
    # print(unique_list(sampLst))

    ## *****6*****
    # multiply([1, 2, 3, -4])

    ## *****7*****
    # print(palindrome('nurses run'))

    ## *****8*****
    print(ispangram("The quick brown fox jumps over the lazy dog"))