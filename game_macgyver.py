"""
import all the class and use them to create and launch the game with the
help of the class LaunchGame
"""
import Board as bo
import Object as ob
import Character as ch
import LaunchGame as lg

if __name__ == "__main__":
    A = lg.LaunchGame(bo.Board, ch.Character, ob.Object)
