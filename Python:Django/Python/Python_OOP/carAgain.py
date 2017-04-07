class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage

        if self.price < 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12

    def displayInfo(self):
        print "Price:", self.price
        print "Speed:" , self.speed , "mph"
        print "Fuel:"  , self.fuel
        print "Mileage:" , self.mileage , "mpg"
        print "Tax:", self.tax
car1 = Car(15000, 75, "Full", 33 )
car2 = Car(12000, 50, "Almost full", 33 )
car3 = Car(16000, 95, "Almost empty", 33 )
car4 = Car(19000, 120, "Empty", 33 )
car5 = Car(11000, 45, "Full", 33 )
car6 = Car(13000, 65, "Empty", 33 )

car1.displayInfo()
car2.displayInfo()
car3.displayInfo()
car4.displayInfo()
car5.displayInfo()
car6.displayInfo()
