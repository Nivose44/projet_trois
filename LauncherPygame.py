"""
class Launcher
"""
import pygame
from pygame.locals import *
class Launcher():
    """
    Initialize pygame an create the graphic version of the game
    """
    def __init__(self, Board, Character, Obj):
        pygame.init()
        premier_Board = Board()
        macgyver = Character("images/macgyver.png")
        premier_Board.set_position_hero(macgyver)
        premier_Board.put_hero_on_board(macgyver)
        guardian = Character("images/guardian.png")
        premier_Board.set_position_guardian(guardian)
        premier_Board.put_guardian_on_board(guardian)
        aiguille = Obj("images/needle.png", "A")
        tube = Obj("images/tube.png", "T")
        ether = Obj("images/ether.png", "E")
        premier_Board.put_object_on_board(aiguille)
        premier_Board.put_object_on_board(tube)
        premier_Board.put_object_on_board(ether)
        self.launch(premier_Board, macgyver)

    def launch(self, Board, Character):
        continuer = 1
        while not Board.positioned_on_guardian(Character):
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()

                if event.type == KEYDOWN:
                    if event.key == K_DOWN:
                        Board.move(Character, Board.DOWN)

                    elif event.key == K_UP:
                        Board.move(Character, Board.UP)

                    elif event.key == K_LEFT:
                        Board.move(Character, Board.LEFT)

                    elif event.key == K_RIGHT:
                        Board.move(Character, Board.RIGHT)
