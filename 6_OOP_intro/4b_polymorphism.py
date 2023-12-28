##
# Polymorphism - This refers to the way in which different object classes can share the same method name, and then those methods can be called from the same place, even though a variety of different objects might be passed in the best way.
# Benefits - 
##


#####################################################################
#################               Dog                 #################
#####################################################################
        

class Dog():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says woof!"


#####################################################################
#################               Cat                 #################
#####################################################################
        

class Cat():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says meow!"


#####################################################################
#################           Main method             #################
#####################################################################
        

def pet_speak(pet):
    print(pet.speak())



if __name__ == "__main__":
    niko = Dog("niko")
    felix = Cat("felix")
    print(niko.speak())
    print(felix.speak())

    for pet in [niko, felix]:
        print(pet.speak())

pet_speak(niko)
pet_speak(felix)


