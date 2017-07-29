cat $1 | grep -e '^ATOM' -e '^HETATM' | python xyz.py
