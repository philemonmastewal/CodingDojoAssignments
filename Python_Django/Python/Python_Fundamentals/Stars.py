#Create a function that takes a list of numbers and prints out a number of stars corresponding to the number that element is

#Part 1
def draw_stars(arr):
  for x in arr:
    arr= "*"*x
    print arr
draw_stars([4,2,3])

#Part 2
from types import *
def draw_stars(arr):
  for item in arr:
    if type(item) is StringType:

        print item[0].lower() * len(item)
    else:
        type(item)
        arr= "*"*item
        print item
draw_stars([4,2,'Hello',3,'Tuna'])
