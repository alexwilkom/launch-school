import json

with open('calculator-messages.json', 'r') as file:
    MESSAGES = json.load(file)

def prompt(message):
    print(f"=> {message}")

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

def ask_numbers():
    prompt(MESSAGES['first_number'])
    number1 = input()

    while invalid_number(number1):
        prompt(MESSAGES['invalid_number'])
        number1 = input()

    prompt(MESSAGES['second_number'])
    number2 = input()

    while invalid_number(number2):
        prompt(MESSAGES['invalid_number'])
        number2 = input()

    return (number1, number2)

def ask_operation():
    prompt(MESSAGES['choose_operation'])
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt(MESSAGES['error_operation'])
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

prompt(MESSAGES['welcome'])

while True:
    result = perform_operation(ask_numbers(), ask_operation())
    prompt(f'The result is: {result}')

    prompt(MESSAGES['another_operation'])
    answer = input()
    if answer.lower() != 'y':
        break
