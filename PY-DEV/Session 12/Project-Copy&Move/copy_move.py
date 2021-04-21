import sys
import os


def copy_and_move(fro, to, move=False):
    for e in os.listdir(fro):
        if os.path.isdir(os.path.join(fro, e)):
            if not os.path.exists(os.path.join(to, e)):
                os.mkdir(os.path.join(to, e))
            #delete pos 1
            copy_and_move(os.path.join(fro, e), os.path.join(to, e), move)
            #delete pos 2
            if move:
                os.rmdir(os.path.join(fro, e))
    
        else:
            data = open(os.path.join(fro, e), "rb").read()
            open(os.path.join(to, e), "wb").write(data)
            if move:
                os.remove(os.path.join(fro, e))


fro = sys.argv[1]
to = sys.argv[2]
move = None
if len(sys.argv) > 3:
    print("Moving files from", fro, "to", to, "...")
    move = sys.argv[3]
    
else:
    print("Copying files from", fro, "to", to, "...")

copy_and_move(fro, to, move == "m")


