from math import pi, floor,ceil,nan,e,inf,log,sin,degrees,radians

from random import randint,seed,choice,choices,sample,gauss,uniform

#####################################
# Math module
#####################################

def math_module():
    value = 4.35

    # floor() will round off number which is <= decimal
    print(floor(value))

    # ceil() will round off to next integer
    print(ceil(value))

    # round().
    print(f'round({value}) is {round(value)}')
    print(f'round(4.5) is {round(4.5)}')
    print(f'round(5.5) is {round(5.5)}')
    #The round() function rounding strategy and return type have changed. Exact halfway cases are now rounded to the nearest even result instead of away from zero. (For example, round(2.5) now returns 2 rather than 3.) round(x[, n]) now delegates to x.round([n]) instead of always returning a float. It generally returns an integer when called with a single argument and a value of the same type as x when called with two arguments.

    print(f'Mathematical constants - pi - {pi}')
    print(f'Mathematical constants - nan - {nan}')
    print(f'Mathematical constants - e - {e}')
    print(f'Mathematical constants - inf - {inf}')
    print(f'Mathematical log - loge - {log(e)}')
    print(f'Mathematical log - log(100,10) - {log(100,10)}')
    print(f'Mathematical sin(10) - {sin(10)}')
    print(f'Mathematical degrees - {degrees(pi/2)}')
    print(f'Mathematical radians - {radians(180)}')


# math_module()

#####################################
# Random module
#####################################

def seed_random_nums():
    print("================================")
    seed(101)
    print(randint(100000,999999))
    print(randint(100000,999999))
    print(randint(100000,999999))
    print("================================")

def random_module():
    print(randint(100000,999999))
    # To test functionality but with same set of random numbers, we use seeding.
    seed_random_nums()
    seed_random_nums()
    seed_random_nums()
    print(randint(100000,999999))
    print("VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV")
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    my_list = list(range(0,20))
    print(choice(my_list))
    # pick 5 random numbers from my_list
    # There are 2 different ways:
    # 1. SAMPLE WITH REPLACEMENT
    # 2. SAMPLE WITHOUT REPLACEMENT
    print(choices(population=my_list,k=10))
    print(sample(population=my_list,k=10))
    print(uniform(a=0,b=100))
    print(gauss(mu=0,sigma=1))

random_module()