#Let us pratice some more ways we can accept input from the user.

from sys import argv	#NOTE: we don't have to import the intire library so that binaries
						#		don't become too large.

script, first, second, third = argv

print "The script is called: ", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is", third