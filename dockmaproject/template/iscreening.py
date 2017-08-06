import time
import os
import re
from supergrid import SuperGrid
from threading import Thread

class IScreening(Thread):
	def __init__(self, 
			root,
			user,
			project,
			pair,
			payload = 50,
			runnies = 10,
			grid_mesh_size = 28,
			hold_time = 5):
		Thread.__init__(self)

		self.pair = pair
		self.user = user
		self.project = project
		self.payload = payload
		self.runnies = runnies
		self.hold_time = hold_time
		self.grid_mesh_size = grid_mesh_size

		self.template = open('template/task_docking.sbatch').read()
		self.index = 1

	def jCount(self, state = 'R,PD'):
		statsfile = 'log/stats.txt'
		os.system("squeue -t {} -u {} --Format=name | grep -e '{}_' | wc > {}".format(state, self.user, self.project, statsfile))
		tpl = open(statsfile).read().strip()
		tpl = re.split('\s+',tpl)

		return int(tpl[0])

	def hold(self):
		jc = self.jCount()
		while jc > self.runnies:
			print('holding ... {} runnies'.format(jc))
			time.sleep(self.hold_time)
			jc = self.jCount()

	def exists_score(self, path):
		try:
			content = open(path).read().strip()
			print(content)
			return len(content) > 0 and content != '1.0'
		except:
			return False

	def create_task(self, pid, cid, i, center):
		task =  self.template.replace('PID', pid).replace('CID',cid).replace('INDEX',str(i))
		task = task.replace('CENTER_X', str(center[0])).replace('CENTER_Y', str(center[1])).replace('CENTER_Z', str(center[2]))
		task = task.replace('PROJECT', self.project)

		path = 'task/{}_{}_{}_{}_docking.sbatch'.format(self.project, pid, cid, i)

		return task, path



	def process(self, pid, cid, i, center):
		if self.index % self.payload == 0:
			self.hold()

		dir = 'hot/{}_{}'.format(pid, cid)
		if not os.path.isdir(dir):
			os.system('mkdir {}'.format(dir))

		score_path = dir + '/score_{}.txt'.format(i)
		if not self.exists_score( score_path ):
			open( score_path,'w').write('1.0')

			task, path = self.create_task(pid, cid, i, center)

			open(path,'w').write(task)

			os.system('sbatch ' + path )

			self.index += 1

	def box(self, pdb):
		a = (float('inf'), float('inf'), float('inf'))
		b = (float('-inf'), float('-inf'), float('-inf'))
		for line in open(pdb):
			if line.startswith('ATOM'):
				line = line.strip('\n')
				x, y, z = ( float(line[30:38]), float(line[39:46]), float(line[47:54]) )

				a = (min(a[0],x), min(a[1], y), min(a[2], z))
				b = (max(b[0],x), max(b[1], y), max(b[2], z))

		return a,b

	def supergrid(self, pid, sink):
		a, b = self.box( 'data/{}.pdb'.format(pid) )
		SuperGrid( a, b, self.grid_mesh_size ).foreach( lambda i, center : sink(i, center) )

	def run(self):
		for line in open(self.pair):
			pid, cid = line.strip('\n').split('\t')
			self.supergrid(
				pid,
				lambda i, center: self.process(pid, cid, i, center)
			)
