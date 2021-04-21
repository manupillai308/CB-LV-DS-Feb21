import sys
import os

def get_listdir(dirname):
    t = []

    for e in os.listdir(dirname):
        p = os.path.join(dirname, e)
        t.append(p)

    return t

def printsTree(dirname, prefix):
    # for e in get_listdir(dirname):
    for e in os.listdir(dirname):
        
        print(prefix, e) # if i could know that e is a folder then
        
        if os.path.isdir(os.path.join(dirname, e)):
        
            printsTree(os.path.join(dirname, e), prefix+"\t")

dirname = sys.argv[1]

printsTree(dirname, "")
