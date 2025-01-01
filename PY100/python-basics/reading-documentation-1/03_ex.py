# Use the Python documentation for the str class to determine which method can 
# be used to right justify a str object.

name = 'Alex'
print(name)
print(name.rjust(8))       # Without a second argument, rjust pads with spaces
print(name.rjust(8, "*"))