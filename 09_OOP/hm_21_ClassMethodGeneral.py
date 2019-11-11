class Game:

    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print("Help: Let Zombies In!!!")

    @classmethod
    def show_top_score(cls):
        print("The highest score is %d" % cls.top_score)

    def start_game(self):
        print("%s start the game" % self.player_name)


Game.show_help()

Game.show_top_score()

game = Game("Xiaoming")

game.start_game()