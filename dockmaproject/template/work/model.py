import sys
import glob

def model(pid, cid):
	try:
		files = glob.glob('hot/{}_{}/score_*.txt'.format(pid, cid))
		scores = [ float(open(file).read().strip()) for file in files ]
		index = scores.index(min(scores))
		return files[index].replace('score','model').replace('txt','pdbqt')
	except:
		return 'hot/{}_{}/?.pdbqt'.format(pid,cid)


for line in sys.stdin:
	pid, cid, mark = line.strip('\n').split('\t')

	print( model(pid,cid) )
