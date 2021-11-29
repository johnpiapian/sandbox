def growth(n, t, p): #n -> number, t -> times, p -> percentage
	pt = p/100.0 # for efficiency : or does it?
	if t <= 0:
		return round(n)
	else:
		return cal(n+(n*pt), t-1, p)


def pdiff(n1, n2):
	n1, n2 = float(n1), float(n2)

	# n1 + x = n2, x = n1*(a/100)
	# n1 + (n1*(a/100)) = n2
	# n1 * (a/100) = n2-n1
	# a = 100((n2-n1)/n1))	

	# result = [n1, n2, round(100.0 * ((n2/n1) - 1.0), 2)]
	result = [n1, n2, round(100.0 * ((n2-n1)/n1), 2)]

	return result


def display():
	# print(growth(10000, 10, 100)) # O(n) where n is the number of times the function is called t
	print("Going from {0[0]} to {0[1]} is an increase in {0[2]}%.\n").format(pdiff(150, 200))


display()