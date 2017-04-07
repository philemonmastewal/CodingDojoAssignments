#This function should simulate tossing a coin 5,000 times, and then print how many times head/tail appears.

import random

heads = 0
tails = 0
headsCount= 0
tailsCount= 0
side = ""
for count in range(1,5000):
    x = random.random()
    x_rounded = round(x)
    # print x_rounded --- this was to test if it was 1.0 or 0.0
    if x_rounded == 1.0:
        side = "Heads"
        count += 1
        headsCount += 1
    else:
        side = "Tails"
        count += 1
        tailsCount += 1
    print "Attempt #",count,": Throwing a coin...","It's a",side+"!... Got", headsCount,"head(s) so far and",tailsCount,"tail(s) so far"
