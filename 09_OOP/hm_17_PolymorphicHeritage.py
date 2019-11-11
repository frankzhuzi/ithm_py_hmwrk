class Dog(object):

    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s plays around" % self.name)


class Xiaotian(Dog):

    def game(self):
        print("%s flies up to sky" % self.name)


class Person(object):

    def __init__(self, name):
        self.name = name

    def play_with_dog(self, dog):
        print("%s is playing with %s happily" % (self.name, dog.name))

        dog.game()


wangcai = Dog("Wangcai")
xiaotian = Xiaotian("Xiaotian")
xiaoming = Person("Xiaoming")

xiaoming.play_with_dog(wangcai)
xiaoming.play_with_dog(xiaotian)





