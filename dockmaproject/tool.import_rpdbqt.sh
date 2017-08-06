cat data/receptor.txt | awk '{printf "cp git.toxicology/data/Proteins/pdbqt/%s.pdbqt data/\n", $1}' | awk '{print $0; system($0)}'
