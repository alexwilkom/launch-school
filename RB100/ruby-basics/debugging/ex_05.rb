# We want to iterate through the numbers array and return
# a new array containing only the even numbers.
# However, our code isn't producing the expected output.
# Why not? How can we change it to produce the expected result?
numbers = [5, 2, 9, 6, 3, 1, 8]

# even_numbers = numbers.map do |n|
#   n if n.even?
# end
even_numbers = numbers.select do |n|
  n.even?
end

p even_numbers # expected output: [2, 6, 8]

# Array#map returns a new array with the same number of elements of the original.
# We have to use Array#select if we want only the numbers based on the condition.