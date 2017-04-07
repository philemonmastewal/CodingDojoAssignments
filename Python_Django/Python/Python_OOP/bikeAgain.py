class Bike(object):
    def __init__(self,price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
        print self.price
        print self.max_speed
        print self.miles
        return self
    def ride(self):
        print "Riding"
        self.miles = self.miles + 10
        return self
    def reverse(self):
        print "Reversing"
        if self.miles <= 0:      #<-----prevents negative miles
            pass
        else:
            self.miles = self.miles - 5
        return self
bike1 = Bike(5000, 45)
bike2 = Bike(1200, 35)
bike3 = Bike(2500, 40)

bike1.ride().ride().ride().reverse().displayInfo()
bike2.ride().ride().reverse().reverse().displayInfo()
bike3.reverse().reverse().reverse().displayInfo()
