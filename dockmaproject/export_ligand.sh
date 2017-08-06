cat data/ligand.txt | awk '{printf "cp data/%s.pdbqt ../../Toxicology/data/Ligands/pdbqt\n", $1}' | awk '{print $0; system($0)}'
