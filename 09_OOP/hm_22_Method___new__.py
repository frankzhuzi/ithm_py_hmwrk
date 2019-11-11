class MusicPlayer(object):

    def __new__(cls, *args, **kwargs):
        print("Create an object, make a space!")
        instance = super().__new__(cls)
        return instance

    def __init__(self):
        print("Initialising a music player...")

player = MusicPlayer()
print(player)