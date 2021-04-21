import os
import time
import sys


time.sleep(2)

print("Child:", os.getpid())
print("Child's Parent:", os.getppid())
sys.exit(2)