# Write a function that returns the last element of a list provided as an 
# argument. For example:

def first(lst):
    return lst[-1] if lst else None

print(first(['Earth', 'Moon', 'Mars']))  # Mars

# Be sure to handle the case where the input list is empty.
