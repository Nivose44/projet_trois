"""
class Character
"""
import pygame
class Character():
    """
    Create the characte that will be place on the board.
    The character will contain is position and the visual representation
    of himself that will be displayed on teh board.
    """
    def __init__(self, content):
        self.line = 0
        self.column = 0
        self.bag = 0
        self.content = pygame.image.load(content).convert()
        self.position = self.content.get_rect()
