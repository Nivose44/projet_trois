"""
that algorythm will take the informations contained inside board.py and divide
them equally among the lists of the two dimensionnal list list_board.
You can easily change the number of items by list by changing the modulo divider
of j: if the modulo is set to 5 (j%5 == 0), each list of list_board will contain
5 items if the number of item in board.py is big enough
"""
import random
#créer appel exception si les de board_size ne créent pas un board assez grand
class Board():
    """ The class Board manage all the objects and characters of the game and initialize the board"""
    WALL = "#"
    def __init__(self, height_board, lenght_board):
        """create a board from the file maze.py. height_board define the numbers of list in the list board and lenght_board the number of element by list"""
        self.all_object = {}
        self.start_position = {}
        self.end_posititon = {}
        #self.objects_content =  self.board[self.object[content].column][self.object[content].line]
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
        """that method will change the position of the object untill it find an
        empty space and place it on the board, and add them in a dictionnary so that we
        know how many objects are on the board"""
        while self.board[object.line][object.column] != " ":
            self.set_position_object(object)
        self.board[object.line][object.column] = object.content
        self.all_object[object.content] = object
    def put_object_on_wall(self, object):
        """ methode use to place the object in a place where the hero can't reach it again"""
        while self.board[object.line][object.column] != "#":
            self.set_position_object(object)
    def set_position_object(self, object):
        """ define randomly, depending of the size of the board, the value of line and column of the object used in argument"""
        object.line = random.randint(0, 14)
        object.column = random.randint(0, 14)
    def pickup_object(self, character, object):
        """ remove the object from a accessible place for the hero and increase the number of object in nhis bag"""
        for content in object:
            if self.board[character.line][character.column] == self.board[self.all_object[content].line][self.all_object[content].column]:
                self.put_object_on_wall(object[content])
                character.bag += 1
                print("objet(s) ramassé(s): ", character.bag)
    def check_character_bag(self, character):
        """ method called when the hero reach the guardian so that it is checked if the hero has picked up all the object"""
        if character.bag == len(self.all_object):
            return True
        else:
            self.board[character.line][character.column] = " "
            self.display_board()
            print("You are dead, you should have pick up all the object")
    #methods to manage the hero on the board
    def put_hero_on_board(self, character):
        """place the hero on the board"""
        self.board[character.line][character.column] = character.contenu
    def set_position_hero(self, character):
        """define the position of the hero on the place on the board where the maze begin"""
        character.column = self.start_position["column"]
        character.line = self.start_position["line"]
    def movement(self, character):
        """change the position of the hero by one in one direction, if there is a wall on that position, the position get back to his previous value and we don't call put_hero_on_board,
        if the new position is the same as the one of the guardian we check the value of the attribute bag of the hero: if the value equal the number of object created
        the hero win, otherwise he lose.In both cases the game end."""
        move = input("Write q(left), s(down), d(right) or z(up) and press Enter to move:")
        if move == "q":
            character.column -= 1
            if self.board[character.line][character.column] == self.WALL:
                character.column += 1
                print("Ouch, you just hit a wall.Try again.")
            elif self.board[character.line][character.column] == self.board[self.end_position["line"]][self.end_position["column"]]:
                character.column += 1
                if self.check_character_bag:
                    character.column -= 1
                    self.put_hero_on_board(character)
                    self.board[character.line-1][character.column] = " "
                    self.display_board()
                    print("Houra, you won")
                else:
                    character.column -= 1
            else:
                self.put_hero_on_board(character)
                self.board[character.line][character.column+1] = " "
                self.display_board()
                self.pickup_object(character, self.all_object)
        elif move == "s":
            character.line += 1
            if self.board[character.line][character.column] == self.WALL:
                character.line -= 1
                print("Ouch, you just hit a wall.Try again.")
            elif self.board[character.line][character.column] == self.board[self.end_position["line"]][self.end_position["column"]]:
                character.line -= 1
                if self.check_character_bag(character):
                    character.line += 1
                    self.put_hero_on_board(character)
                    self.board[character.line-1][character.column] = " "
                    self.display_board()
                    print("Houra, you won")
                else:
                    character.line += 1
            else:
                self.put_hero_on_board(character)
                self.board[character.line-1][character.column] = " "
                self.display_board()
                self.pickup_object(character, self.all_object)
        elif move == "d":
            character.column += 1
            if self.board[character.line][character.column] == self.WALL:
                character.column -= 1
                print("Ouch, you just hit a wall.Try again.")
            elif self.board[character.line][character.column] == self.board[self.end_position["line"]][self.end_position["column"]]:
                character.column -= 1
                if self.check_character_bag:
                    character.column += 1
                    self.put_hero_on_board(character)
                    self.board[character.line-1][character.column] = " "
                    self.display_board()
                    print("Houra, you won")
                else:
                    character.column += 1
            else:
                self.put_hero_on_board(character)
                self.board[character.line][character.column-1] = " "
                self.display_board()
                self.pickup_object(character, self.all_object)
        elif move == "z":
            character.line -= 1
            if self.board[character.line][character.column] == self.WALL:
                character.line += 1
                print("Ouch, you just hit a wall.Try again.")
            elif self.board[character.line][character.column] == self.board[self.end_position["line"]][self.end_position["column"]]:
                character.line += 1
                if self.check_character_bag:
                    character.line -= 1
                    self.put_hero_on_board(character)
                    self.board[character.line-1][character.column] = " "
                    self.display_board()
                    print("Houra, you won")
                else:
                    character.line -= 1
            else:
                self.put_hero_on_board(character)
                self.board[character.line+1][character.column] = " "
                self.display_board()
                self.pickup_object(character, self.all_object)
        else:
            print("Vous avez gagné!Non je rigole petit malin, utilise donc les touches indiquées")
    #methods to manage the guardian on the board
    def put_guardian_on_board(self, character):
        """ place the guardian on the board"""
        self.board[character.line][character.column] = character.contenu
    def set_position_guardian(self, character):
        """ define the position of the guardian on the place on the board where the maze end"""
        character.column = self.end_position["column"]
        character.line = self.end_position["line"]
    #method to display the board
    def display_board(self):
        """display the board"""
        for line in self.board:
            print("".join(line))
