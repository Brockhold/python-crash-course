#!/usr/bin/env python

def most_used(args):
	''' gives the most commonly used command in the specified .bash_history file'''
	# Open the file
	with open(args[1]) as f:
		# Using the file, create a list of a first full word from each line
		command_list={}
		for line in f:
			word = line.split(" ")[0]
			# remove newlines, as they do not distinguish commands
			if "\n" in word:
				word = word[0:-1]
			# Add the word to the list if it is not there, and increment its count
			if word not in command_list:
				command_list[word] = 0
			command_list[word]+=1
	return sorted(command_list,key=command_list.get)[-1]

# NOTE: this is an encoded solution
#       the programme will decode it automatically
#         so you can check your results against it yourself
#       it will create a function called `solution'
solution = None
exec '''
qrs fbyhgvba(svyranzr):
	pbzznaqf = {}
	jvgu bcra(svyranzr) nf s:
		sbe yvar va s:
			pbzznaq = yvar.fcyvg(' ')[0]
			vs pbzznaq abg va pbzznaqf:
				pbzznaqf[pbzznaq] = 0
			pbzznaqf[pbzznaq] += 1
	erghea znk(pbzznaqf, xrl=pbzznaqf.trg)
'''.decode('rot13') in locals(), globals()

# TODO: write some tests!

if __name__ == '__main__':
	from sys import argv
	# argv is a list of the command line parameters
	#   the 0th element is the name of the program itself
	#   the 1st... elements are the arguments passed to the program

	if len(argv) < 2:
		print 'usage {} ~/.bash_history: ' \
		      'gives the most commonly used command'.format(argv[0])
	else:
		a =  most_used(argv)
		b = solution(argv[1])
		print("Student's solution: "+str(a),"Teacher's solution: "+str(b),"Test passes? "+str(a==b))