"""
class Obj
"""
import pygame
class Obj():
    """
    Create the object that will be placed on the board.
    The character will contain is position and the visual representation
    of himself that will be displayed on teh board.
    """
    def __init__(self, content, name):
        self.line = 0
        self.column = 0
        self.name = name
        self.content = pygame.image.load(content).convert()
        self.content.set_colorkey((255, 255, 255))
