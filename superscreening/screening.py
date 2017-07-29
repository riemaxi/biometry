from daemon import Daemon
import time
import os
import re
from supergrid import SuperGrid
from convexhull import ConvexHull

from signal import SIGTERM

class Screening(Daemon):
	def __init__(self, 
			root,
			user,
			project,
			pair,
			payload = 50,
			runnies = 10,
			hold_time = 5):
		Daemon.__init__(
				self, 
				pidfile = 'log/process.pid', 
				root = root,
				stdout = 'log/stdout.txt',
				stderr = 'log/stderr.txt')

		self.pair = pair
		self.user = user
		self.project = project
		self.payload = payload
		self.runnies = runnies
		self.hold_time = hold_time

		self.template = open('template/task_docking.sbatch').read()
		self.index = 1

	def jCount(self, state = 'R'):
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
		task =  self.template.replace('PID', pid).replace('CID',cid).replace('INDEX',i)
		task = task.replace('CENTER_X', center[0]).replace('CENTER_Y', center[1]).replace('CENTER_Z', center[2])
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

	def xyz(self, pdb):
		data = []
		for line in open(pdb):
			line = line.strip('\n')
			if line.startswith('ATOM'):
				data.append( (float(line[30:38]), float(line[39:46]),float(line[47:54])) )
		return data

	def supergrid(self, pid, sink):
		hull = ConvexHull(self.xyz('data/{}.pdb'.format(pid))
		SuperGrid(hull.data(), hull.minz(), hull.maxz()).foreach( lambda i, center : sink(i, center) )

	def run(self):
		for line in open(self.pair):
			pid, cid = line.strip('\n').split('\t')
			self.supergrid(
				pid,
				lambda i, center: self.process(pid, cid, i, center)
			)

		os.system('sbatch heatmatrix.sbatch'


	def kill(self):
		try:
			id = int(open(self.pidfile).read().strip('\n'))
			os.system('rm -f ' + self.pidfile)

			os.kill(id, SIGTERM)
		except OSError as e:
			pass


