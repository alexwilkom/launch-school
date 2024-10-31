def factorial_of(number)
  return 1 if number == 1
  number * factorial_of(number - 1)
end

puts factorial_of(5)
puts factorial_of(6)
puts factorial_of(7)
puts factorial_of(8)
