"""Relational Operators"""

__author__= "730323932"

left_hand_side: int = int(input("choose a number"))
right_hand_side: int = int(input("choose another number"))
x = int(left_hand_side)
y = int(right_hand_side)


print("Left-hand side: " + str(left_hand_side)) 
print("Right-hand side: " + str(right_hand_side))

boolless: bool = bool(left_hand_side < right_hand_side)
print(str(x) ,("<") , str(y), "is" , boolless)

boolgreat: bool = bool(left_hand_side >= right_hand_side)
print(str(x) ,(">=") , str(y), "is" , boolgreat)

booleq: bool = bool(left_hand_side == right_hand_side)
print(str(x) ,("==") , str(y), "is" , booleq)

boolnoteq: bool = bool(left_hand_side != right_hand_side)
print(str(x) ,("!=") , str(y), "is" , boolnoteq)