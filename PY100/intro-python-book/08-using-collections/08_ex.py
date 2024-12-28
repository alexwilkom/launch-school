# Explain why the code below prints different values on lines 3 and 4.

text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8   Slicing creates a new array, and so the search starts at 0.
print(text.rfind('f', 21, 35))    # 29  Here the search is on the original collections starting at index 21 and ending at index 35.