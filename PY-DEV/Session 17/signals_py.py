import signal, sys, os

def handler(signum, frame):
    print("CTRL + C Pressed, exiting....")
    # sys.exit(-1)
    os._exit(1)

signal.signal(signal.SIGINT, handler)


try:
    while True:
        pass
except :
    print("Sys exit called")
