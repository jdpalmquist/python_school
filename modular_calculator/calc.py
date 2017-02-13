num1 = 0.0
num2 = 0.0
op = 0

def print_welcome():
	print('WELCOME TO THE MODULAR PYTHON CALCULATOR!')

def get_numbers():
	ok1 = True
	ok2 = True
	while ok1:
		try:
			num1 = float(input('Number 1: '))
			ok1 = False
		except ValueError:
			print("That is not a number! Try Again! Error: " + ValueError)

	while ok2:
		try:
			num2 = float(input('Number 2: '))
			ok2 = False
		except ValueError:
			print("That is not a number! Try Again! Error: " + ValueError)

	return (num1, num2)

def get_operation():
	run = True
	while(run):
		print("Please choose which math operation to perform:")
		print("1.) Add")
		print("2.) Subtract")
		print("3.) Multiply")
		print("4.) Divide")
		print("5.) Modulus")
		op = int(input("Choice: "))
		if op >= 1 and op <= 5:
			run = False
		else:
			print("Please make a choice between 1-5! ")

	return op


def add(x,y):
	return x+y

def sub(x,y):
	return x-y

def mul(x,y):
	return x*y

def div(x,y):
	return x/y

def mod(x,y):
	return x%y


	