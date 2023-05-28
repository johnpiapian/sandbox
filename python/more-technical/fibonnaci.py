
number = input("Enter the number: ")
number = int(number)

# def fibo(n):
# 	if n == 0 or n == 1:
# 		return 1
# 	else:
# 		return n + fibo(n-1)


# Fibonacci Series using Dynamic Programming  
def f(n):  
      
    # Taking 1st two fibonacci nubers as 0 and 1  
    FibArray = [0, 1]  
      
    # set the array size to n(and set each elemet to 0)
    while len(FibArray) < n + 1:  
        FibArray.append(0) 
      
    if n <= 1:  
        return n  
    else:  
        if FibArray[n - 1] == 0:  
            FibArray[n - 1] = f(n - 1)  
  
        if FibArray[n - 2] == 0:  
            FibArray[n - 2] = f(n - 2)  
              
    FibArray[n] = FibArray[n - 2] + FibArray[n - 1]  
    return FibArray[n]  

for i in range(number):
	print(f(i))
