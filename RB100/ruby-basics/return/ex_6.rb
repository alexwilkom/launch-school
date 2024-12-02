# What will the following code print? Why? Don't run it until you've attempted to answer.
def meal
  return 'Breakfast'
  'Dinner'
  puts 'Dinner'
end

puts meal

# "Breakfast"
# When the return keyword is encoutered, the value in the line is evaluated, returned,
# and finally the method execution terminated, ignoring all the next lines in the method.