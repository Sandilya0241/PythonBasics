
'''PROBLEM1'''

def problem1():
    '''
    Create a generator that generates the squares of numbers up to some number N.
    '''
    for number in solution1(10):
        print(number)

def solution1(number_limit):
    for number in range(number_limit):
        yield number**2

'''PROBLEM2'''
from random import randint
def problem2():
    '''
    Create a generator that yields "n" random numbers between a low and high number (that are inputs).
    Note: Use the random library. For example:
    '''
    for number in solution2(1,10,12):
        print(number)

def solution2(low, high, number_limit):
    for _ in range(number_limit):
        yield randint(low, high)



# Can you explain what gencomp is in the code below? (Note: We never covered this in lecture! You will have to do some Googling/Stack Overflowing!)
# generator comprehension
my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)


if __name__ == "__main__":
    # problem1()
    problem2()

