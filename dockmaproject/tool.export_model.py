import sys
import os

dir = sys.argv[1]

for line in sys.stdin:
	source = line.strip('\n')

	path = os.path.dirname(dir + '/screening/' + '/'.join(source.split('/')[1:]))
	if not os.path.exists(path):
		os.makedirs(path)

	if os.path.exists(source):
		print('cp {} {}/model.pdbqt'.format(source, path))
		os.system('cp {} {}/model.pdbqt'.format(source, path))
