def calculator(num1, num2, operation):
	match operation:
		case 'plus':
			print(f"{num1 + num2}");
		case 'minus':
			print(f"{num1 - num2}");
		case 'divide':
			print(f"{num1 / num2}");
		case 'multiply':
			print(f"{num1 * num2}");

calculator(10,4,'plus')
calculator(10,4,'minus')
calculator(10,4,'divide')
calculator(10,4,'multiply')
