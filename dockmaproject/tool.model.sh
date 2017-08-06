cat data/receptor.txt | shuf -n 50 | awk '{printf "python tool.model.py %s\n", $0}' | awk '{system($0)}' | grep -ve '?' 
