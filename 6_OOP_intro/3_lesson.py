

#####################################################################
#################                DOG                #################
#####################################################################

class Dog():

    # CLASS OBJECT ATTRIBUTES
    # THESE ARE SAME FOR ANY INSTANCE
    species = "mammal"

    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        self.spots = spots

    ##
    # Methods are essentially functions defined inside body of a class, and they're used to perform operations that sometimes utilize the actual attributes of the object we created.
    ##
    def change_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

    def bark(self, number):
        print("WOOF! Hi my name is {} and number is {}".format(self.name, number))


def method_use_dog():
    my_dog1 = Dog(breed="Labrador", name="Snoopy", spots=False)
    my_dog2 = Dog(breed="Dalmatian", name="Lisa", spots=True)
    print(f'species of {my_dog1.name} is {my_dog1.species}')
    print()
    print(f'species of {my_dog2.name} is {my_dog2.species}')
    print()
    my_dog1.change_name("Dollor")
    print(f'Changed my dog name to {my_dog1.get_name()}')
    print()
    my_dog1.bark(10)
    print()
    my_dog2.bark(25)


#####################################################################
#################                DOG                #################
#####################################################################
        
class Circle():
    #Class Object Attribute
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        ## We can use self.pi or Circle.pi
        self.area = self.pi * (radius**2)
        # self.area = Circle.pi * (radius**2)

    def get_circumference(self):
        return (2 * self.pi * self.radius)

    def change_radius(self, new_radius):
        self.radius = new_radius

def method_use_circle():
    my_circle = Circle()
    print(my_circle.get_circumference())
    my_circle.change_radius(5)
    print('Circumference after changing radius to {} is {}'.format(my_circle.radius, round(my_circle.get_circumference(),2)))
    print('Area is {}'.format(my_circle.area))


#####################################################################
#################          MAIN METHOD              #################
#####################################################################


if __name__ == "__main__":
    # method_use_dog()
    method_use_circle()