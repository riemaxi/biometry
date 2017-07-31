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

def readtimes(pid,cid):
	try:
		files = glob.glob('hot/{}_{}/score_*.txt'.format(pid, cid))
		scores = [ float(open(file).read().strip()) for file in files ]
		index = scores.index(min(scores))
		times = glob.glob('hot/{}_{}/time_{}_*'.format(pid,cid,index))
		
		return '\t'.join([':'.join(time.split('_')[3:]) for time in times])
			
	except:
		return 'xx:xx\txx:xx'

for line in sys.stdin:
	pid, cid = line.strip('\n').split('\t')

	print( '{}\t{}\t{:.2f}\t{}'.format( pid, cid, real( readscore( pid,cid,maxscore ) ), readtimes( pid,cid ) ) )

