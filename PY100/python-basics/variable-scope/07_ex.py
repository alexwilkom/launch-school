# What will the following code do and why? Don't run it until you have tried 
# to answer.

a = 1

def my_function():
    global a
    a = 2

my_function()
print(a) # 2

# The global keyword is used in order to change the value of the global variable a.