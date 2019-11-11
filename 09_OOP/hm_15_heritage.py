class Animal:

    def eat(self):
        print("Yum!")

    def drink(self):
        print("Gulu...")

    def run(self):
        print("huhuhu~~~")

    def sleep(self):
        print("Zzz...")


class Dog(Animal):

    def bark(self):
        print("Wang!")


class Xiaotian(Dog):

    def fly(self):
        print("I can fly! hoo~")

    def bark(self):
        print("I'm your father hahaha!")
        # override a method
        super().bark()
        super().sleep()


black = Xiaotian()

black.drink()
black.bark()
black.fly()