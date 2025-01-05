# What will the following code do and why? Don't run it until you have tried 
# to answer.

a = 7

def my_function(b):
    b += 10

my_function(a)
print(a)        # 7

# When 'a' is passed as an argument, the local 'b' variable points to the same 
# object as 'a'. However, when 'b' is reassigned using +=, a new 
# reference to a new object is created. That leaves the global 'a' variable 
# intact.