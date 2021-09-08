"""Repeating a beat in a loop."""

__author__ = 730323932


beat = input("Make a beat! Type a phrase that will be repeated.")
num = int(input("How many times do you want this repeated?"))
i = 1
s = ""

if num <= 0:
    print("No beat...")

while i <= num:
    if i > 0:
        s = s + " " + beat
    i = i + 1

print(s)