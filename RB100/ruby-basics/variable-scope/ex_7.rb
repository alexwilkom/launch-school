# What will the following code print, and why?
# Don't run the code until you have tried to answer.
a = 7
array = [1, 2, 3]

array.each do |element|
  a = element
end

puts a

# 3
# 'a' is visible from inside the block.
# 'a' is reassigned every time the block goes through an element of the array.