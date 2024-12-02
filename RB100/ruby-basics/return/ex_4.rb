# What will the following code print? Why? Don't run it until you've attempted to answer.
def meal
  puts 'Dinner'
  return 'Breakfast'
end

puts meal

# "Dinner"
# "Breakfast"
# The puts method inside meal method prints "Dinner". The meal method returns the string "Breakfast",
# which is printed by the puts method calling the meal method.