# prints all odd numbers between 1 and 1,000
for count in range(0,1000):
    if count % 2 != 0:
        print count

# prints all the multiples of 5 from 5 to 1,000,000
for count in range(5,1000000,5):
    print count

# prints the sum of all the values in the list a= [1,2,5,10,255,3]
a= [1,2,5,10,255,3]
i=0
sum=0
while i < len(a):
    sum = sum + a[i]
    i += 1
print sum

#prints the average--same as the one above, except at the end you divide the length from the sum
a= [1,2,5,10,255,3]
i=0
sum=0
while i < len(a):
    sum = sum + a[i]
    i += 1
print sum/len(a)
