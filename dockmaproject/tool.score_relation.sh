sh tool.create_relation.sh
sh tool.relation.sh | awk '{printf "%s\t%s\t%s\n",$1,$2,$3}' > relation.txt

mv relation.txt git.toxicology/results/reloaded/
