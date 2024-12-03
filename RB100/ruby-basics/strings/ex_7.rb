# Given the following code, invoke a destructive method on greeting so that
# Goodbye! is printed instead of Hello!.
# greeting = 'Hello!'
# puts greeting

greeting = 'Hello!'
puts greeting.gsub('Hello', 'Goodbye')

# https://docs.ruby-lang.org/en/3.2/String.html#method-i-gsub