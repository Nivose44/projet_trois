"""
import all the class and use them to create and launch the game with the
help of the class LaunchGame
"""
import Board as bo
import Obj as ob
import Character as ch
import Launcher as lg

if __name__ == "__main__":
    A = lg.Launcher(bo.Board, ch.Character, ob.Obj)
