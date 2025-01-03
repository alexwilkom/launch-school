# Modify the following code so the loop continues iterating until the user 
# inputs 'yes'.

while True:
    answer = input('Should I stop looping? yes or no: ')

    if answer == 'yes':
        print('Bye!')
        break