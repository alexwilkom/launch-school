# What will the following code print and why?
# Don't run it until you have tried to answer.

a = 7

def my_value(b)
  b += 10
end

my_value(a)
puts a

# 7. Because 'b' has been reassigned to a new different object and method variables are self-contained.