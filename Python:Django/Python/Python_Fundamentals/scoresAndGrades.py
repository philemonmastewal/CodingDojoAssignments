#This function should generate 10 scores between 60 and 100, & each time a score is generated it should display the grade for a particular score.

import random
def scoreGenerate():
    count= 0
    arr = ['D','C','B','A']
    grade= 0
    # for count in range(1,10):
    while count <10:
        random_num= random.random()
        str= random.randint(60,100)
        if str >89:
            grade = arr[3]
        elif str >79:
            grade = arr[2]
        elif str >69:
            grade = arr[1]
        elif str >59:
            grade = arr[0]
        count += 1
        print "Score:",str,"Your grade is",grade

scoreGenerate()
