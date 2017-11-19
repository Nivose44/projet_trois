"""
class Launcher
"""
class Launcher():
    """
    That class will create the board and all the object and characters and
    place them on the board whith the method init and can launch the game with
    the method launch
    """
    def __init__(self, Board, Character, Object):
        self.board = Board(15, 15)
        self.needle = Object("N")
        self.ether = Object("E")
        self.tube = Object("T")
        self.board.put_object_on_board(self.needle)
        self.board.put_object_on_board(self.ether)
        self.board.put_object_on_board(self.tube)
        self.hero = Character("H")
        self.guardian = Character("G")
        self.board.set_position_hero(self.hero)
        self.board.put_hero_on_board(self.hero)
        self.board.set_position_guardian(self.guardian)
        self.board.put_guardian_on_board(self.guardian)
        self.board.display_board()
        self.launch()
    def launch(self):
        """
        launch will create a loop that will call the method movement untill
        the hero reached the guardian
        """
        while self.board.board[self.hero.line][self.hero.column] != self.board.board[self.board.end_position["line"]][self.board.end_position["column"]]:
            self.board.movement(self.hero)
