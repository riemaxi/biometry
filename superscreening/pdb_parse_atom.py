import sys

for line in sys.stdin:
	line = line.strip('\n')
	print(line[30:38], line[39:46],line[47:54], sep = '\t')
