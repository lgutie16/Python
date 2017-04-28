infile = open('testformat.txt', 'r')

for line in infile:
	newline = ''.join([i for i in line if not i=='"'])[:-1]
	print newline
	print ''.join([i for i in newline if not i=='\t'])[:-1]

infile.close()