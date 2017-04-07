class Product(object):
    def __init__(self, name):
        self.name = name

class Store(object):
    def __init__(self, location, owner):
        self.products = []
        self.location = location
        self.owner = owner
    def add_product(self, product):
        self.products.append(product)
        return self

    def remove_product(self, product):
        self.products.remove(product)
        return self
    def inventory(self):
        print self.products
    def displayInfo(self):
        print(self.products, self.location, self.owner)
store1 = Store("Denver", "Tyler")
store1.add_product("tuna").add_product("soda").add_product("chips").add_product("dog-food").add_product("bread").add_product("milk")
store1.displayInfo()
store1.remove_product("tuna")
store1.remove_product("soda")
store1.displayInfo()
