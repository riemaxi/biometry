sh tool.model.sh | awk -F_ '{printf "%s/%s\n", substr($1,5),$0}' | python tool.export_model.py $1
