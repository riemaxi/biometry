from signal import SIGTERM
import os
from screening_stop_after import clean

pid = 'log/process.pid'

try:
	id = int(open(pid).read().strip('\n'))
	os.kill(id, SIGTERM)
except OSError as e:
	pass

clean()
