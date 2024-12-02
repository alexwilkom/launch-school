# What will the following code print? Why? Don't run it until you've attempted to answer.
def count_sheep
  5.times do |sheep|
    puts sheep
  end
  10
end

puts count_sheep

# 0
# 1
# 2
# 3
# 4
# 10
# This time the number 10 is the returned value of the method, which is printed
# after the numbers of the block 'times'.