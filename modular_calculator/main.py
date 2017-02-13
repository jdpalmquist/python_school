#!/bin/python

import calc

run = True

while run:
	calc.print_welcome()

	numbers = calc.get_numbers()

	operation = calc.get_operation()

	if operation == 1:
		print(numbers[0], " + ", numbers[1], " = ", calc.add(numbers[0], numbers[1]))

	if operation == 2:
		print(numbers[0], " - ", numbers[1], " = ", calc.sub(numbers[0], numbers[1]))

	if operation == 3:
		print(numbers[0], " x ", numbers[1], " = ", calc.mul(numbers[0], numbers[1]))

	if operation == 4:
		print(numbers[0], " / ", numbers[1], " = ", calc.div(numbers[0], numbers[1]))

	if operation == 5:
		print(numbers[0], " % ", numbers[1], " = ", calc.mod(numbers[0], numbers[1]))

	cont = input("Would you like to do another calculation? (y/n): ")
	if cont != 'y' and cont != 'Y':
		run = False