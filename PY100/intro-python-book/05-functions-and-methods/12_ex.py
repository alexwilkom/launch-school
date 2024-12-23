# Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo()

# It will raise an exception as there it needs at least the first argument to be passed because it has no default value.