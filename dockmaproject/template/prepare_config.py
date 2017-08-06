import sys
from parameter import *

pid,cid,index,x,y,z = sys.argv[1:7]

config = open('template/config.txt').read()

config = config.replace('__EXHAUSTIVENESS__', str(exhaustiveness))

config = config.replace('__CENTER_X__', x)
config = config.replace('__CENTER_Y__', y)
config = config.replace('__CENTER_Z__', z)

open('hot/{}_{}/config_{}.txt'.format(pid, cid, index),'w').write(config)
