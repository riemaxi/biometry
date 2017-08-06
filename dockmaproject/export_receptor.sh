cat data/receptor.txt | awk '{printf "cp data/%s.pdbqt ../../Toxicology/data/Proteins/pdbqt\n", $1}' | awk '{print $0; system($0)}'
