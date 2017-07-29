#!/bin/bash -l

#SBATCH -t 10:00:00
#SBATCH --qos=high-throughput
#SBATCH -o hot/PID_CID/output.txt

# run
python prepare_receptor.py PID
python prepare_ligand.py CID
sh prepare_config.sh PID CID INDEX CENTER_X CENTER_Y CENTER_Z

python docking.py PID CID INDEX

python extract_score.py hot/PID_CID INDEX

rm task/PROJECT_PID_CID_INDEX_docking.sbatch
