# class User(object):
#     name = "Anna"
# anna = User()
# print "anna's name: ", anna.name
# User.name = "Bob"
# print "anna's name after change:", anna.name
# bob = User()
# print "bob's name:", bob.name


class Human(object):
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height


user1 = Human(Tyler, 25, "6'0")
print user1.name


# class Animal(object):
#     def __init__(self,name,size):
#         self.name = name
#         self.size = size
