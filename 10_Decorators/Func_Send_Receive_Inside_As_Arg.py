def hello():
    return 'Sandy'

def other_function(other_fp):
    print("Other code runs here")
    print(other_fp())

other_function(hello)