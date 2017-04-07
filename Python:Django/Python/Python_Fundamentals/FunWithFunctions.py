# Odd/Even: This function counts from 1 to 2000& as the loop executes, prints the number of that iteration and specifies whether it's an odd or even number.

def odd_even(a,b):
    for count in range(a,b):
        if count % 2 != 0:
            print "Number is",count,"This is an odd number."
        else:
            print "Number is",count,"This is an even number."
odd_even(1,2000)

#Multiply: iterates through each value in a list and returns a list where each value has been multiplied by 5
def multiply(a,x):

    count= 0
    while count < len(a):
        a[count] = a[count]*x
        count += 1
    print a
multiply([1,2,3,4],5)

#Hacker Challenge: this function takes the multiply function call as an arguement. The new function should return the multiplied list as a two-dimensional list. Each internal list should contain the number of 1's as the number in thee original list.
