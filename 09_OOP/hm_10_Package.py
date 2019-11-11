class Person:
    """This is a person class"""

    def __init__(self, name, weight):

        self.name = name
        self.weight = weight

    def __str__(self):

        return "My Name is %s. I'm %.2f kg." % (self.name, self.weight)

    def run(self):

        print("%s loves run." % self.name)
        self.weight -= 0.5

    def eat(self):

        print("%s loves eat" % self.name)
        self.weight += 1


frank = Person("Frank", 75)
rose = Person("Rose", 45)
print(frank, rose)

rose.eat()
frank.run()

print(frank, rose)

rose.run()
frank.eat()

print(frank, rose)

