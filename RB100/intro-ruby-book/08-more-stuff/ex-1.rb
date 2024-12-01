# Write a program that checks if the sequence of characters "lab" exists in the following strings.
# If it does exist, print out the word.

def find_lab_word(string)
  if string =~ /lab/
    puts string
  else
    puts "Not found."
  end
end

find_lab_word("laboratory")
find_lab_word("experiment")
find_lab_word("Pans Labyrinth")
find_lab_word("elaborate")
find_lab_word("polar bear")