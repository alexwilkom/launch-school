# Without running this code, what will it print? Why?

set1 = {42, 'Monty Python', ('a', 'b', 'c')}
set2 = set1
set1.add(range(5, 10))
print(set2)  # {42, 'Monty Python', ('a', 'b', 'c'), range(5, 10)}

# set2 points to the same object as set1 points in the same memory address.
# Changing one set also changes the other.