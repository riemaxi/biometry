import sys
import os

name = sys.argv[1]

if not os.path.isdir(name):
	os.system('mkdir {}'.format(name))

os.system('cp -R template/* {}'.format(name))

parameter = open('{}/parameter.py'.format(name) ).read()

parameter = parameter.replace('__PROJECT__', name)

open('{}/parameter.py'.format(name),'w' ).write(parameter)

