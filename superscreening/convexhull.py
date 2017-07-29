class ConvexHull():
	def __init__(self,point):
		self.point = point

	def orientation(self, p, q, r):
		val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
 
		if val == 0:
			 return 0  #colinear

		return 1 if val > 0 else 2 # clock or counterclock wise

	def minx(self):
		return min([v[0] for v in self.point])

	def minz(self):
		return min([v[2] for v in self.point])

	def maxz(self):
		return max([v[2] for v in self.point])

	def data(self):
		if len(self.point)<3:
			return [(v[0],v[1],self.z) for v in self.point]

		hull = []
		minx = self.minx()
		n = len(self.point)
		p = 1
		while True:
			pnt = self.point[p]
			hull.append((pnt[0],pnt[1]))
			q = (p + 1) % n
			for i in range(n):
				if self.orientation(pnt, self.point[i], self.point[q]) == 2:
					q == i
			p = q

			if p == 1:
				break;

		return hull
