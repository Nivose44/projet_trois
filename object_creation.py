
"""
class object créant les objets ainsi que les fonctions définissant leur position
et les placant dans le tableau
"""
import random

class Object():
    def __init__(self, contenu):
        #améliroer le code pour que board_object ne soit pas utilisé en variable globale
        self.line = 0
        self.column = 0
        self.contenu = contenu
        

    def position_object(self, board_object):
        while board_object.board[self.line][self.column] != " ":
            self.define_object_position()
        board_object.board[self.line][self.column] = self.contenu
        

    def define_object_position(self):
        self.line = random.randint(0, 14)
        self.column = random.randint(0, 14)



