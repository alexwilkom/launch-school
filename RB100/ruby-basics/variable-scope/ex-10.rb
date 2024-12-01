# What will the following code print, and why?
# Don't run the code until you have tried to answer.
a = 7
array = [1, 2, 3]

def my_value(ary)
  ary.each do |b|
    a += b
  end
end

my_value(array)
puts a

# Error
# This code snippet will crash when the block of the method invocation each,
# in the method my_value, tries to access the variable 'a'.
# As variables outside methods are not visible, an error will occur.