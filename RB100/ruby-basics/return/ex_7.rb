# What will the following code print? Why? Don't run it until you've attempted to answer.
def count_sheep
  5.times do |sheep|
    puts sheep
  end
end

puts count_sheep

# 0
# 1
# 2
# 3
# 4
# 5
# The block inside the method prints the numbers 0 to 4. 
# The block is the last line of the method and therefore it evaluates to whatever
# the block 'times' returns, the number 5, which is printed when puts method
# invokes the count_sheep method.