puts "Choose a number between 0 and 100:"
number = gets.chomp.to_i

if number < 51 
  puts "The number is between 0 and 50"
elsif number < 101
  puts "The number is between 51 and 100"
else
  puts "The number is greater than 100 or less than 0"
end
