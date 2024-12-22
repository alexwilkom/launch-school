# What happens when you run the following code? Why?

NAME = 'Victor'
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)

NAME = 'Nina'
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)

# The first three 'print' calls will display the greeting with the name Victor.
# The last three 'print' calls will display the greeting with the name Nina.
# Constants are not pure constants in python and the reassignemnt is totally legal, although a poor practice and not recommended.