##
# *args -> Arguments -> Gives arguments in tuple form
# **kwargs -> Keyword Arguments -> Gives arguments in dictionary format
# For below function a,b are called Positional arguments
#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
# def my_func(a,b):
#   # This function returns 5% of sum of a and b
#   return sum((a,b)) * 0.05
# my_func(40, 60)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
# In above function call, 40 is a and 60 is b based on their position in the function definition.
# If we want to pass more parameters, then function definition would be like: 
#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
# def my_func(a,b,c=0,d=0,e=0):
#   # This function returns 5% of sum of a and b
#   return sum((a,b,c,d,e)) * 0.05
# my_func(40, 60, 100, 100)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 
# We get answer for above function call as 15.0. But what if we call my_func like shown below:
#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
# my_func(40, 60, 100, 100, 100, 100)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 
# We might encounter TypeError: my_func() takes 2 to 5 positional arguments but 6 were given. Which means above approach has a limitation. Let us explore *args implementation
#
##


####################################################################################################################################################################
# *args can be *params/*spiderman. As a convention, we use args to indicate these are arguments.
####################################################################################################################################################################

def my_func(*args):
    print(f"Arguments received are {args}")
    return sum(args) * 0.05

def my_func2(*args):
    for value in args:
        print(value)

def understand_args():
    print(f"5% on sum for parameters (40, 60) is {my_func(40, 60)}")
    print()
    print(f"5% on sum for parameters (40, 60, 100) is {my_func(40, 60, 100)}")
    print()
    print(f"5% on sum for parameters (40, 60, 100, 1) is {my_func(40, 60, 100, 1)}")
    print()
    print(f"5% on sum for parameters (40, 60, 100, 1, 34) is {my_func(40, 60, 100, 1, 34)}")
    print()
    my_func2(40, 60, 100, 1, 34)

####################################################################################################################################################################
# *kwargs
####################################################################################################################################################################

def my_func3(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('The fruit selected is {}'.format(kwargs['fruit']))
    else:
        print('Oops! could not find the fruit')

def understand_kwargs():
    my_func3(fruit='Apple', Veggies='Lettuce')

def understand_args_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)
    print("I would like {} {}".format(args[0], kwargs['Food']))

def assignment(inputStr):
    output = []
    for index in range(len(inputStr)):
        if index%2 == 0:
            output.append(inputStr[index].lower())
        else:
            output.append(inputStr[index].upper())
    return ''.join(output)

#####################################################################################################################################################################
# Args and Kwargs
#####################################################################################################################################################################
if __name__ == "__main__":
    # understand_args()
    # understand_kwargs()
    # understand_args_kwargs(10, 20, 30,Fruit='Orange', Food='eggs', Animal='Dog')
    print("""Define a function called myfunc that takes in a string, and returns a matching string where every even letter is uppercase, and every odd letter is lowercase. Assume that the incoming string only contains letters, and don't worry about numbers, spaces or punctuation. The output string can start with either an uppercase or lowercase letter, so long as letters alternate throughout the string.""")
    print(assignment("Anthropomorphism"))