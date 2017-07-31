#!/bin/bash -l

#SBATCH -t 10:00:00
#SBATCH --qos=high-throughput
#SBATCH -o hot/PID_CID/output.txt

# run
python prepare_receptor.py PID
python prepare_ligand.py CID
sh prepare_config.sh PID CID INDEX CENTER_X CENTER_Y CENTER_Z

date +%H_%M | awk '{printf "touch hot/PID_CID/time_INDEX_%s\n", $0}' | awk '{system($0)}'

python docking.py PID CID INDEX

date +%H_%M | awk '{printf "touch hot/PID_CID/time_INDEX_%s\n", $0}' | awk '{system($0)}'

python extract_score.py hot/PID_CID INDEX

rm task/PROJECT_PID_CID_INDEX_docking.sbatch
