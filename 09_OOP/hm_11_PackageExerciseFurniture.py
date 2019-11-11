class HouseItem:

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "This is a %s, it takes %.2f m2" % (self.name, self.area)


class House:

    def __init__(self):
        pass

    def __str__(self):
        pass

    def add_item(self):
        pass


bed = HouseItem("bed", 4)
print(bed)
chest = HouseItem("chest", 2)
print(chest)
table = HouseItem("table", 1.5)
print(table)


