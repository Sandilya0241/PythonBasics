##
# Abstract class is one that never expects to be instantiated, yet never actually expect to create an instance of this class.
# Instead, it's just designed to basically only serve as a base class.
##


#####################################################################
#################            Animal                 #################
#####################################################################
class Animal():

    def __init__(self, name):
        self.name = name

    # Abstracting a method
    def speak(self):
        raise NotImplementedError("Sub class must implement this abstract method")
    

class Dog(Animal):
    def speak(self):
        return self.name + " says woof!"


class Cat(Animal):
    def speak(self):
        return self.name + " says Meow!"


if __name__ == "__main__":
    fido = Dog("Fido")
    icici = Cat("icici")