# What will the following code do and why? Don't run it until you have tried 
# to answer.

x = 10

def my_function():
    x = x + 5
    print(x)

my_function()

# Before running: It will reassign x to x + 5 (15) and print it

# After running: UnboundLocalError: cannot access local variable 'x' where it # is not associated with a value. It is attempting to use a local variable (x) 
# but it has never been initialise.