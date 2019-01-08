import argparse

def fib(n) :
	a,b = 0,1
	for i in range(n):
		a,b = b,a+1

	return(a)

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("num", help = "Fibonacci number you wish to calculate. ", type = int)

	args = parser.parse_args()

	result = fib(args.num)

	print("The ", str(args.num), "the Fibonacci number is ", str(result))


if __name__ == '__main__' :
	main()

