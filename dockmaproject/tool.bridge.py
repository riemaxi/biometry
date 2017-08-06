import sys
import glob

def bridge(paths, pid):
	names = [path.split('/')[-1].replace('.pdb','').upper() for path in paths]
	try:
		index = names.index(pid)
		print(paths[index], 'data/{}.pdb'.format(pid), sep = '\t')
	except:
		pass	

path = sys.argv[1]
paths = glob.glob('{}/*.pdb'.format(path))

for pid in sys.stdin:
	pid = pid.strip('\n')
	bridge(paths, pid)	
