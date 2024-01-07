# - Collections:
# =============================================================================================

#     Counter
#     ==================

#     The Collections module is built in based Python and it implements specialized container data types that are essentially alternatives to Python's built-in containers that are just general purpose.

#     Built-in containers are something like Dictionary/ Tuples. But counter has specialized Dictionary objects or specialized Tuple objects.

#     We may not need these specialized versions always, but in certain use cases we may find them quite useful.

#     Common patterns when using the Counter() object
#     ================================================
#         sum(c.values())                 # total of all counts
#         c.clear()                       # reset all counts
#         list(c)                         # list unique elements
#         set(c)                          # convert to a set
#         dict(c)                         # convert to a regular dictionary
#         c.items()                       # convert to a list of (elem, cnt) pairs
#         Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
#         c.most_common()[:-n-1:-1]       # n least common elements
#         c += Counter()                  # remove zero and negative counts

#     defaultdict
#     ==================
#     defaultdict is a dictionary-like object which provides all methods provided by a dictionary but takes a first argument (default_factory) as a default data type for the dictionary. Using defaultdict is faster than doing the same using dict.set_default method.

#     A defaultdict will never raise a KeyError. Any key that does not exist gets the value returned by the default factory.

#     namedtuple
#     ==================
#     The standard tuple uses numerical indexes to access its members, for example:

#     t = (12,13,14)
#     t[0]
#     12
#     For simple use cases, this is usually enough. On the other hand, remembering which index should be used for each value can lead to errors, especially if the tuple has a lot of fields and is constructed far from where it is used. A namedtuple assigns names, as well as the numerical index, to each member.

#     Each kind of namedtuple is represented by its own class, created by using the namedtuple() factory function. The arguments are the name of the new class and a string containing the names of the elements.

#     You can basically think of namedtuples as a very quick way of creating a new object/class type with some attribute fields.


from collections import Counter
from collections import defaultdict
from collections import namedtuple

    
def CounterExample():
    my_list = [1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3]
    print(Counter(my_list))
    my_list = ['a','a','b',10,10]
    print(Counter(my_list))
    print(Counter('aabbbassahjsalksalsjdjdjdjl'))
    sentence = "How many times does each word show up in this sentence with a word"
    print(Counter(sentence.lower().split()))
    #Common patterns when using counter object.
    letter = "aaaaaabbbbbbbbbbcccccccdddddddddddd"
    c = Counter(letter)
    print(c.most_common())
    # First 2 most common
    print(c.most_common(2))
    # First 2 most common
    print(c.most_common(3))
    l = list(c)
    print(l)


def DefaultDictExample():
    '''
    To get rid of KeyError, we can assign a default value to unavailable keys.
    '''
    # d = {'a':10}
    # print(d['a'])
    # print(d['WRONG_KEY'])

    d = defaultdict(lambda: 0)
    d['correct_key'] = 100
    print(d['correct_key'])
    print(d['incorrect_key'])
    print(d)


def NamedTupleExample():
    '''
    To find out the location of an element in a large tuple is difficult. With namedtuple, we can easily access tulple elements
    '''
    my_tuple = (10,20,30)
    Dog = namedtuple('Dog',['age','breed','name'])
    sammy = Dog(age=5,breed='Husky',name='Sam')
    print(type(sammy))
    print(sammy.age)
    print(sammy[0])


# CounterExample()
# DefaultDictExample()
NamedTupleExample()