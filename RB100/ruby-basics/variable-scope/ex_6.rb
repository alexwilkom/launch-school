# What will the following code print, and why?
# Don't run the code until you have tried to answer.
a = 7

def my_value(b)
  b = a + a
end

my_value(a)
puts a

# NameError
# 'a' is not visible from inside the method.