import os
import sys
from pair_selection import select_ready
from parameter import maxscore
import glob

def readscore(pid, cid, maxscore):
	try:
		files = glob.glob('hot/{}_{}/score_*.txt'.format(pid, cid))
		return min([ float(open(file).read().strip()) for file in files ])
	except:
		return maxscore + 1

for line in sys.stdin:
	pid, cid, mark = line.strip('\n').split('\t')
	score = abs(readscore(pid,cid, maxscore))

	if mark == '!' and score == 0.0:
		print(pid, cid , sep = '\t')
