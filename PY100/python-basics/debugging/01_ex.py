# You come across the following code. What errors does it raise for the given 
# examples and what exactly do the error messages mean?

def find_first_nonzero_among(numbers):
    for n in numbers: # After invoking find_first_nonzero_among(1), TypeError. int object is not iterable
        if n != 0:
            return n

# find_first_nonzero_among(0, 0, 1, 0, 2, 0)
# TypeError. It takes too many arguments; it accepts only one, which must be 
# iterable.

# find_first_nonzero_among(1)

find_first_nonzero_among([0, 0, 1, 0, 2, 0])
find_first_nonzero_among([1])