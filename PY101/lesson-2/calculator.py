# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user for an operation to perform.
# Perform the operation on the two numbers.
# Print the result to the terminal.

def prompt(message):
    print(f"=> {message}")

prompt('Welcome to Calculator!')

# Ask the user for the first number
prompt("What's the first number?")
number1 = input()

# Ask the user for the second number
prompt("What's the second number?")
number2 = input()

prompt('What operation would you like to perform?\n'
      '1) Add 2) Subtract 3) Multiply 4) Divide')
operation = input()

if operation == '1':   # '1' represents addition
    output = int(number1) + int(number2)
elif operation == '2': # '2' represents subtraction
    output = int(number1) - int(number2)
elif operation == '3': # '3' represents multiplication
    output = int(number1) * int(number2)
elif operation == '4': # '4' represents division
    output = int(number1) / int(number2)

prompt(f"The result is: {output}")