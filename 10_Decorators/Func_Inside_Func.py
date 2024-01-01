import sys

def hello():
    print("This hello() function has been executed.")

    def greet():
        return "\t This is greet() function inside hello function."

    def welcome():
        return "\t This is welcome() function inside hello function."

    print("I'm going to return a function()!!!")

    # print(sys.argv[1])
    if len(sys.argv) > 1 and  sys.argv[1] == 'Sandy':
        return greet
    else:
        return welcome

func = hello()
print(func())

# welcome()

####################################
print("++++++++++++++++++++++++++++++++++++++++++++++++++++=")


def cool():

    def super_cool():
        print("I'm very cool")

    return super_cool

some_fun_def = cool()

print(some_fun_def)

some_fun_def()