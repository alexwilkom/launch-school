# What will the following code print, and why?
# Don't run the code until you have tried to answer.
a = "Xyzzy"

def my_value(b)
  b[2] = '-'
end

my_value(a)
puts a

# Xy-zy. The string object "Xyzzy" is being passed into the method referenced by variable 'a'.
# In Ruby stringd are mutable and line 'b[2] = '-'' in the method is mutating the object rather than creating a new one.