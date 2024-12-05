# Our predict_weather method should output a message indicating whether
# a sunny or cloudy day lies ahead. However, the output is the same
# every time the method is invoked.
# Why? Fix the code so that it behaves as expected.
# def predict_weather
#   sunshine = ['true', 'false'].sample

#   if sunshine
#     puts "Today's weather will be sunny!"
#   else
#     puts "Today's weather will be cloudy!"
#   end
# end

def predict_weather
  sunshine = [true, false].sample

  if sunshine
    puts "Today's weather will be sunny!"
  else
    puts "Today's weather will be cloudy!"
  end
end

# The sunshine array held String objects instead of Boolean.
# Anything that is not nil or false is truthy. Therefore the if clause always executed.