# randint is used to gurantee integer numbers for line numbers
from random import randint


def print_random_lines(file_name, file_num_lines):
	# create a list of 20 random number
	rand_lines = [randint(1,file_num_lines) for i in range(20)]


	with open(file_name,'r') as f:
		for k,v in enumerate(f):
			if k in rand_lines:
				# the [:-1] is to ensure new line is not included
				print(v[:-1])


# file name and number of lines given
file_name = './sample.csv'
file_num_lines = 1000

# calling the function
print_random_lines(file_name,file_num_lines)

