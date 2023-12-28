##
# Let us understand, how python deals with variable names. When we create a name in python, that name is stored in what's called the namespace.
# Variable names also have a scope. And scope determines the vibility.
#
# LEGB rule format is followed.
# (L)ocal                    ->>> Names assigned in any way within a function (def or lambda), and not declared global in that function.
# (E)nclosed function locals ->>> Names in the local scope of any and all enclosing functions (def or lambda), from inner to outer.
# (G)lobal                   ->>> Names assigned at the top-level of a module file, or declared global in a def within the file.
# (B)uilt-in (Python)        ->>> Names preassigned in the built-in names module: open, range, SyntaxError ...
##

# xVar = 25

# def printer():
#     xVar = 50
#     return xVar

# print(xVar)

# print(printer())

##########################################################################
################################  locals  ################################
##########################################################################
print()
print("num is a local variable inside below lambda function\nlambda num : num**2")
print()

##########################################################################
################ Enclosed function locals ################################
##########################################################################

# Global Variable
name = 'This is a global string'
def greet():
    # Enclosed Local Variable
    name = 'Sammy'
    def hello():
        #Local Variable
        name = 'Sandy'
        print("Hello " + name)
    hello()
greet()
print()
print("First it checks for a variable with name 'name' inside hello() function.\nAs there isn't any such variables, it checks at next level which is enclosed function locals.\nNow it found name='Sammy'. So, it picks up the variable and executes.\nIf we comment, name variable inside greet() function, it goes to next level global and check for variable named 'name'")
print()


##########################################################################
################ locals variable and global variables ####################
##########################################################################

x = 50
def func(x):
    print(f'x value is {x}')
    # LOCAL REASSIGNMENT
    x = 200
    print(f'Just reassigned x to {x}')

func(x)
print(x)

def func_global():
    global x
    print(f'x value is {x}')
    # LOCAL REASSIGNMENT ON A GLOBAL VARIABLE
    x = 500
    print(f'Just reassigned global x to {x}')


func_global()
print(x)