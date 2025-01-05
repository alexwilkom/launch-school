# What will the following code do and why? Don't run it until you have tried 
# to answer.

a = 1

def my_function():
    a = 2

my_function()
print(a) # 1

# The 'a' variable created inside the my_function is a local variable and not 
# seen in the global scope. The invokation of my_function does nothing. 1 is 
# printed because there is a global variable initialised.