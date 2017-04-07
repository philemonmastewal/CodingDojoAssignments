#print dir(object)

#class ClassName(object):
#  //attributes and methods here
#Think of the class as a blueprint for creating something. Once, we've finished our blueprint we can create instances of this class. The Human class we defined above is a blueprint for creating humans. We create a new instance by using the class name as if it were a function.

#EXAMPLE WITH human class
import random                      # import the random module
class Human(object):               # define a new Human class
    def __init__(self, clan=None): # define a parameter with a default value, clan
      print 'New Human!!!'
      # define attributes
      self.health = 100
      self.clan = clan
      self.strength = 3
      self.intelligence = 3
      self.stealth = 3
    # define methods
    def taunt(self):               # pass self into all methods to access attributes
      print "You want a piece of me?"
    def attack(self):
      self.taunt()                 # use the random module to generate a number when we attack
      luck = round(random.random() * 100)
      if(luck > 50):
        if(luck * self.stealth > 150):
          print 'attacking!'
          return True
        else:
          print 'attack failed'
          return False
      else:
        self.health -= self.strength
        print "attack failed"
        return False




import random                      # import the random module
class Human(object):               # define a new Human class
    def __init__(self, clan=None): # define a parameter with a default value, clan
      print 'New Human!!!'
      # define attributes
      self.health = 100
      self.clan = clan
      self.strength = 3
      self.intelligence = 3
      self.stealth = 3
    # define methods
    def taunt(self):               # pass self into all methods to access attributes
      print "You want a piece of me?"
    def attack(self):
      self.taunt()                 # use the random module to generate a number when we attack
      luck = round(random.random() * 100)
      if(luck > 50):
        if(luck * self.stealth > 150):
          print 'attacking!'
          return True
        else:
          print 'attack failed'
          return False
      else:
        self.health -= self.strength
        print "attack failed"
        return False


##inheritance

When we defined each of our classes, we typed Wizard(Human), Ninja(Human), and Samurai(Human). You could read each of these like "Make a class Wizard/Ninja/Samurai that inherits from Human". This is what is known as the implicit inheritance which allows us to use inherited attributes and methods of the Human(parent) class in our new subclasses.

A general skeleton for implicit inheritance:

class Parent(object): # inherits from the object class
  # parent methods and attributes here
class Child(Parent): #inherits from Parent class so we define Parent as the first parameter
  # parent methods and attributes are implicitly inherited
  # child methods and attributes

###SUPER###
Sometimes in your OOP code, you will want to create updated versions of methods that are defined in the parent class, because in addition to your custom code you want specifically to call the parent implementation of that method as well (or instead). In these cases, you would reference that parent object with the keyword ' super'. Specifically you reference that parent's method by calling 'super(ChildClassName, self).parent_method()'.


from human import Human
class Wizard(Human):
    def __init__(self):
        super(Wizard, self).__init__()   # use super to call the Human __init__ method
        self.intelligence = 10           # every wizard starts off with 10 intelligence
    def heal(self):
        self.health += 10
class Ninja(Human):
    def __init__(self):
        super(Ninja, self).__init__()    # use super to call the Human __init__ method
        self.stealth = 10                # every Ninja starts off with 10 stealth
    def steal(self):
        self.stealth += 5
class Samurai(Human):
    def __init__(self):
        super(Samurai, self).__init__()  # use super to call the Human __init__ method
        self.strength = 10               # every Samurai starts off with 10 strength
    def sacrifice(self):
        self.health -= 5
