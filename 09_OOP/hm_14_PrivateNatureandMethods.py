class Women:

    def __init__(self, name):

        self.name = name
        self.__age = 18

    def __secret(self):
        print("%s is %d years old" % (self.name, self.__age))

rose = Women("Rose")

# print(rose.__age)

# rose.__secret()

# There is no real private in Python! hahah

print(rose._Women__age)

rose._Women__secret()