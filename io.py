#Let us pratice some more ways we can accept input from the user.
''' When we run this from the command line it is nifty that python has 
	built in error checking. If the number of arguments necessary aore not present
	then the program does not run and an error message is displayed
'''

from sys import argv	#NOTE: we don't have to import the intire library so that binaries
						#		don't become too large.

script, name = argv
prompt = '>\t'

print "Hi %s, I'm the %s script." % (name, script)
print "i'd like to ask you a few questions."
print "Do you like me %s?" % name
likes = raw_input(prompt)

print "wher do you live %s?" % name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print '''
	Alright, so you said %r about liking me .
	You live in %r. not sure where that is.
	And you have a %r computer. NICE.''' % (likes, lives, computer)


