from iscreening import IScreening
from parameter import *
import time

screening = IScreening(
	root,
	user, 
	project, 
	pair, 
	payload, 
	runnies,
	grid_mesh_size)

screening.start()
print('super screening ...')
screening.join()
