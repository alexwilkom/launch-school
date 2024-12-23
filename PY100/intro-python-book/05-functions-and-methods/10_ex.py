# Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592)

# It will print the arguments and the default value of 'third' (2) parameter 
# 42
# 3.141592
# 2