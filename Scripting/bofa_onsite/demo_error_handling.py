while True:
	try:
		x = int(input("Enter a number here :"))
		break
	except ValueError:
		print("That\'s not a valid number")
	except KeyboardInterrupt:
		print('\nNo input given\n')
		break
	finally:
		print('Attempted Input\n')
