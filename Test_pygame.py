"""
that algorythm will take the informations contained inside board.py and divide
them equally among the lists of the two dimensionnal list list_board.
You can easily change the number of items by list by changing the modulo divider
of j: if the modulo is set to 5 (j%5 == 0), each list of list_board will contain
5 items if the number of item in board.py is big enough
"""
import random
import pygame
from pygame.locals import *

pygame.init()
class Board():
    def __init__(self):
        with open("maze.py", "r") as f:
            f = [i.replace('\n','') for i in f]
            self.board = [[] for k in range(15) ]
            self.all_object = {}
            self.start_position = {}
            self.end_position = {}
            self.x=480
            self.y=480
            self.size_fenetre=(self.x,self.y)
            self.fenetre = pygame.display.set_mode(self.size_fenetre)
            self.wall = pygame.transform.scale(pygame.image.load("images/wall.png").convert(), (int(self.x / 15),int(self.y / 15)))
            self.floor = pygame.transform.scale(pygame.image.load("images/floor.jpg").convert(), (int(self.x / 15),int(self.y / 15)))
            self.death = pygame.transform.scale(pygame.image.load("images/death.png").convert(), (int(self.x / 15),int(self.y / 15)))
            i=0
            j=0
            for numbers in f:                
                for number in numbers:
                    if int(number) == 0:
                        self.board[i].append("#")
                        self.fenetre.blit(self.wall, (int(self.x / 15)*j,int(self.y / 15)*i))
                    elif int(number) == 1:
                        self.board[i].append(" ")
                        self.fenetre.blit(self.floor, (int(self.x / 15)*j,int(self.y / 15)*i))
                    elif int(number) == 3:
                        self.board[i].append(number)
                        self.fenetre.blit(self.floor, (int(self.x / 15)*j,int(self.y / 15)*i))
                        self.start_position = {"line":i, "column":j}
                    elif int(number) == 4:
                        self.board[i].append(number)
                        self.fenetre.blit(self.floor, (int(self.x / 15)*j,int(self.y / 15)*i))
                        self.end_position = {"line":i, "column":j}
                    j += 1
                    if j%15 == 0: 
                        i += 1
                        j = 0
            pygame.display.flip()
    #methods to manage objects
    def put_object_on_board(self, object):
        while self.board[object.line][object.column] != " ":
            self.set_position_object(object)
        self.board[object.line][object.column] = "O"
        self.all_object[object.content] = object
        object.content = pygame.transform.scale(object.content, (int(self.x/ 15),int(self.y/ 15)))
        self.fenetre.blit(object.content, (int(self.x / 15)*object.column, int(self.y / 15)*object.line))
        #la mérthode d'affichage de blt fonctionne à l'envers de la logique d'organisation en list de list
        self.display_board()
        pygame.display.flip()
    def put_object_on_wall(self, object):
        """ that method will place the position of te object on a place where there is a wall so that the hero can't walk and pick up twice the same object"""
        while self.board[object.line][object.column] != "#":
            self.set_position_object(object)
    def set_position_object(self, object):
        object.line = random.randint(0, 14)
        object.column = random.randint(0, 14)
            #method to display the board
    def display_board(self):
        for line in self.board:
            print("".join(line))
    def pickup_object(self, character, object):
        """check the position of the hero to know if there is an object on his position and increase his attribute bag after calling the method put_object_on_wall"""
        for content in object:
            if self.board[character.line][character.column] == self.board[self.all_object[content].line][self.all_object[content].column]:
                self.put_object_on_wall(object[content])
                character.bag += 1
                print("objet(s) ramassé(s): ", character.bag)
    def check_character_bag(self, character):
        """check the number of object the hero picked up so that the board know if the player won or not when he reach the guardian"""
        if character.bag == len(self.all_object):
            return True
        else:
            self.fenetre.blit(self.death, character.position)
            pygame.display.flip()
            print("You are dead, you should have pick up all the object")
    #methods to manage the hero on the board
    def put_hero_on_board(self, character):
        """place the hero on the board"""
        character.content = pygame.transform.scale(character.content, (int(self.x/ 15),int(self.y/ 15)))
        self.fenetre.blit(character.content, character.position)
        self.board[character.line][character.column] = "M"
    def set_position_hero(self, character):
        """define the position of the hero"""
        character.column = self.start_position["column"]
        character.line = self.start_position["line"]
        character.position.x = int(self.x / 15)*character.column
        character.position.y = int(self.y / 15)*character.line
    #methods to manage the guardian on the board
    def put_guardian_on_board(self, character):
        """place the hero on the board"""
        character.content = pygame.transform.scale(character.content, (int(self.x/ 15),int(self.y/ 15)))
        self.fenetre.blit(character.content, character.position)
        self.board[character.line][character.column] = "G"
    def set_position_guardian(self, character):
        """define the position of the hero"""
        character.column = self.end_position["column"]
        character.line = self.end_position["line"]
        character.position.x = int(self.x / 15)*character.column
        character.position.y = int(self.y / 15)*character.line


"""
class object créant les objets ainsi que les fonctions définissant leur position
et les placant dans le tableau
"""
class Object():
    def __init__(self, content, board_object):
        #améliroer le code pour que board_object ne soit pas utilisé en variable globale
        self.line = 0
        self.column = 0
        self.content = pygame.image.load(content).convert()
        self.content.set_colorkey((255,255,255))
        

    
"""
class pour créer macgyver et le faire se mouvoir
"""
class Character():
    def __init__(self, content):
        self.line = 0
        self.column = 0
        self.bag = 0
        self.content = pygame.image.load(content).convert()
        self.position = self.content.get_rect()
        
            

premier_Board = Board()
macgyver = Character("images/macgyver.png")
premier_Board.set_position_hero(macgyver)
premier_Board.put_hero_on_board(macgyver)
guardian = Character("images/guardian.png")
premier_Board.set_position_guardian(guardian)
premier_Board.put_guardian_on_board(guardian)
aiguille = Object( "images/needle.png", premier_Board)
tube = Object( "images/tube.png", premier_Board)
ether = Object( "images/ether.png", premier_Board)
premier_Board.put_object_on_board(aiguille)
premier_Board.put_object_on_board(tube)
premier_Board.put_object_on_board(ether)


#BOUCLE INFINIE
continuer = 1
while premier_Board.board[macgyver.line][macgyver.column] != premier_Board.board[premier_Board.end_position["line"]][premier_Board.end_position["column"]]:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
                    if event.key == K_DOWN:
                        if premier_Board.board[macgyver.line+1][macgyver.column] == "#":
                            print("Ouch, you just hit a wall.Try again.")
                        elif premier_Board.board[macgyver.line+1][macgyver.column] == premier_Board.board[premier_Board.end_position["line"]][premier_Board.end_position["column"]]:
                            macgyver.line += 1
                            if premier_Board.check_character_bag(macgyver):
                                premier_Board.fenetre.blit(premier_Board.floor, macgyver.position)
                                macgyver.position = macgyver.position.move(0, int(premier_Board.y / 15))
                                premier_Board.fenetre.blit(macgyver.content, macgyver.position)
                                pygame.display.flip()
                                print("Houra, you won you hardcore gamer!")

                        else:
                            macgyver.line += 1
                            premier_Board.board[macgyver.line][macgyver.column] = "M"
                            premier_Board.board[macgyver.line-1][macgyver.column] = " "
                            premier_Board.display_board()
                            premier_Board.fenetre.blit(premier_Board.floor, macgyver.position)
                            macgyver.position = macgyver.position.move(0, int(premier_Board.y / 15))
                            premier_Board.fenetre.blit(macgyver.content, macgyver.position)
                            pygame.display.flip()
                            premier_Board.pickup_object(macgyver, premier_Board.all_object)
                        

                    elif event.key == K_UP:
                        if premier_Board.board[macgyver.line-1][macgyver.column] == "#":
                            print("Ouch, you just hit a wall.Try again.")
                        elif premier_Board.board[macgyver.line-1][macgyver.column] == premier_Board.board[premier_Board.end_position["line"]][premier_Board.end_position["column"]]:
                            macgyver.line -= 1
                            if premier_Board.check_character_bag(macgyver):
                                premier_Board.fenetre.blit(premier_Board.floor, macgyver.position)
                                macgyver.position = macgyver.position.move(0, int(premier_Board.y / 15))
                                premier_Board.fenetre.blit(macgyver.content, macgyver.position)
                                pygame.display.flip()
                                print("Houra, you won you hardcore gamer!")
                        else:
                            macgyver.line -= 1
                            premier_Board.board[macgyver.line][macgyver.column] = "M"
                            premier_Board.board[macgyver.line+1][macgyver.column] = " "
                            premier_Board.display_board()
                            premier_Board.fenetre.blit(premier_Board.floor, macgyver.position)
                            macgyver.position = macgyver.position.move(0, -(int(premier_Board.y / 15)))
                            premier_Board.fenetre.blit(macgyver.content, macgyver.position)
                            pygame.display.flip()
                            premier_Board.pickup_object(macgyver, premier_Board.all_object)
                        
                    elif event.key == K_LEFT:
                        if premier_Board.board[macgyver.line][macgyver.column-1] == "#":
                            print("Ouch, you just hit a wall.Try again.")
                        elif premier_Board.board[macgyver.line][macgyver.column-1] == premier_Board.board[premier_Board.end_position["line"]][premier_Board.end_position["column"]]:
                            macgyver.column -= 1
                            if premier_Board.check_character_bag(macgyver):
                                premier_Board.fenetre.blit(premier_Board.floor, macgyver.position)
                                macgyver.position = macgyver.position.move(0, int(premier_Board.y / 15))
                                premier_Board.fenetre.blit(macgyver.content, macgyver.position)
                                pygame.display.flip()
                                print("Houra, you won you hardcore gamer!")
                        else:
                            macgyver.column -= 1
                            premier_Board.board[macgyver.line][macgyver.column] = "M"
                            premier_Board.board[macgyver.line][macgyver.column+1] = " "
                            premier_Board.display_board()
                            premier_Board.fenetre.blit(premier_Board.floor, macgyver.position)
                            macgyver.position = macgyver.position.move(-(int(premier_Board.x / 15)), 0)
                            premier_Board.fenetre.blit(macgyver.content, macgyver.position)
                            pygame.display.flip()
                            premier_Board.pickup_object(macgyver, premier_Board.all_object)
                        
                    elif event.key == K_RIGHT:
                        if premier_Board.board[macgyver.line][macgyver.column+1] == "#":
                            print("Ouch, you just hit a wall.Try again.")
                        elif premier_Board.board[macgyver.line][macgyver.column+1] == premier_Board.board[premier_Board.end_position["line"]][premier_Board.end_position["column"]]:
                            macgyver.column +=1
                            if premier_Board.check_character_bag(macgyver):
                                premier_Board.fenetre.blit(premier_Board.floor, macgyver.position)
                                macgyver.position = macgyver.position.move(0, int(premier_Board.y / 15))
                                premier_Board.fenetre.blit(macgyver.content, macgyver.position)
                                pygame.display.flip()
                                print("Houra, you won you hardcore gamer!")
                        else:
                            macgyver.column +=1
                            premier_Board.board[macgyver.line][macgyver.column] = "M"
                            premier_Board.board[macgyver.line][macgyver.column-1] = " "
                            premier_Board.display_board()
                            premier_Board.fenetre.blit(premier_Board.floor, macgyver.position)
                            macgyver.position = macgyver.position.move((int(premier_Board.x / 15)), 0)
                            premier_Board.fenetre.blit(macgyver.content, macgyver.position)
                            pygame.display.flip()
                            premier_Board.pickup_object(macgyver, premier_Board.all_object)
                        
                    
                            

