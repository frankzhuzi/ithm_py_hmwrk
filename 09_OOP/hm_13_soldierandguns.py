class Gun:

    def __init__(self, model):

        self.model = model
        self.bullet = 0

    def __str__(self):

        return "This is a %s gun" % self.model

    def reload(self, count):

        self.bullet += count

    def shoot(self):

        if self.bullet <= 0:
            print("Out of armor! fail to shoot!")
            return

        self.bullet -= 1

        print("[%s]Boo! [%d]" % (self.model, self.bullet))


class Soldier:

    def __init__(self, name):

        self.name = name

        self.gun = None

    def fire(self):

        if self.gun is None:
            print("%s doesn't have a gun" % self.name)
            return

        print("Fuck you all!")

        self.gun.reload(100)

        self.gun.shoot()


ak47 = Gun("Ak47")

frank = Soldier("Frank")
frank.gun = ak47
print(frank.gun)

frank.fire()