# What will the following code print, and why? Don't run the code until you have tried to answer.
a = 7

def my_value(a)
  a += 10
end

my_value(a)
puts a

# 7. Because the 'a' variable inside the method is self-contained and does not interfere with
# the main top-level variables. Variables outside the method are not visible and the reverse is also true.