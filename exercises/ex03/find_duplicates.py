"""Finding duplicate letters in a word."""

__author__ = 730323932

#from typing import Counter

word: str= input("Enter a word: ")
num: int= 0
i: int = 0

while i < len(word):
    hold: str = word[i] 
    j: int = i + 1
    while j < len(word):
        if word[j] == hold:
            num = num + 1
        else:
            num = num + 0
            j = j + 1
    i = i + 1
if num > 0:
    print("Found duplicate: True")
else:
    print("Found Duplicate: False")

