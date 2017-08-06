#!/bin/bash -l

#SBATCH -t 10:00:00
#SBATCH --qos=high-throughput
#SBATCH -o log/heatmatrix_output.txt

# run
sh heatmatrix.sh
