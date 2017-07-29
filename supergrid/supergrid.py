# the dimensions are in Ansgtroms

class SuperGrid():
	def __init__(self, data, minz, maxz, size = 28):
		self.data = data
		self.size = size
		self.minz = minz
		self.maxz = maxz
		self.minx = min([p[0] for p in data])
		self.maxx = max([p[0] for p in data])
		self.miny =  min([p[1] for p in data])
		self.maxy = max([p[1] for p in data])
		self.hsize = min(min(self.size, self.maxx - self.minx), self.maxy - self.miny)
		self.vsize = min(self.size, self.maxz - self.minz)


	def range(self, start, stop, step):
		while start < stop:
			yield start
			start += step

	def foreach(self, sink):

		steph = min(self.hsize,self.size)/2
		stepz = min(self.vsize,self.size)/2
		
		for z in self.range(self.minz + stepz, self.maxz, stepz):
			for x in self.range(self.minx + steph, self.maxx, steph):
				for y in self.range(self.miny + steph, self.maxy, steph):
					sink(x,y,z)
		
