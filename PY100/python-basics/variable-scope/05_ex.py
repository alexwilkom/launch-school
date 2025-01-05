# What will the following code do and why? Don't run it until you have tried 
# to answer.

a = 1

def my_function():
    print(a)
    a = 2

my_function()

# UnboundLocalError. Python recognise the assignment 2 to 'a' inside the 
# function but it tries to print it before is initialised.