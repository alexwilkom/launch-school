# Write a program that requests two integers from the user, adds them together,
# and then displays the result. Furthermore, insist that one of the integers
# be positive, and one negative; however, the order in which
# the two integers are entered does not matter.

# Do not check for the positive/negative requirement until both integers
# are entered, and start over if the requirement is not met.

# You may use the following method to validate input integers:
def valid_number?(number_string)
  number_string.to_i.to_s == number_string && number_string.to_i != 0
end

# My code:

def opposites?(first_number, second_number)
  first_number.to_i * second_number.to_i < 0
end

first_number = nil
second_number = nil

loop do
  loop do 
    puts ">> Please enter a positive or negative integer:"
    first_number = gets.chomp
    break if valid_number?(first_number)
    puts ">> Invalid input. Only non-zero integers are allowed."
  end

  loop do
    puts ">> Please enter a positive or negative integer:"
    second_number = gets.chomp
    break if valid_number?(second_number)
    puts ">> Invalid input. Only non-zero integers are allowed."
  end

  if opposites?(first_number, second_number)
    result = first_number.to_i + second_number.to_i
    puts "#{first_number} + #{second_number} = #{result}"
    break
  else
    puts ">> Sorry. One integer must be positive, one must be negative."
    puts ">> Please start over."
  end
end