# wrapper function around original_function

def new_decorator(original_function):
    def wrap_func():
        print('Some extra code, before the original function.')
        original_function()
        print('Some extra code, after the original function.')

    return wrap_func

@new_decorator
def needs_decorator():
    print("I need to be decorated")

needs_decorator()
