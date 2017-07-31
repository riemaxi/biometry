import sys
from parameter import *
from pair_selection import select

ligands = open(ligand_id_path).read().strip('\n').split('\n')

for pid in sys.stdin:
	pid = pid.strip('\n')
	[print(pid, cid, sep = '\t') for cid in ligands if select(pid,cid)]
