class Cat:
    """This is a Cat class"""

    def __init__(self):

        print("This is a initialising method")
        self.name = "Tom"

    def eat(self):
        print("%s loves fish" % self.name)


tom = Cat()
tom.eat()
print(tom.name)