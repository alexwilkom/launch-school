def prompt(message):
    print(f'=> {message}')

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

prompt('What is the loan amount?')
loan_amount = input()
while invalid_number(loan_amount):
    prompt('Please enter a valid number (do not use a comma).')
    loan_amount = input()

prompt('What is the Annual Percentage Rate (APR)?')
apr = input()
while invalid_number(apr):
    prompt('Please enter a valid number (positive whole or decimal numbers).')
    apr = input()

prompt('What is the loan duration in years?')
loan_duration_years = input()
while invalid_number(loan_duration_years):
    prompt('Please enter a valid number (whole positive numbers).')
    loan_duration_years = input()