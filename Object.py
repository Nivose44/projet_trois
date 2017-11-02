"""
Class object
"""
class Object():
    """
The class Object create an object to place in the board that will be picked up
by macgyver.
The argument content contain a string that will represent the object in the
board
    """
    def __init__(self, content):
        """ initialize the values of the object when we create it"""
        self.line = 0
        self.column = 0
        self.content = str(content)
