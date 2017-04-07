string = "If monkeys like bananas, then I must be a monkey!"
string.find("monkey")
string.replace("monkey","alligator")

x = [2,54,-2,7,12,98]
print min(x)
print max(x)

x= ["hello",2,54,-2,7,12,98,"world", "boo"]
print x[0], x[(len(x)-1)]

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x
firstHalf=x[0:(len(x)/2)]
secondHalf = x[(len(x)/2):len(x)]

secondHalf.insert(0,firstHalf)
print secondHalf
