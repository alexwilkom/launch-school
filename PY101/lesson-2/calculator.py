import json

LANGUAGE = "it"

with open('calculator-messages.json', 'r') as file:
    MESSAGES = json.load(file)

def messages(message, lang=LANGUAGE):
    return MESSAGES[lang][message]

def prompt(message):
    print(f'=> {message}')

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

def ask_numbers():
    prompt(messages('first_number'))
    number1 = input()

    while invalid_number(number1):
        prompt(messages('invalid_number'))
        number1 = input()

    prompt(messages('second_number'))
    number2 = input()

    while invalid_number(number2):
        prompt(messages('invalid_number'))
        number2 = input()

    return (number1, number2)

def ask_operation():
    prompt(messages('choose_operation'))
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt(messages('error_operation'))
        operation = input()

    return operation

def perform_operation(numbers, operation):
    match operation:
        case '1':
            output = float(numbers[0]) + float(numbers[1])
        case '2':
            output = float(numbers[0]) - float(numbers[1])
        case '3':
            output = float(numbers[0]) * float(numbers[1])
        case '4':
            output = float(numbers[0]) / float(numbers[1])

    return output

prompt(messages('welcome'))

while True:
    output = perform_operation(ask_numbers(), ask_operation())
    prompt(messages('result').format(output=output))

    prompt(messages('another_operation'))
    answer = input()
    if answer.lower() != 'y':
        break
