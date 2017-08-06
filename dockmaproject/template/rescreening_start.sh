sh pair_zero.sh | awk '{printf "rm -rf hot/%s_%s/*\n", $1,$2}' | awk '{system($0)}'
sh pair.sh > hot/pair.txt
python screening_start.py
