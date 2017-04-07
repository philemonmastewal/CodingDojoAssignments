def odd_even(a,b):
    for count in range (a,b):
        if count % 2 != 0:
            print "The number is",count,"This is an odd number."
        else:
            print "This number is",count,"This is an even number."

odd_even(1,200)
