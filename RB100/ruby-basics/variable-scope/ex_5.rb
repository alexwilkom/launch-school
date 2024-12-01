# What will the following code print, and why?
# Don't run the code until you have tried to answer
a = "Xyzzy"

def my_value(b)
  b = 'yzzyX'
end

my_value(a)
puts a

# Xyzzy
# The method is creating a new string object when reassigning b to 'yzzyX',
# stopping the reference to the string object that 'a' is pointing.
# Thus not mutating variable 'a'.