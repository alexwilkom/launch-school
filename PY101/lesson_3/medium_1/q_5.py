# What do you think the following code will output?
nan_value = float("nan")

print(nan_value == float("nan")) # False

# How can you reliably test if a value is nan?

import math
print(math.isnan(nan_value))