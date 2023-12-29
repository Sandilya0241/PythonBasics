## 
# try - This is the block of code to be attempted (may lead to error)
# 
# except - Block of code will execute in case there is an error in tryblock.
#
# finally - A finally block of code to be executed, irrespective of an error. 
## 

def add_numbers(num1, num2):
    print(num1+num2)

num1 = 10
num2 = input("please provide a number : ")
try:
    add_numbers(num1, int(num2))
except:
    print("It looks like there is some issue")
else:
    print("Add went well")

print("something happend")




