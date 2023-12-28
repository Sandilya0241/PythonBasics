class Dog():

    # Attributes
    # We take arguments and assign it to object attributes using self.attribute_name
    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        self.spots = spots


if __name__ == "__main__":
    try:
        my_dog = Dog()
    except TypeError as te:
        print(te)

    my_dog = Dog("Labrador", "Snoopy", spots=False)
    print(f'I have a dog named {my_dog.name} and it is of breed {my_dog.breed}.')
    if my_dog.spots:
        print("It has spots.")
    else:
        print("It doesn't have any spots.")

    print(type(my_dog.breed))