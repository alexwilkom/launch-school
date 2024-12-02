# What will the following code print? Why? Don't run it until you've attempted to answer.
def tricky_number
  if true
    number = 1
  else
    2
  end
end

puts tricky_number

# 1
# The if/else statement will always enter the if clause. number = 1 is the last line
# evaluated and a variable always return its own value. Therefore it can be determined
# that the number 1 will be returned and printed.