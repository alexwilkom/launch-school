# Without running this code, what will it print? Why?

dict1 = {
    'a': [1, 2, 3],
    'b': (4, 5, 6),
}

dict2 = dict(dict1)
dict1['a'][1] = 42
print(dict2['a'])     # [1, 42, 3]

# The constructor dict creates a shallow copy, meaning that a new object is created from the top level object, but nested objects in the new object are the same objects of the original one