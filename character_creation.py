"""
class pour créer les objets, class hérité pour créer macgyver et le faire se mouvoir
"""
class Character():
    def __init__(self, contenu, board_object):
        self.line = board_object.position_depart["line"]
        self.column = board_object.position_depart["column"]
        self.contenu = contenu
        self.bag = 0
        self.bo = board_object
        board_object.board[self.line][self.column] = self.contenu
        
    def pickup(self, aiguille, tube, ether):
        #fonction qui ramasse et gére les objets quand macgyver passe dessus
        if self.bo.board[self.line][self.column] == self.bo.board[aiguille.line][aiguille.column]:
            aiguille.line = 0
            aiguille.column = 0
            self.bag += 1
            print("objet(s) ramassé(s): ", self.bag)
            
        elif self.bo.board[self.line][self.column] == self.bo.board[tube.line][tube.column]:
            tube.line = 0
            tube.column = 0
            self.bag += 1
            print("objet(s) ramassé(s): ", self.bag)
            
        elif self.bo.board[self.line][self.column] == self.bo.board[ether.line][ether.column]:
            ether.line = 0
            ether.column = 0
            self.bag += 1
            print("objet(s) ramassé(s): ", self.bag)
            
            
    def movement(self, aiguille, tube, ether):
        print(self.bo.board)
        while self.bo.board[self.line][self.column] != self.bo.board[self.bo.position_arrivee["line"]][self.bo.position_arrivee["column"]]:
            move = input("Appuyez sur q(gauche), s(bas), d(droite) ou z(haut) pour vous déplacer:")
            if move == "q":
                self.column -= 1
                if self.bo.board[self.line][self.column] == "#":
                    self.column += 1
                    print("Ouch, you just hit a wall.Try again.")
                else:
                    self.bo.board[self.line][self.column] = self.contenu
                    self.bo.board[self.line][self.column+1] = " "
                    print(self.bo.board)
                    self.pickup(aiguille, tube, ether)
                    
            elif move == "s":
                self.line += 1
                if self.bo.board[self.line][self.column] == "#":
                    self.line -= 1
                    print("Ouch, you just hit a wall.Try again.")
                elif self.bo.board[self.line][self.column] == self.bo.board[self.bo.position_arrivee["line"]][self.bo.position_arrivee["column"]] and self.bag != 3:
                    print("vous avez perdu idiot, il fallait tous les ramasser")
                else:
                    self.bo.board[self.line][self.column] = self.contenu
                    self.bo.board[self.line-1][self.column] = " "
                    print(self.bo.board)
                    self.pickup(aiguille, tube, ether)
                    
            elif move == "d":
                self.column += 1
                if self.bo.board[self.line][self.column] == "#":
                    self.column -= 1
                    print("Ouch, you just hit a wall.Try again.")
                else:
                    self.bo.board[self.line][self.column] = self.contenu
                    self.bo.board[self.line][self.column-1] = " "
                    print(self.bo.board)
                    self.pickup(aiguille, tube, ether)
                    
            elif move == "z":
                self.line -= 1
                if self.bo.board[self.line][self.column] == "#":
                    self.line += 1
                    print("Ouch, you just hit a wall.Try again.")
                else:
                    self.bo.board[self.line][self.column] = self.contenu
                    self.bo.board[self.line+1][self.column] = " "
                    print(self.bo.board)
                    self.pickup(aiguille, tube, ether)
                    
            else:
                print("Vous avez gagné!Non je rigole petit malin, utilise donc les touches indiquées")



    
                
                



