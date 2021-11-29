
import math, random

def pop(x):
	return round(math.sqrt(x**x + x**x))

def rand(start,end):
	return random.randrange(start,end)


matched = False
tried = 0

while matched == False:
	if(rand(0,500) == rand(0,500)):
		matched = True
		print('successful')
	else:
		tried += 1
		print(tried)