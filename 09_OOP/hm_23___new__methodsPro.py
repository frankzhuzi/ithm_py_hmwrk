class MusicPlayer(object):

    instance = None
    flag = False

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)

        return cls.instance

    def __init__(self):
        if MusicPlayer.flag is False:
            print("Initialising...")
            MusicPlayer.flag = True
        return


player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)
