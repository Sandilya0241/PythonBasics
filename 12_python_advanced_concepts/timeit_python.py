# To identify how long our logic ran to calculate performance, we have timeit module
from timeit import timeit

if __name__ == "__main__":
    stmt1 = '''
func_one(100)
'''
    
    setup1 = '''
def func_one(num_limit):
    return [str(num) for num in range(num_limit)]
'''
    
    print(timeit(stmt1, setup1, number=100000))

    stmt2 = '''
func_two(100)
'''
    
    setup2 = '''
def func_two(num_limit):
    return list(map(str,range(num_limit)))
'''
    
    print(timeit(stmt2, setup2, number=100000))