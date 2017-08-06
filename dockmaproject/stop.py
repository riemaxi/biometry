import sys
import os

dir = sys.argv[1]

os.chdir(dir)
os.system('python screening_stop.py')
