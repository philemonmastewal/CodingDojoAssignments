class Product(object):
    def __init__(self, price, item_name, weight, brand, cost, status="for sale"):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = status

    def sell(self):
        self.status = "sold"
        return self
    def addTax(self, tax):
        tax_cost = self.price*tax
        self.price = self.price+tax_cost
        return self
    def Return(self,reason):
        self.reason = reason
        if self.reason == "defective":
            self.status = "defective"
            self.price = 0
        elif self.reason == "like new":
            self.price = self.price
        elif self.reason =="open box":
            self.status = "used"
            self.price = self.price-(self.price*.20)
        return self
    def displayInfo(self):
        print self.price
        print self.item_name
        print self.weight
        print self.brand
        print self.cost
        print self.status
        return self
product1 = Product(100, "hammer", 1, "Duwalt", 100)
product1.addTax(.10).Return("open box").displayInfo()
