# If try didn't go well, except block will be executed. But if we want some logic to execute irrespective of try block execution, we use finally

import os

fp = None
try:
    fp = open(os.getcwd()+"\\..\\resources\\test.txt",'w')
    fp.write("Writing a test line")
except TypeError as te:
    print(te)
except IOError as ioe:
    print(ioe)
except:
    print("All other exceptions")
finally:
    print("I always run")
    fp.close()