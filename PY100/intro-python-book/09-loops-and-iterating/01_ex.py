# The following code causes an infinite loop (a loop that never stops
# iterating). Why?

counter = 0

while counter < 5:
    print(counter)

# Because we are not increasing the counter in the while body.
# So counter < 5 always evaluates to True.