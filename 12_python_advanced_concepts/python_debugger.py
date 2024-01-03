import pdb

def debugging_with_print():
    var1 = [1,2,3]
    var2 = 2
    var3 = 5
    print("Debugging point 1 reached...")
    result = var2 + var3
    print("Debugging point 2 reached...")
    result2 = var1 + var3
    print("Debugging point 3 reached...")

# debugging_with_print()

def debugging_with_debugger():
    var1 = [1,2,3]
    var2 = 2
    var3 = 5
    
    result = var2 + var3
    pdb.set_trace()
    result2 = var1 + var3

debugging_with_debugger()