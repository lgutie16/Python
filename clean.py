''' 
given a file directory, transform all 
the files in import to avoid special characters
'''
import re
import fileinput
import glob, os

os.chdir("filesdir")
for file in glob.glob("*.txt"):
	print(file)
	f = open(file)
	for line in f:
		cleanString = re.sub('\W+',' ', line )
		print(cleanString)