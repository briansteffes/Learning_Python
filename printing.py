#	These are examples typed exactly from 'Learn Python the hard Way 3rd Edition

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug\nSep\nOct\nNov\nDec"

#automatically reads the spaces as a 'natural' delimiter.
#technically: string
#treated as: array of string constants
#This negates the need for very simple for loops

print "here are the days: ", days
print "Here are the months:\n", months


'''Because this is a loosley yped language I cannot declare related variables all in one grouping
		as I would in C then assign values read from stdin as the program progresses.
		i.e:  int age, heigh, weight, birth_day;
'''

age = raw_input("Please enter your age: \n")
day = raw_input("Please enter the day of the month you were born: \n")
month = raw_input("Please enter the month you were born: \n")
year = raw_input("Please enter the year you were born\n")


print ("\n"*3) + "So were born on %s %d, %d, making you %d years old!" %(month, int(day), int(year) ,int(age))



