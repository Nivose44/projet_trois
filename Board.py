"""
that algorythm will take the informations contained inside board.py and divide
them equally among the lists of the two dimensionnal list list_board.
You can easily change the number of items by list by changing the modulo divider
of j: if the modulo is set to 5 (j%5 == 0), each list of list_board will contain
5 items if the number of item in board.py is big enough
"""
import random
class Board():
    """ class to initialize the board and manage the object and characters on it"""
    WALL = "#"
    GO_LEFT = 0
    GO_RIGHT = 1
    GO_DOWN = 2
    GO_UP = 3
    def __init__(self, height_board, lenght_board):
        """
        Create the board.
        Height_board will define the number of list in the list and
        lenght_board the number of elements by list.
        """
        self.all_object = {}
        self.start_position = {}
        self.end_posititon = {}
        with open("maze.py", "r") as file:
            file = [i.replace('\n', '') for i in file]
            self.board = [[] for k in range(height_board)]
            i = 0
            j = 0
            for line in file:
                for number in line:
                    if int(number) == 0:
                        self.board[i].append("#")
                    elif int(number) == 1:
                        self.board[i].append(" ")
                    elif int(number) == 3:
                        self.board[i].append(number)
                        self.start_position = {"line":i, "column":self.board[i].index("3")}
                    elif int(number) == 4:
                        self.board[i].append(number)
                        self.end_position = {"line":i, "column":self.board[i].index("4")}
                    j += 1
                    if j % lenght_board == 0:
                        i += 1

# methods to manage the objects on the board
    def put_object_on_board(self, object):
        """
        That method will change the position of the object untill it find
        an empty space and place it on the board,and add them in a dictionnary
        so that we know how many objects are on the board.
         """
        while self.board[object.line][object.column] != " ":
            self.set_position_object(object)
        self.board[object.line][object.column] = object.content
        self.all_object[object.content] = object

    def put_object_on_wall(self, object):
        """
        That method will place the position of te object on a place where
        there is a wall so that the hero can't walk
        and pick up twice the same object.
        """
        while self.board[object.line][object.column] != "#":
            self.set_position_object(object)

    def set_position_object(self, object):
        """
        Define randomly, depending of the size of the board,
        the value of line and column of the object used in argument.
        """
        object.line = random.randint(0, 14)
        object.column = random.randint(0, 14)

    def pickup_object(self, character, object):
        """
        Check the position of the hero to know if there is an object on his
        position and increase his attribute bag after calling the method put_object_on_wall.
        """
        for content in object:
            if self.board[character.line][character.column] == self.board[self.all_object[content].line][self.all_object[content].column]:
            #compare the position of the character with the position of all the objects created with the class Obj
                self.put_object_on_wall(object[content])
                character.bag += 1
                print("object(s) picked up: ", character.bag)

    def check_character_bag(self, character):
        """
        Check the number of object the hero picked up so that the board know if
        the player won or not when he reach the guardian.
        """
        if character.bag == len(self.all_object):
            return True
        else:
            self.board[character.line][character.column] = " "
            self.display_board()
            print("You are dead, you should have pick up all the object")

#methods to manage the hero on the board
    def put_hero_on_board(self, character):
        """place the visual representation of the hero on the board"""
        self.board[character.line][character.column] = character.contenu

    def set_position_hero(self, character):
        """define the position of the hero"""
        character.column = self.start_position["column"]
        character.line = self.start_position["line"]

    def positioned_on_wall(self, character):
        """ check if the character is positioned on a wall"""
        if self.board[character.line][character.column] == self.WALL:
            print("Ouch, you just hit a wall.Try again.")
            return True

    def positioned_on_guardian(self, character):
        """check if the character is positioned on the same position as the guardian"""
        if self.board[character.line][character.column] == self.board[self.end_position["line"]][self.end_position["column"]]:
            return True

    def move_back(self, character, side_to_move):
        """Move the position of the character in the opposite direction indicated by the user"""
        if side_to_move == self.GO_LEFT:
            self.move_forward(character, self.GO_RIGHT)
        if side_to_move == self.GO_RIGHT:
            self.move_forward(character, self.GO_LEFT)
        if side_to_move == self.GO_DOWN:
            self.move_forward(character, self.GO_UP)
        if side_to_move == self.GO_UP:
            self.move_forward(character, self.GO_DOWN)

    def move_forward(self, character, side_to_move):
        """Move the position of the character in the direction indicated by the user"""
        if side_to_move == self.GO_LEFT:
            character.column -= 1
        if side_to_move == self.GO_RIGHT:
            character.column += 1
        if side_to_move == self.GO_DOWN:
            character.line += 1
        if side_to_move == self.GO_UP:
            character.line -= 1

    def update_character_info(self, character, side_to_move):
        """
        Update all the infos of the character.
        We first make the character walk back to erase is visual representation on the board
        before replacing it to the position the user asked him to move to.We then check that 
        the character isn't standing on the object by calling pickup_object and
        the we display the board with the character at his new position.
        """
        self.move_back(character, side_to_move)
        self.board[character.line][character.column] = " "
        self.move_forward(character, side_to_move)
        self.put_hero_on_board(character)
        self.pickup_object(character, self.all_object)
        self.display_board()

    def move(self, character):
        """
        Move the character on a different position on the board.
        Change the position of the hero by one in one direction, if there is a wall on that
        position, the position get back to his previous value and we don't call put_hero_on_board,
        if the new position is the same as the one of the guardian we check the value of
        the attribute bag of the hero: if the value equal the number of object created
        the hero win, otherwise he loses.In both cases the game end.
        """
        move = input("Write q(left), s(down), d(right) or z(up) and press Enter to move:")
        if move == "q":
            side_to_move = self.GO_LEFT
            self.move_forward(character, side_to_move)
            if self.positioned_on_wall(character):
                self.move_back(character, side_to_move)
            else:
                self.update_character_info(character, side_to_move)
                if self.positioned_on_guardian(character):
                    if self.check_character_bag(character):
                        print("Houra, you won")

        elif move == "s":
            side_to_move = self.GO_DOWN
            self.move_forward(character, side_to_move)
            if self.positioned_on_wall(character):
                self.move_back(character, side_to_move)
            else:
                self.update_character_info(character, side_to_move)
                if self.positioned_on_guardian(character):
                    if self.check_character_bag(character):
                        print("Houra, you won")

        elif move == "d":
            side_to_move = self.GO_RIGHT
            self.move_forward(character, side_to_move)
            if self.positioned_on_wall(character):
                self.move_back(character, side_to_move)
            else:
                self.update_character_info(character, side_to_move)
                if self.positioned_on_guardian(character):
                    if self.check_character_bag(character):
                        print("Houra, you won")

        elif move == "z":
            side_to_move = self.GO_UP
            self.move_forward(character, side_to_move)
            if self.positioned_on_wall(character):
                self.move_back(character, side_to_move)
            else:
                self.update_character_info(character, side_to_move)
                if self.positioned_on_guardian(character):
                    if self.check_character_bag(character):
                        print("Houra, you won")

        else:
            print("You won!Just Kidding.You can only press the letters that i indicated to move")

#methods to manage the guardian on the board
    def put_guardian_on_board(self, character):
        """Place the visual representation of the guardian on the board."""
        self.board[character.line][character.column] = character.contenu

    def set_position_guardian(self, character):
        """Define the position of the guardian."""
        character.column = self.end_position["column"]
        character.line = self.end_position["line"]

#method to display the board
    def display_board(self):
        """Transform the board into a list and display it."""
        for line in self.board:
            print("".join(line))