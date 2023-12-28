#################################################################################################################################
##
# Lambda Expressions : This is a way to quickly create what are known as anynomous functions, basically just one time use functions that you don't even really name. You just use them and never reference them again.
# Map : It applies a function for every element in the list.
# Filter : To filter out elements that meet function's condition from a list
##
#################################################################################################################################

##
# map function example1
##

def square(num):
    return num**2

def map_functionality_1():
    my_nums = [1,2,3,4,5]

    for item in map(square,my_nums):
        print(item)
    
    print(list(map(square,my_nums)))


##
# map function example2
##
    

def splicer(my_string):
    if len(my_string)%2 == 0:
        return "EVEN"
    else:
        return my_string[0]
    

def map_functionality_2():
    names = ['Andy', 'Eve', 'Sally']
    print(list(map(splicer,names)))


##
# filter function example1
##
def check_even(num):
    return num%2 == 0

def filter_functionality():
    my_nums = [1,2,3,4,5,6]
    print(list(filter(check_even, my_nums)))
    print()
    for num in filter(check_even, my_nums):
        print(num)
    


##
# Lamdba function example1
##
sqr_function = lambda num: num ** 2


def lamdba_functionality():
    ##
    # Inside map function, we were passing function as first parameter. When we are using it once, we don't need to declare a function. Instead we can use an anynomous function.
    ##
    # print(sqr_function(9))
    my_nums = [1,2,3,4,5]
    map_squares = map(lambda num : num**2, my_nums)
    for n in map_squares:
        print(n)


def lamdba_functionality_2():
    my_nums = [1,2,3,4,5,6]
    filter_evens = filter(lambda num : num%2==0, my_nums)
    for n in filter_evens:
        print(n)


def lamdba_functionality_3():
    names = ['Andy', 'Eve', 'Sally']
    map_first_char = map(lambda name : name[0], names)
    for n in map_first_char:
        print(n)


if __name__=="__main__":
    # map_functionality_1()
    # map_functionality_2()
    # filter_functionality()
    # lamdba_functionality()
    # lamdba_functionality_2()
    lamdba_functionality_3()