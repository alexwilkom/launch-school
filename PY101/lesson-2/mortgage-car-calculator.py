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

prompt('What is the interest rate?')
interest_rate = input()
while invalid_number(interest_rate):
    prompt('Please enter a valid number (positive whole or decimal numbers).')
    interest_rate = input()

prompt('What is the loan duration in years?')
loan_duration_years = input()
while invalid_number(loan_duration_years):
    prompt('Please enter a valid number (whole positive numbers).')
    loan_duration_years = input()

monthly_interest_rate = float(interest_rate) / 100 / 12
loan_duration_months = float(loan_duration_years) * 12
monthly_payment = float(loan_amount) * (
        monthly_interest_rate /
            (1 - (1 + monthly_interest_rate) ** (-loan_duration_months))
    )