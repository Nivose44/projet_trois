"""
Class Character"""
class Character():
    """create the character with his attributes.It can be a hero or a guardian"""
    def __init__(self, contenu):
        self.line = 0
        self.column = 0
        self.contenu = contenu
        self.bag = 0
