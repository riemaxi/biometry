import sys
import os

dir = sys.argv[1]

os.chdir(dir)
os.system('sh relation.sh > report/relation.txt')
