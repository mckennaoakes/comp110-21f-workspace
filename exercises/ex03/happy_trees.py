"""Drawing forests in a loop."""

__author__ = 730323932

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

deep: int = int( input( "Depth:"))
i: int = 0
s = ""

while i < deep:
     s = s + TREE
     print(s)
     i = i + 1
