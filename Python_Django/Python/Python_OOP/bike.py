class Bike(object):
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
        print [self.price, self.max_speed, self.miles]
        return self

    def ride(self):
        print "Riding"
        self.miles = self.miles + 10
        return self

    def reverse(self):
        print "Reversing"
#First Instance
bike1 = Bike(300, 45, 10)
# bike1.ride()
# bike1.ride()
# bike1.ride()
# bike1.reverse()
# bike1.displayInfo()
#result= [300, 45, 30]
bike1.ride().ride().ride().ride().displayInfo();
