"""
class Board
"""
import random
import pygame
from pygame.locals import *

pygame.init()
class Board():
    """ class to initialize the board and manage the object and characters on it"""
    WALL = "#"
    LEFT = 0
    RIGHT = 1
    DOWN = 2
    UP = 3
    def __init__(self):
        self.all_object = {}
        self.start_position = {}
        self.end_posititon = {}
        with open("maze.py", "r") as f:
            file = [i.replace('\n', '') for i in f]
            self.board = [[] for k in range(15)]
            self.all_object = {}
            self.start_position = {}
            self.end_position = {}
            self.black = (0, 0, 0)
            self.font = pygame.font.SysFont('Arial', 15)
            self.x = 480
            self.y = 480
            self.size_screen = (self.x, self.y)
            self.screen = pygame.display.set_mode(self.size_screen)
            self.wall = pygame.transform.scale(pygame.image.load("images/wall.png").convert(), (int(self.x / 15), int(self.y / 15)))
            self.floor = pygame.transform.scale(pygame.image.load("images/floor.jpg").convert(), (int(self.x / 15), int(self.y / 15)))
            self.death = pygame.transform.scale(pygame.image.load("images/death.png").convert(), (int(self.x / 15), int(self.y / 15)))
            i = 0
            j = 0
            for numbers in file:
                for number in numbers:
                    if int(number) == 0:
                        self.board[i].append("#")
                        self.screen.blit(self.wall, (int(self.x / 15)*j, int(self.y / 15)*i))
                    elif int(number) == 1:
                        self.board[i].append(" ")
                        self.screen.blit(self.floor, (int(self.x / 15)*j, int(self.y / 15)*i))
                    elif int(number) == 3:
                        self.board[i].append(number)
                        self.screen.blit(self.floor, (int(self.x / 15)*j, int(self.y / 15)*i))
                        self.start_position = {"line":i, "column":j}
                    elif int(number) == 4:
                        self.board[i].append(number)
                        self.screen.blit(self.floor, (int(self.x / 15)*j, int(self.y / 15)*i))
                        self.end_position = {"line":i, "column":j}
                    j += 1
                    if j%15 == 0:
                        i += 1
                        j = 0
            pygame.display.flip()

# methods to manage the objects on the board
    def put_object_on_board(self, object):
        """
        That method will change the position of the object untill it find
        an empty space, place it on the board,and stock them inside a
        dictionnary.
         """
        while self.board[object.line][object.column] != " ":
            self.set_position_object(object)
        self.board[object.line][object.column] = object.name
        self.all_object[object.content] = object
        object.content = pygame.transform.scale(object.content, (int(self.x/ 15), int(self.y/ 15)))
        self.screen.blit(object.content, (int(self.x / 15)*object.column, int(self.y / 15)*object.line))
        pygame.display.flip()

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
                print("object picked up: ", character.bag)
                self.screen.blit(self.wall, (int(self.x / 15)*14, 0))
                self.screen.blit(self.font.render('Object(s) picked up : ' + str(character.bag), True, (255, 255, 255)), (320, 10))
                pygame.display.update()

    def check_character_bag(self, character):
        """
        Check the number of object the hero picked up so that the board know if
        the player won or not when he reach the guardian.
        """
        if character.bag == len(self.all_object):
            return True

#methods to manage the hero on the board
    def put_hero_on_board(self, character):
        """place the visual representation of the hero on the board"""
        character.content = pygame.transform.scale(character.content, (int(self.x/ 15), int(self.y/ 15)))
        self.screen.blit(character.content, character.position)
        self.board[character.line][character.column] = "M"

    def set_position_hero(self, character):
        """define the position of the hero"""
        character.column = self.start_position["column"]
        character.line = self.start_position["line"]
        character.position.x = int(self.x / 15)*character.column
        character.position.y = int(self.y / 15)*character.line

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
        if side_to_move == self.LEFT:
            self.move_forward(character, self.RIGHT)
        if side_to_move == self.RIGHT:
            self.move_forward(character, self.LEFT)
        if side_to_move == self.DOWN:
            self.move_forward(character, self.UP)
        if side_to_move == self.UP:
            self.move_forward(character, self.DOWN)

    def move_forward(self, character, side_to_move):
        """Move the position of the character in the direction indicated by the user"""
        if side_to_move == self.LEFT:
            character.column -= 1
            character.position = character.position.move(-(int(self.x / 15)), 0)
        if side_to_move == self.RIGHT:
            character.column += 1
            character.position = character.position.move((int(self.x / 15)), 0)
        if side_to_move == self.DOWN:
            character.line += 1
            character.position = character.position.move(0, int(self.y / 15))
        if side_to_move == self.UP:
            character.line -= 1
            character.position = character.position.move(0, -(int(self.y / 15)))

    def update_character_info(self, character, side_to_move):
        """
        Update all the infos of the character.
        We first make the character walk back to erase is visual representation on the board
        before replacing it to the position the user asked him to move to.We then check if
        the character is standing on an object by calling pickup_object and
        then we display the board with the character at his new position.
        """
        self.move_back(character, side_to_move)
        self.board[character.line][character.column] = " "
        self.screen.blit(self.floor, character.position)
        self.move_forward(character, side_to_move)
        self.pickup_object(character, self.all_object)
        self.screen.blit(character.content, character.position)
        pygame.display.flip()
        self.pickup_object(character, self.all_object)


    def move(self, character, side_to_move):
        """
        Pattern that the character will do every time he moves.
        Change the position of the hero by one in one direction.If there is a wall on that
        position, the position get back to his previous value and we don't call put_hero_on_board.
        If the new position is the same as the one of the guardian, we check the value of
        the attribute bag of the hero: if the value equal the number of object created,
        the hero win and is displayed on the guardian position, otherwise he loses.
        In both cases the game end.
        """
        self.move_forward(character, side_to_move)
        if self.positioned_on_wall(character):
            self.move_back(character, side_to_move)
        else:
            if self.positioned_on_guardian(character):
                if self.check_character_bag(character):
                    self.update_character_info(character, side_to_move)
                    self.put_hero_on_board(character)
                    self.display_board()
                    print("Houra, you won")
                else:
                    #We don't update the visual representation of the character because he lost
                    #So only the guardian is left on the board
                    self.move_back(character, side_to_move)
                    self.display_board()
                    self.screen.blit(self.death, character.position)
                    pygame.display.flip()
                    self.move_forward(character, side_to_move)
                    print("You lose.Next time pick up all the objects")
            else:
                self.update_character_info(character, side_to_move)
                self.put_hero_on_board(character)
                self.display_board()
#methods to manage the guardian on the board
    def put_guardian_on_board(self, character):
        """Place the visual representation of the guardian on the board."""
        character.content = pygame.transform.scale(character.content, (int(self.x/ 15), int(self.y/ 15)))
        self.screen.blit(character.content, character.position)
        self.board[character.line][character.column] = "G"

    def set_position_guardian(self, character):
        """Define the position of the guardian."""
        character.column = self.end_position["column"]
        character.line = self.end_position["line"]
        character.position.x = int(self.x / 15)*character.column
        character.position.y = int(self.y / 15)*character.line

#method to display the board
    def display_board(self):
        """Transform the board into a list and display it."""
        for line in self.board:
            print("".join(line))
