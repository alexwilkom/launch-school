# What happens when you run the following program? Why do we get that result?
def set_foo():
    foo = 'bar'

set_foo()
print(foo)

# An exception is raised because foo is a local variable. foo is not defined in the global scope.