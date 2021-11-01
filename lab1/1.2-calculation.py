operation = input('Enter operation:')
number1 = int(input('Enter your first number:'))
number2 = int(input('Enter your second number:'))
if operation == '*':
    print(number1 * number2)
elif operation == '/':
    print(number1 / number2)
elif operation == '+':
    print(number1 + number2)
elif operation == '-':
    print(number1 - number2)
elif operation == '%':
    print(number1 % number2)
else:
    print('WRONG OPERATION!')