# 

run = True

while run:
	print("Welcome to the simple python calculator!")
	print(" ")
	number1 = int(input("Please enter the first number:"))
	number2 = int(input("Please enter the second number:"))

	operation = 0
	while operation <= 0:
		print("Now choose a mathematical operation to perform on them: ")
		print("1 - Add")
		print("2 - Subtract")
		print("3 - Multiply")
		print("4 - Divide")
		operation = int(input("Choice (1-4): "))
		if operation >= 1 or operation <= 4:
			if operation == 1:
				print(number1, "+", number2, "=", str(number1 + number2))
			elif operation == 2:
				print(number1, "-", number2, "=", str(number1 - number2))
			elif operation == 3:
				print(number1, "x", number2, "=", str(number1 * number2))
			elif operation == 4:
				if number2 != 0:
					print(number1, "/", number2, "=", str(number1 / number2))
				else:
					print("Divide by Zero error!")

		else:
			print("Invalid choice, try again!")


	keep_going = input("Would you like to do another calculation? (y/n):")
	if keep_going != 'y' and keep_going != 'Y':
		run = False
