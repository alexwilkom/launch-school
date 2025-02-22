def prompt(message):
    print(f'=> {message}')

def invalid_number(number_str):
    try:
        number = float(number_str)
        if number <= 0:
            raise ValueError
    except ValueError:
        return True

    return False

prompt('What is the loan amount?')
loan_amount = input()
while invalid_number(loan_amount):
    prompt('Please enter a positive number.')
    loan_amount = input()

prompt('What is the interest rate? Example: 5.5 for 5.5%')
interest_rate = input()
while invalid_number(interest_rate):
    prompt('Please enter a positive number.')
    interest_rate = input()

prompt('What is the loan duration in years?')
loan_duration_years = input()
while invalid_number(loan_duration_years):
    prompt('Please enter a positive number.')
    loan_duration_years = input()

monthly_interest_rate = float(interest_rate) / 100 / 12
loan_duration_months = float(loan_duration_years) * 12
monthly_payment = float(loan_amount) * (
        monthly_interest_rate /
            (1 - (1 + monthly_interest_rate) ** (-loan_duration_months))
    )

prompt(f"The monthly payment is: ${round(monthly_payment, 2)}")