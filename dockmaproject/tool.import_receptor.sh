cat data/receptor.txt | python tool.bridge.py $1 | awk '{printf "cp %s %s\n",$1,$2}' | awk '{print $0; system($0)}'
