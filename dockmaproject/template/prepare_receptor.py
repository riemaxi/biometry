import sys
import os

id = sys.argv[1]

if not os.path.exists('{}/{}.pdbqt'.format('data',id)):
	os.system('prepare_receptor4.py -r {0}/{1}.pdb -o {0}/{1}.pdbqt'.format('data', id))

