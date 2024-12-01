# What will the following code print, and why?
# Don't run the code until you have tried to answer.
array = [1, 2, 3]

array.each do |element|
  a = element
end

puts a

# NameError
# 'a' is not defined in global scope. Variables inside blocks are not visible outside.
# The method 'puts' is unable to use a variable 'a' as it is not defined in its scope.