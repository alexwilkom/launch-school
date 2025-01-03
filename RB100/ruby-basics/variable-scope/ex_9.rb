# What will the following code print, and why?
# Don't run the code until you have tried to answer.
a = 7
array = [1, 2, 3]

array.each do |a|
  a += 1
end

puts a
puts array

# 7
# The 'a' inside the block refers to the element in the array, not the 'a' in the global scope.
# The block does not mutate the array.