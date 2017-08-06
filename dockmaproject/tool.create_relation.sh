cat data/receptor.txt | awk '{if(system( "[ -d " $0 " ]") == 0) print $0}' | awk '{printf "python tool.create_relation.py %s\n",$0}' | awk '{print($0); system($0)}'
