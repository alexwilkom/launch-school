# What does this program print? Why?
foo = 'bar'

def set_foo():
    foo = 'qux'

set_foo()
print(foo)

# It prints bar. foo = 'qux' is defined as a local variable in the function set_foo and thus not visible in the global scope.