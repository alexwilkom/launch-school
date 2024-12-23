# Write a program that uses a multiply function to multiply two numbers and returns the result. Ask the user to enter the two numbers, then output the numbers and result as a simple equation.

def multiply(first, second):
    return first * second

first_number = float(input('Enter the first number: '))
second_number = float(input('Enter the second number: '))
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')
