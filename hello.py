"""Notes about syntax:
		*	automatically includes a new line character '\n'
		*	parenthesis unecessary to use the print function
		*	libraries are already accessible to the compiler w/ out a specific 'include <...>'
		*	Return key 'Enter' signifies end of use of the function.
				- No need for end of line character ';'
				- How would I be able to span the contents of a funciton across multiple lines?

				You need to explicitly change the default newline character to a space or a tab.
"""

x = "There are %d types of people." %10
binary = "binary"
do_not = "don't"
z = "Thos who know %s know that there is no such thing aas a %s world view" %(x,binary)


print z


#You can even includ variables in the string and assign what that variable points to in
#a separate function declaration using that string. (in this case the print function)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
print joke_evaluation%hilarious

main_word = 'Ashes'
part_1 = "%s" %main_word
part_2 = "to ashes and"

print "Ring around the rosy"
print "Pocket full of posy"
print part_1,					#We can use the comma to replace '\n' w/ ' '
print part_2

print 'we all fall down'

print "*" * 25
user_name = "\tbrian.steffes\n"
print user_name * 10
















