"""An exercise in remainders and boolean logic."""

__author__ = 730323932

num: int= int(input("Choose an integer"))

two: bool = (num % 2 == 0)
seven: bool = (num % 7 == 0)
both: bool = (num % 2 == 0 and num % 7 == 0)

if both == True:
    print("TAR HEELS")
else:
    if two == True:
        print("TAR")
    else:
        if seven == True: 
            print("HEELS")
        else:
            print("CAROLINA")