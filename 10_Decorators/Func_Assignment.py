
def func():
    return 1

print(func())

print(func)

def hello():
    return "Hello"

greet = hello

print(greet())

del hello

try:
    hello()
except:
    print("Exception occurred")

print(greet())
