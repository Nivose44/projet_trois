"""game_macgyver will launch the game"""
import argparse
import BoardPygame as bp
import Board as bo
import ObjPygame as op
import Obj as ob
import CharacterPygame as cp
import Character as ch
import LauncherPygame as lp
import Launcher as lg

def parse_arguments():
    #create an option to decide wich version of the game to use
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--extension", help="""launch  text or pygame version""")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    if args.extension == "text":
        A = lg.Launcher(bo.Board, ch.Character, ob.Obj)
    elif args.extension == "pygame":
        A = lp.Launcher(bp.Board, cp.Character, op.Obj)
