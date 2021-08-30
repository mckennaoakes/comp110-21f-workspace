"""Numeric Operators"""

__author__= "730323932"

left_hand_side: int = int(input("choose a number 1-10"))
right_hand_side: int = int(input("choose another number 1-10"))

print("Left-hand side: " + str(left_hand_side)) 
print("Right-hand side: " + str(right_hand_side))
exponent: int = int((left_hand_side) ** (right_hand_side))
divide: float= int(left_hand_side) / (right_hand_side)
intdiv: int = int(left_hand_side) // (right_hand_side)
remainder: int = int(left_hand_side) % (right_hand_side)

print((str(left_hand_side)), ("**"), (str(right_hand_side)), ("is"), (str(exponent)))
print((int(left_hand_side)), ("/"), (int(right_hand_side)), ("is"), (float(divide)))
print((str(left_hand_side)), ("//"), (str(right_hand_side)), ("is"), (str(intdiv)))
print((str(left_hand_side)), ("%"), (str(right_hand_side)), ("is"), (str(remainder)))