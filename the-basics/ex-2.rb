print "Enter number: "
number = gets.chomp.to_i

thousand = number / 1000
hundreds = number % 1000 / 100
tens = number % 100 / 10
ones = number % 10

puts "#{thousand}, #{hundreds}, #{tens}, #{ones}"
