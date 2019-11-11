class Cat:
    def eat(self):
        print("%s love fish" % self.name)

    def drink(self):
        print("Cats need water")


tom = Cat()

tom.name = "Tom" # Give an object a nature from outside class. Not recommended.

tom.eat()
tom.drink()
print(tom)

lazy_cat = Cat()

lazy_cat.name = "LazyBones"

lazy_cat.eat()
lazy_cat.drink()
print(lazy_cat)
lazy_cat2 = lazy_cat
print(lazy_cat2)
