cat data/receptor.txt | awk '{printf "sh install.sh %s\n", $1}' | awk '{print $0; system($0)}'
