# You want to have a small script delivering motivational quotes,
# but with the following code you run into a very common error
# message: no implicit conversion of nil into String (TypeError).
# What is the problem and how can you fix it?
def get_quote(person)
  # if person == 'Yoda'
  #   'Do. Or do not. There is no try.'
  # end

  # if person == 'Confucius'
  #   'I hear and I forget. I see and I remember. I do and I understand.'
  # end

  # if person == 'Einstein'
  #   'Do not worry about your difficulties in Mathematics. I can assure you mine are still greater.'
  # end

  if person == 'Yoda'
    return 'Do. Or do not. There is no try.'
  end

  if person == 'Confucius'
    return 'I hear and I forget. I see and I remember. I do and I understand.'
  end

  if person == 'Einstein'
    return 'Do not worry about your difficulties in Mathematics. I can assure you mine are still greater.'
  end
end

puts 'Confucius says:'
puts '"' + get_quote('Confucius') + '"'

# Everything in Ruby returns a value. In this case the method
# checks every if statement as there is no return keyword inside them.
# The last evaluated if statement is always "if person == 'Einstein'",
# thus returning nil if the argument passed does not equal 'Einstein'.
# We just need to use return in every if statement.