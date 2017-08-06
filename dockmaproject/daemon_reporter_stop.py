from signal import SIGTERM
import os

pid = 'daemon_reporter.pid'

try:
	id = int(open(pid).read().strip('\n'))
	os.kill(id, SIGTERM)
except OSError as e:
	pass

os.system('rm -f ' + pid)


