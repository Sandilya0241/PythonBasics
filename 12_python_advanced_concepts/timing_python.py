# To identify how long our logic ran to calculate performance, we have timeit module
import time

def func_one(num_limit):
    return [str(num) for num in range(num_limit)]

def func_two(num_limit):
    return list(map(str,range(num_limit)))

def test_perf_func_one():
    # CURRENT TIME
    start_time = time.time()

    result = func_one(100000)

    end_time = time.time()

    elapsed_time = end_time - start_time
    print(elapsed_time)


def test_perf_func_two():
    # CURRENT TIME
    start_time = time.time()

    result = func_two(100000)

    end_time = time.time()

    elapsed_time = end_time - start_time
    print(elapsed_time)

if __name__ == "__main__":
    test_perf_func_one()
    test_perf_func_two()