def fib_usual(n):
	if n == 1:
		return 1
	elif n == 2:
		return 2
	else :
		return fib_usual(n-1) + fib_usual(n-2)

fibDict = {1:1, 2:2}    #Providing the base case to dictionary
def fib_efficient(fibDict, n):
	if n in fibDict:
		return fibDict[n]

	else:
		ans =  fib_efficient[fibDict, n-1] + fib_efficient[fibDict, n-2]
		fibDict[n] = ans
		return ans

