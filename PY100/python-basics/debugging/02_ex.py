# Our predict_weather function should output a message indicating whether a 
# sunny or cloudy day lies ahead. However, the output is the same every time 
# the function is invoked. Why? Fix the code so that it behaves as expected.

import random

def predict_weather():
    sunshine = random.choice(['True', 'False']) # Here strings are used instead of booleans. In this case it will always be True in a conditional, as a non-empty string is always truthy.

    sunshine = random.choice([True, False])

    if sunshine:
        print("Today's weather will be sunny!")
    else:
        print("Today's weather will be cloudy!")

predict_weather()