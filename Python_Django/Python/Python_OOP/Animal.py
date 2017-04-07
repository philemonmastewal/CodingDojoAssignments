class Animal(object):
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def displayInfo(self):
        print ("This animal is called:" +" "+ self.name + " "+"and it has"+" "+str(self.health)+" "+"health points remaining.")
        return self
Turtle = Animal("Turtle")
Turtle.walk().walk().walk().run().run().displayInfo()

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150
    def pet(self):
        self.health += 5
        return self
Fido = Dog("Fido")
Fido.walk().walk().walk().run().run().pet().displayInfo()

class Dragon(Animal):
    def __init__(self,name):
        super(Dragon,self).__init__(name)
        self.health = 170
    def fly(self):
        self.health -= 10
        return self
David = Dragon("David")
David.walk().walk().walk().run().run().fly().displayInfo()
