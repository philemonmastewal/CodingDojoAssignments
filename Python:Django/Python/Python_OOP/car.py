class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage

        if self.price > 10000:
            tax = .15
        else:
            tax = .12
        self.tax = tax

    def displayAll(self):
        print ["Price:" + str(self.price), "Speed:" + str(self.speed), "Fuel:" + str(self.fuel), "Mileage:" + str(self.mileage), "Tax:" + str(self.tax)]

car1 = Car(7000,120,15,28)
car2 = Car(4000,140,19,24)
car3 = Car(8000,110,20,28)
car4 = Car(12000,150,25,27)
car5 = Car(22000,180,21,22)
car6 = Car(16000,160,24,25)

car1.displayAll()
car2.displayAll()
car3.displayAll()
car4.displayAll()
car5.displayAll()
car6.displayAll()
