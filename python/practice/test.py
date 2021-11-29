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
		# result = "0"
		result = '1'
		
	return result


def printPow(i, n):
	for index in range(n):

		letter = printLetter(i, index)
		val = pow(i, index)

		print(f'{letter} = {val}')

def fact(n):
	if n <= 1:
		return 1
	else:
		return n * fact(n-1)

printPow(7, 7)
print(fact(10))