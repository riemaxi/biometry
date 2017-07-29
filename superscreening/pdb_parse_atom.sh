#cat $1 | grep -e '^ATOM' -e '^HETATM' | python pdb_parse_atom.py
cat $1 | grep -e '^ATOM' | python pdb_parse_atom.py
