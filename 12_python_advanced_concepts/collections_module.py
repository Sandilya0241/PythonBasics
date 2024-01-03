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