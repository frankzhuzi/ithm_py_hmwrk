class Cat:
    def eat(self):
        print("Cats love fish")

    def drink(self):
        print("Cats need water")

tom = Cat()
tom.eat()
tom.drink()
print(tom)

lazy_cat = Cat()

lazy_cat.eat()
lazy_cat.drink()
print(lazy_cat)
lazy_cat2 = lazy_cat
print(lazy_cat2)
