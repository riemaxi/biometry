import sys
import os

dir = sys.argv[1]

os.chdir(dir)
os.system('sh setup.sh')
os.system('sh screening_start.sh')
