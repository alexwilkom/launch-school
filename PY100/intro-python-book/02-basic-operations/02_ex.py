def extract_ones(number):
    return number % 10

def int_division(number):
    return number // 10

num = 4936

ones = extract_ones(num)
num = int_division(num)

tens = extract_ones(num)
num = int_division(num)

hundreds = extract_ones(num)
num = int_division(num)

thousands = extract_ones(num)

print(thousands, hundreds, tens, ones)