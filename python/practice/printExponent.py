# This program prints the powers of the given number x times.
# For example, if the given number is 3 and x is 4, then the program will print:
# 0 = 1
# 3 = 3
# 3 x 3 = 9
# 3 x 3 x 3 = 27

def pow(i, n): # i -> integer, n -> the power, x^0 = 1
	total = 1
	for x in range(n):
		total = total * i
	return total


def printLetter(i, n):
	result = ''
	for x in range(n):
		if x == n-1: # Last element(val) 
			result = result + f'{i}'
		else:
			result = result + f'{i} × '

	if not result:
		result = '0'
		
	return result


def printPow(i, n):
	for index in range(n):
		letter = printLetter(i, index)
		val = pow(i, index)

		print(f'{letter} = {val}')

print("Printing powers of the given n:")
printPow(3, 5)