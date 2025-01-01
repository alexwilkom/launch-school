# Python lists come with a variety of built-in methods that allow for common 
# list manipulations. One such operation is determining the index of an item 
# in the list.

# Given a list:

fruits = ["apple", "banana", "cherry", "peach", "watermelon"]

# How would you determine the index of the fruit "cherry" in this list?

# Refer to the official Python documentation on lists to assist with your 
# answer.

fruit = 'cherry'
if fruit in fruits:
    print(fruits.index('cherry')) # 2
else:
    print(f'{fruit} not in fruits.')