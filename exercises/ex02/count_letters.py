"""Counting letters in a string."""

__author__ = 730323932

letter = input("What letter do you want to search for?:")
word = input("Enter a word:")

i = 0
a = (len(word))
num: int = 0

while i <= (a-1):
    if word[i] == letter:
        num = num + 1
    i = i + 1 

print(("Count:"), (num))