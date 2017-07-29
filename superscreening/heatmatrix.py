import sys
from parameter import maxscore
import re
import glob

def real(r):
	return r if r != 0.0 else abs(r)

def readscore(pid, cid, maxscore):
	try:
		files = glob.glob('hot/{}_{}/score_*.txt'.format(pid, cid))
		return min([ float(open(file).read().strip()) for file in files ])
	except:
		return maxscore + 1


rel = {}
rows = []
columns = []
minscore = float('inf')
for line in sys.stdin:
	pid, cid  = line.strip('\n').split('\t')

	if not cid in  rows:
		rows.append(cid)

	if not pid in  columns:
		columns.append(pid)

	score = readscore(pid, cid, float(maxscore))
	minscore = min(score, minscore)

	rel['{}_{}'.format(cid, pid)] = score

rows = sorted(rows)
columns = sorted(columns)

print(minscore, maxscore , sep = '\t')
print('\t' + '\t'.join(columns))

for cid in rows:
	row = ['{:.2f}'.format(real(rel['{}_{}'.format(cid,pid)])) for pid in columns]
	print('{}\t{}'.format(cid, '\t'.join(row)))

