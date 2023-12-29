def problem1():

    ##
    # Handle the exception thrown by the code below by using try and except blocks.
    #
    #   for i in ['a','b','c']:
    #       print(i**2)
    ##

    try:
        for i in ['a','b','c']:
            print(i**2)
    except TypeError as te:
        print(te)
    except:
        print("Generic error")
    

def problem2():
    
    ##
    # Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done.'
    #
    #   x = 5
    #   y = 0
    #
    #   z = x/y
    ##
    
    try:
        x = 5
        y = 0

        z = x/y
    except ZeroDivisionError as zde:
        print(zde)
    except:
        print("Generic error")
    finally:
        print("All Done.")


def ask():
    
    ##
    # Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs.
    ##
    while True:
        try:
            int_val = int(input("Input an integer: "))
        except:
            print("An error occurred! Please try again!")
            continue
        else:
            print("Thank you, your number squared is:  {}".format(int_val**2))
            break


if __name__ == "__main__":
    # problem1()
    # problem2()
    ask()
    
