# What will the following code print, and why?
# Don't run the code until you have tried to answer.
a = 7

def my_value(b)
  a = b
end

my_value(a + 5)
puts a

# 7. When passing 'a + 5' to the method callig, we are creating a new object
# instead of reassigning 'a'. Variables are not visible to/from methods, leaving top-level
# 'a' variable untouched.