import os
import sys
from pair_selection import select_ready
import glob


def reeady(pid, cid, maxscore):
	try:
		files = glob.glob('hot/{}_{}/score_*.txt'.format(pid, cid))
		readies = [1 for file in files if open(file).read().strip() != '1.0']
		return not len(readies)
	except:
		return False

for line in sys.stdin:
	pid, cid = line.strip('\n').split('\t')
	if select_ready(pid,cid) and ready(pid,cid):
		print(pid, cid,'!', sep = '\t')
	else:
		print(pid, cid,'?', sep = '\t')
