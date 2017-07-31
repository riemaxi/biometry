from parameter import *
import sys
import os

id = sys.argv[1]

if not os.path.exists('{}/data/{}.pdbqt'.format(root,id)):
	os.system('prepare_ligand4.py -l {0}/data/{1}.pdb -o {0}/data/{1}.pdbqt'.format(root, id))


