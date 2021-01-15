def calculator(num1, operator, num2):
	return {
		"+" : num1 + num2,
		"-" : num1 - num2,
		"*" : num1 * num2,
		"/" : num1 // num2 if num2 else "Can't divide by 0!"
	}[operator]