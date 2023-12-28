
def has_33(int_list):
    ##
    # FIND 33:
    # Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
    ##
    for index in range(0,len(int_list)-1):
        if int_list[index:index+2] == [3,3]:
        # or
        # if int_list[index] == 3 and int_list[index+1] == 3:
            return True
    return False
    

def paper_doll(text):
    ##
    # PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
    ##
    return ''.join([letter*3 for letter in text])


def blackjack(a,b,c):
    ##
    # BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
    ##
    if (a != 11 and b != 11 and c != 11):
        if sum((a,b,c)) > 21:
            return "BUST"
        else:
            return sum((a,b,c))
    else:
        return sum((a,b,c))-10


def summer_69(arr):
#     ##
#     # SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
#     ##
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


def spy_game(nums):
    ##
    # SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
    ##
    my_list = [0,0,7,'x']
    for num in nums:
        if num == my_list[0]:
            my_list.pop(0)
            # nums.remove(num)
    return len(my_list) == 1


def is_prime(num):
    count = 0
    for n in range(1, num):
        if num%n == 0:
            count += 2
    if count == 2:
        return True
    else:
        return False

def find_prime(num):
    primes = [n for n in range(1,num) if is_prime(n)];
    return len(primes)


# print(has_33([1, 3, 3]))
# print(has_33([1, 3, 1, 3]))
# print(has_33([3, 1, 3]))

# print(paper_doll('Hello'))
# print(paper_doll('Mississippi'))

# print(blackjack(5,6,7))
# print(blackjack(9,9,9))
# print(blackjack(9,9,11))

# print(summer_69([1, 3, 5]))
# print(summer_69([4, 5, 6, 7, 8, 9]))
# print(summer_69([2, 1, 6, 9, 11]))
# print(summer_69([4, 5, 9, 6, 7, 8, 9]))

# print(spy_game([1,2,4,0,0,7,5]))
# print(spy_game([1,0,2,4,0,5,7]))
# print(spy_game([1,7,2,0,4,5,0]))
    
print(find_prime(100))