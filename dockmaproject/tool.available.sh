cat data/receptor.txt | awk '{if(system( "[ -d " $0 " ]") != 0) print $0}'
