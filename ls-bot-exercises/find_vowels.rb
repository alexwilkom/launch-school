# Write a function find_vowels that takes a string as an argument
# and returns an array containing all of the vowels present in that string.
# The vowels should old appear once in the output array and should be alphabetized.

def find_vowels(string)
  if !string.is_a? String
    return "Not a string"
  end

  vowels = ["a", "e", "i", "o", "u"]
  array_vowels = []

  string.downcase.each_char do |char|
    if vowels.include?(char)
      if !array_vowels.include?(char)
        array_vowels << char
      end
    end
  end
  
  array_vowels.sort
end

p find_vowels "Welcome to the jungle!" # ["e", "o", "u"]
p find_vowels "Anna Maria is alive." # ["a", "i", "e"]
p find_vowels "Marsupial" # ["a", "u", "i"]
p find_vowels "" # []
p find_vowels 1 # "Not a string"
