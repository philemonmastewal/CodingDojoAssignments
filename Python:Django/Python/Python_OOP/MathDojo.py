class MathDojo(object):
    def __init__(self,result=0):
        self.result = result
    def add(self,*numbers):
        self.numbers = numbers
        print self.numbers
        total = 0
        for x in range(len(self.numbers)):
            total += x
        self.result = total
        return total
        return self
    def subtract(self,*numbers):
        self.numbers = numbers
        for x in range(0,len(numbers)):
            self.result -= x
        return self
    def result(self):
        print self.result
        print result
        return self
md = MathDojo()
print md.add(10,2,21,12)
