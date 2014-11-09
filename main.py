import math
import random


def substraction():
    x = random.randrange(0,9)
    y = random.randrange(x,10)
    try:
        result = int(raw_input("What is the result of %d - %d :" %(y,x)))
    except:
        ValueError
        print 'Please enter number only'
    if result == (y-x):
        print 'Correct'
        score = 1
    else:
        print 'Incorrect'
        score = 0
    return score


def addition ():
    x = random.randrange(0,50)
    y = random.randrange(0,50)
    try:
        result = int(raw_input("What is the result of %d + %d :" %(x,y)))
    except:
        ValueError
        print 'Please enter number only'
    if result == (x+y):
        print 'Correct'
        score = 1
    else:
        print 'Incorrect'
        score = 0
    return  score


def multiplication ():
    x = random.randrange(0,9)
    y = random.randrange(0,10)
    try:
        result = int(raw_input("What is the result of %d * %d :" %(x,y)))

    except:
        ValueError
        print 'Please enter number only'
    if result == (x*y):
            print 'Correct'
            score = 1
    else:
            print 'Incorrect'
            score = 0
    return  score


def division():
    x = 2
    y = 3

    while x%y != 0:
        x = random.randrange(0,20)
        y = random.randrange(1,20)

    try:
        result = int(raw_input("What is the result of %d / %d :" %(x,y)))

    except:
        ValueError
        print 'Please enter number only'
    if result == (x/y):
        print 'Correct'
        score = 1
    else :
        print 'Incorrect'
        score = 0
    return  score


x = 0

score =[]

while x < 6:
    d = random.randrange(1,5)
    if d == 1:
        score.append(substraction())
    if d == 2 :
        score.append(addition())
    if d == 3 :
        score.append(multiplication())
    if d == 4 :
        score.append(division())
    x += 1

print ' Your score is %d'%(score[0]+score[1]+score[2]+score[3]+score[4]+score[5])