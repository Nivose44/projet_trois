"""
that algorythm will take the informations contained inside board.py and divide
them equally among the lists of the two dimensionnal list list_board.
You can easily change the number of items by list by changing the modulo divider
of j: if the modulo is set to 5 (j%5 == 0), each list of list_board will contain
5 items if the number of item in board.py is big enough
"""
#créer appel exception si les de board_size ne créent pas un board assez grand
class Board():
    def __init__(self, height_board, lenght_board):
        with open("board.py", "r") as file:
            file = [i.replace('\n', '') for i in file]
            self.board = [[] for k in range(height_board)]
            #comprendre ce code
            self.objets = []
            i = 0
            j = 0
            for numbers in file:
                for number in numbers:
                    if int(number) == 0:
                        self.board[i].append("#")
                    elif int(number) == 1:
                        self.board[i].append(" ")
                    elif int(number) == 3:
                        self.board[i].append(number)
                        self.position_depart = {"line":i, "column":self.board[i].index("3")}
                    elif int(number) == 4:
                        self.board[i].append(number)
                        self.position_arrivee = {"line":i, "column":self.board[i].index("4")}
                    j += 1
                    if j%lenght_board == 0:
                        i += 1
