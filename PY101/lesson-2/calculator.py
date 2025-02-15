def prompt(message):
    print(f"=> {message}")

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

def ask_numbers():
    prompt("What's the first number?")
    number1 = input()

    while invalid_number(number1):
        prompt("Hmm... that doesn't look like a valid number.")
        number1 = input()

    prompt("What's the second number?")
    number2 = input()

    while invalid_number(number2):
        prompt("Hmm... that doesn't look like a valid number.")
        number2 = input()

    return (number1, number2)

def ask_operation():
    prompt('What operation would you like to perform?\n'
        '1) Add 2) Subtract 3) Multiply 4) Divide')
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt('You must choose 1, 2, 3, or 4')
        operation = input()

    return operation

def perform_operation(numbers, operation):
    match operation:
        case '1':
            output = int(numbers[0]) + int(numbers[1])
        case '2':
            output = int(numbers[0]) - int(numbers[1])
        case '3':
            output = int(numbers[0]) * int(numbers[1])
        case '4':
            output = int(numbers[0]) / int(numbers[1])

    return output

prompt('Welcome to Calculator!')

while True:
    result = perform_operation(ask_numbers(), ask_operation())
    prompt(f'The result is: {result}')

    prompt('Would you like to perform another operation?\n'
           'Type y if yes. Reply anything else if not.')
    answer = input()
    if answer.lower() != 'y':
        break
