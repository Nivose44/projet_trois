import board_creation as bc
import object_creation as oc
import character_creation as cc

if __name__ == "__main__":
    board_object = bc.Board(15, 15)
    #creation of the board
    aiguille = oc.Object("A")
    tube = oc.Object("T")
    ether = oc.Object("E")
    #creation of the three objects
    aiguille.position_object(board_object)
    tube.position_object(board_object)
    ether.position_object(board_object)
    #we place the three objects randomly inside the board (ajouter set)
    macgyver = cc.Character("M", board_object)
    macgyver.movement(aiguille, tube, ether)
    
