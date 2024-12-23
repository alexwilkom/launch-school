# Without running the following code, what do you think it will do?

def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42)

# There is an error on the parameters definitions. When we create a default value, all the subsequent parameters must also have a default value.