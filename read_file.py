#Goal is to hav a single line program that copy's contents of one file to another.

from sys import argv
from os.path import exists #Literally a single function is imported from the os.path module

#declare input file  at the command but only initiate the output file within the program itself.
script, from_file, to_file = argv

'''When using this version of the program a new file will be created if 
	the file being used to write to does not already exists

	if the file output file does exist, this scripit will overwright the contents of that file.
	How can we add to a file???.... change the second argument in the open commmand to 'a'''
open(to_file, 'a').write(open(from_file).read())
