##
#   Object Oriented Programming allows programmers to create their own objects that have methods and attributes.
#   For example : upper() method of string class or index method of tuple object.
#
#   These methods acts as functions that use information about the object, as well as the object itself to return results, or change the current object.
#
#   OOP allows users to create their own objects.
#   In general, OOP allows us to create code that is repeatable and organized.
#
#
#   Syntax:
#       class NameOfClass():
#           
#           def __init__(self, param1, param2):
#               self.param1 = param1
#               self.param2 = param2
#    
#           def some_method(self):
#               # Some actions to be performed
#               print(self.param1)
##

# class keyword is used to define a class like other languages. class keyword followed by name of the class and paranthesis.
# class names 
class SampleClass():

    # This looks like a function. But it is called a method when it is inside of class.
    # This is a special method. This allows us to create an instance of the actual object.
    # param1 and param2 are the parameters Python expects you to pass when we are creating an instance of the object.
    # when we are assigning "self.param2 = param2", we are setting param2 attribute of the class with input param2.
    # we use self. to map it to the attribute of class.
    # This can be thought of as a constructor of a class.
    # This is automatically called when we create an instance of the class.

    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    # self keyword lets python know that it is not just some function but method of the class.
    def some_method(self):
        # Some actions to be performed
        print(self.param1)


# We all know that class is a blueprint that defines nature of a future object.
# From classes, we can define an instance of the object.

class Sample():
    pass

my_sample = Sample()
print(type(my_sample))