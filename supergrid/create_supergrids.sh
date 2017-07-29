cat 671x10/data/receptor.txt | awk '{printf "sh create_supergrid.sh 671x10/data/%s.pdb\n", $0}' | awk '{printf "%s\n",$0; system($0)}'
