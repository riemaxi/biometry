import sys
from convexhull import ConvexHull
from supergrid import SuperGrid

def read_data():
	point = []
	for line in sys.stdin:
		x,y,z = [float(v) for v in line.strip('\n').split('\t')]
		point.append((x,y,z))

	return point

hull = ConvexHull(read_data())

SuperGrid(
	hull.data(), 
	hull.minz(), 
	hull.maxz()).foreach(
		lambda x,y,z: print('{:.2f}\t{:.2f}\t{:.2f}'.format(x, y, z) )
)

