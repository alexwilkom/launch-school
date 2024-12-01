# Using some of Ruby's built-in Hash methods, write a program that loops through a hash and prints all of the keys.
# Then write a program that does the same thing except printing the values.
# Finally, write a program that prints both.

family = {
  uncle: "Bob",
  sister: "Jane",
  brother: "Frank",
  aunt: "Mary"
}

# prints keys
family.keys.each { |key| puts key }
puts "--------"
# print values
family.values.each { |value| puts value }
puts "--------"
# prints both
family.each { |key, value| puts "My #{key} is #{value}"}
puts "--------"
