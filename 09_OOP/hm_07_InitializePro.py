class Cat:
    """This is a Cat class"""

    def __init__(self, new_name):

        print("This is a initialising method")
        self.name = new_name

    def eat(self):
        print("%s loves fish" % self.name)


tom = Cat("Tom")
tom.eat()
print(tom.name)

lazy_cat = Cat("LazyBones")
lazy_cat.eat()
print(lazy_cat.name)