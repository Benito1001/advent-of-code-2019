import os
os.system("stty -icanon min 1 time 0")
import sys

val = sys.stdin.read(3)
print("\n", val)
