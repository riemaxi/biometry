import os
import sys

pid, cid, index = sys.argv[1:4]

os.system('vina --out hot/{0}_{1}/model_{2}.pdbqt --log hot/{0}_{1}/report_{2}.txt --receptor data/{0}.pdbqt --ligand data/{1}.pdbqt --config hot/{0}_{1}/config_{2}.txt'.format(pid,cid,index))
