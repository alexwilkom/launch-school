# Modify the age.py program you wrote in Exercise 3 of the Input/Output
# chapter. The updated code should use a for loop to display the future ages.

age = int(input('How old are you? '))
print(f'You are {age} years old.')

for years in [10, 20, 30, 40]:
    print(f'In {years} years, you will be {age + years} years old.')