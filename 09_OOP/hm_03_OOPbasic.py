class Cat:
    def eat(self):
        print("Cats love fish")

    def drink(self):
        print("Cats need water")

tom = Cat()
tom.eat()
tom.drink()

print(tom)

addr = id(tom)
print("%d" % addr)
print("%x" % addr)
