import sys
from parameter import maxscore
import glob

def real(r):
	return r if r!=0.0 else abs(r)

def readscore(pid, cid, maxscore):
	try:
		files = glob.glob('hot/{}_{}/score_*.txt'.format(pid, cid))
		return min([ float(open(file).read().strip()) for file in files ])
	except:
		return maxscore + 1

for line in sys.stdin:
	pid, cid = line.strip('\n').split('\t')

	print('{}\t{}\t{:.2f}'.format(pid, cid, real( readscore(pid,cid,maxscore))) )

