##
# Special methods - these allow us to use some built in operations in Python, such as length function or the print function with our own user created object
# These are also called as Magic methods or Dunder methods.
##

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'{self.title} by {self.author}'
    
    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book object is deleted")

if __name__ == "__main__":
    b = Book("A thiller", "Sandy", 200)
    print(b)
    ## What happens when we call print() method. It calls string representation of that object. To check previous statement, let us find out below:
    print(str(b))
    
    # print()
    # try:
    #     len(b)
    # except TypeError as ex:
    #     print(ex)

    print(len(b))

    del b
    try:
        print(b)
    except NameError as ne:
        print(ne)