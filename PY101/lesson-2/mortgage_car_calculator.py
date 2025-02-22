def prompt(message):
    print(f'\n=> {message}')

def invalid_number(number_str):
    try:
        number = float(number_str)
        if number <= 0:
            raise ValueError
    except ValueError:
        return True

    return False

def get_number(message):
    prompt(message)
    number = input()
    while invalid_number(number):
        prompt('Please enter a positive number.')
        number = input()
    return float(number)

while True:
    loan_amount = get_number('What is the loan amount?')
    interest_rate = get_number('What is the interest rate? ie. 5.5 for 5.5%')
    loan_duration_years = get_number('What is the loan duration in years?')

    monthly_interest_rate = interest_rate / 100 / 12
    loan_duration_months = loan_duration_years * 12
    monthly_payment = loan_amount * (
            monthly_interest_rate /
                (1 - (1 + monthly_interest_rate) ** (-loan_duration_months))
        )

    prompt(f'The monthly payment is: ${round(monthly_payment, 2)}')

    while True:
        answer = input('\nDo you want to perform another calculation? (y/n) ')
        if answer.strip().lower().startswith(('y', 'n')):
            break
        prompt('Please enter "y" or "n".')

    if answer.startswith('n'):
        print('\nThank you for using the Mortgage/Car Loan Calculator!')
        break