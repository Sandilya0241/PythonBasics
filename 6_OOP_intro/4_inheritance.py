##
# Inheritance - Is a way defining new classes using existing classes that are already been defined.
# Benefits - ability to reuse code that you have already worked on and reduce the complexity of the program.
##


#####################################################################
#################           Animal (Base)           #################
#####################################################################
        

class Animal():

    def __init__(self):
        print("Animal created")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("Animal is eating")


#####################################################################
#################           Dog (Derived)           #################
#####################################################################
        

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def who_am_i(self):
        # return super().who_am_i()
        print("I am a dog!")

    def bark(self):
        print("WOOF!!")

#####################################################################
#################           Main method             #################
#####################################################################
        


if __name__ == "__main__":
    # my_animal = Animal()
    # my_animal.eat()
    # my_animal.who_am_i()

    my_dog = Dog()
    ## Eventhough we don't have eat method defined inside Dog class, we could able to access it.
    my_dog.eat()
    my_dog.who_am_i()
    my_dog.bark()

