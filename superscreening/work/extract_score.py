import sys
import re

def score(data):
	data = [s for s in data if re.match('^[0-9]',s) != None]
	return min([float((re.split('\s+',v))[1]) for v in data]) if len(data) else ''


dir, index = sys.argv[1:3]

data = [s.strip() for s in open('{}/report_{}.txt'.format(dir, index)).read().split('\n')]

open('{}/score_{}.txt'.format(dir, index),'w').write('{}'.format(score(data)))
