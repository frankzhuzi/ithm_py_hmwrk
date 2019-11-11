class HouseItem:

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "This is a %s, it takes %.2f m2" % (self.name, self.area)


class House:

    def __init__(self, house_type, area):

        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []

    def __str__(self):

        return ("This is a %s house. it takes %.2f m2, now remain %.2f m2. " 
               "We have %s in this house"
                % (self.house_type, self.area,
                                             self.free_area, self.item_list))

    def add_item(self, item):

        print("We need to add a %s" % item.name)
        if item.area > self.free_area:
            print("Free Space is not enough...")
            return
        self.item_list.append(item.name)
        self.free_area -= item.area


bed = HouseItem("bed", 4)
print(bed)
chest = HouseItem("chest", 2)
print(chest)
table = HouseItem("table", 1.5)
print(table)

my_home = House("SwimPool", 60)
my_home.add_item(bed)
print(my_home)
my_home.add_item(chest)
print(my_home)
my_home.add_item(table)
print(my_home)


