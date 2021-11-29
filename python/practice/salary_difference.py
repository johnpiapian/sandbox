	
#The difference of two numbers in percentage; assuming 2nd number is greater.
def percentDiff(noI,noII): 
	thediff = noII - noI
	result = thediff / (noI*0.01)
	return result

def increaseSalary():
	currentSalary = int(input("What is your current salary? \n"))
	nextSalary = int(input("What will be your next salary? \n"))

	percentage = percentDiff(currentSalary,nextSalary)
	decide = "increase" if percentage >= 0 else "decrease"
	result = "Going from ${} to ${} will give you {}% {} in salary.".format(currentSalary,nextSalary,round(abs(percentage)),decide)
	return result
	
print(increaseSalary())
