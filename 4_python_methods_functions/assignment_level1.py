
def old_macdonald(word):
    ##
    # OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
    ##
    if len(word) > 3:
        return word[:3].capitalize() + word[3:].capitalize()
    else:
        return "Word is too short"


def master_yoda(sentence):
    ##
    # MASTER YODA: Given a sentence, return a sentence with the words reversed
    ##
    wordList = sentence.split()
    return ' '.join(wordList[::-1])


def almost_there(num):
    ##
    # ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
    ##
    return abs(num-100) <= 10 or abs(num-200) <= 10


# print(old_macdonald('macdonald'))

# print(master_yoda('I am home'))
# print(master_yoda('We are ready'))

print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))