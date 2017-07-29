import sys
from convexhull import ConvexHull

def read_data():
	point = []
	for line in sys.stdin:
		x,y,z = [float(v) for v in line.strip('\n').split('\t')]
		point.append((x,y,z))

	return point

print( ConvexHull(read_data()).data() )
