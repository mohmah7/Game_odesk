import random


def substraction():
    x = random.randrange(0,9)
    y = random.randrange(x,10)
    try:
        result = int(raw_input("What is the result of %d - %d :" %(y,x)))

        if result == (y-x):
            print 'Correct Answer'
            score = 1
        else:
            print 'Incorrect Answer'
            score = 0
    except:
        ValueError
        print 'Incorrect Answer'
        print 'Please enter number only'
        score = 0


    return score

substraction()