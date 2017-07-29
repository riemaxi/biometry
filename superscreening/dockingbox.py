import  sys
import re

def createbox(boxscale):
	totalcharge = 0
	center = [0.0,0.0,0.0]
	minvector = [float('inf'), float('inf'), float('inf')]
	maxvector = [float('-inf'), float('-inf'), float('-inf')]

	count = 0
	for line in sys.stdin:
		line = line.strip('\n').split('\t')
		vector = [float(v) for v in line[:3]]
		minvector = [min(vector[i],minvector[i]) for i in range(3)]
		maxvector = [max(vector[i],maxvector[i]) for i in range(3)]
		center = [center[i] + vector[i] for i in range(3)]

		count += 1

	return ((
		#box
		(maxvector[0] - minvector[0])*boxscale,
		(maxvector[1] - minvector[1])*boxscale,
		(maxvector[2] - minvector[2])*boxscale),

		#center
		(center[0]/count,
		center[1]/count,
		center[2]/count))
