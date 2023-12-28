
####################################################################################################################################
# warm_up_section
####################################################################################################################################

def lesser_of_two_evens(num1, num2):
    ##
    # LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
    ##
    if num1%2 == 0 and num2%2 == 0:
        return min(num1, num2)
    else:
        return max(num1, num2)

def animal_crackers(word):
    ##
    # ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
    ##
    wordList = word.split()
    return wordList[0][0] == wordList[1][0]

def makes_twenty(num1, num2):
    ##
    # MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
    ##
    return num1 == 20 or num2 == 20 or num1+num2==20

# print(lesser_of_two_evens(2,4))
# print(lesser_of_two_evens(2,5))

# print(animal_crackers('Levelheaded Llama'))
# print(animal_crackers('Crazy Kangaroo'))

print(makes_twenty(20,10))
print(makes_twenty(12,8))
print(makes_twenty(2,3))
print(makes_twenty(21,11))