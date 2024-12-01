# Write a function letter_tally that takes a string as an argument
# and returns a hash with each character from the string and the number of times it appears.

def letter_tally(string)
  return "Not a string" unless string.is_a? String

  string.delete(" ").chars.each_with_object(Hash.new(0)) do |char, tally|
    tally[char] += 1
  end
end

p letter_tally "Welcome to the jungle!!!!!"
p letter_tally "Orlando Orlando Orlando..."
p letter_tally 45
p letter_tally "Alibaba"
