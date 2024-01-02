def create_cubes(num_limit):
    result = []
    for num in range(num_limit):
        result.append(num**3)
    return result

# print(create_cubes(10))

# for num in create_cubes(10):
#     print (num)
print(create_cubes(10))

def create_cubes_new(num_limit):
    for num in range(num_limit):
        yield num ** 3

print(create_cubes_new(10))

def fibonacci_cust(num_limit):
    a=1
    b=1
    for num in range(num_limit):
        yield a
        a,b = b,a+b
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=
for num in fibonacci_cust(10):
    print(num)

def simple_gen():
    for number in range(3):
        yield number

for number in simple_gen():
    print(number)

g = simple_gen()

print(next(g))
print(next(g))
print(next(g))
try:
    print(next(g))
except StopIteration as sie:
    print(sie)

s = "Hello"
# next(s)

s_iter = iter(s)
print(next(s_iter))