# Assume that obj already has a value of 42 when the code below starts running. Which of the subsequent statements reassign the variable? Which statements mutate the value of the object that obj references? Which statements do neither? If necessary, you can read the documentation.

# obj = 42
obj = 'ABcd'        # Reassignment
obj.upper()         # Nothing
obj = obj.lower()   # Reassignment
print(len(obj))     # Nothing
obj = list(obj)     # Reassignment
obj.pop()           # Mutate
obj[2] = 'X'        # Mutate
obj.sort()          # Mutate
set(obj)            # Nothing
obj = tuple(obj)    # Reassignment