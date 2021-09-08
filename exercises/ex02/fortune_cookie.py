"""Program that outputs one of at least four random, good fortunes."""

__author__ = 730323932

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint

cookie1= "Your dream lover will walk into your life today."
cookie2= "You will ace all of the tests you take today."
cookie3= "Look out for new opportunities coming your way in the next week."
cookie4= "You will achieve all of your life goals if you keep working towards them."

fortune= (randint(1, 4))
print("Your fortune cookie says...")
if fortune == 1:
    print(cookie1)
else:
    if fortune == 2:
        print(cookie2)
    else: 
        if fortune == 3:
            print(cookie3)
        else:
            if fortune == 4:
                print(cookie4)
print("Now, go spread positive vibes!")