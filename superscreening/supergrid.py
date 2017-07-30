# the dimensions are in Ansgtroms

class SuperGrid():
	def __init__(self, a,b, size = 28):
		self.size = size
		self.minx = a[0]
		self.maxx = b[0]

		self.miny =  a[1]
		self.maxy = b[1]

		self.minz = a[2]
		self.maxz = b[2]

		self.hsize = min(min(self.size, self.maxx - self.minx), self.maxy - self.miny)
		self.vsize = min(self.size, self.maxz - self.minz)


	def range(self, start, stop, step):
		while start < stop:
			yield start
			start += step

	def foreach(self, sink):

		steph = min(self.hsize,self.size)/2
		stepz = min(self.vsize,self.size)/2

		index = 0		
		for z in self.range(self.minz + stepz, self.maxz, 2*stepz):
			for x in self.range(self.minx + steph, self.maxx, 2*steph):
				for y in self.range(self.miny + steph, self.maxy, 2*steph):
					sink( index, (x,y,z) )
					index += 1
		
