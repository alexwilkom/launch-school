# The following code throws an error. Find out what is wrong and think about how you would fix it.
colors = ['red', 'yellow', 'purple', 'green', 'dark blue', 'turquoise', 'silver', 'black']
things = ['pen', 'mouse pad', 'coffee mug', 'sofa', 'surf board', 'training mat', 'notebook']

colors.shuffle!
things.shuffle!

i = 0 # 7
loop do
  # break if i > colors.length
  # break if i >= things.length # solution
  break if i >= [colors.length, things.length].min # further exploration

  if i == 0
    puts 'I have a ' + colors[i] + ' ' + things[i] + '.'
  else
    puts 'And a ' + colors[i] + ' ' + things[i] + '.'
  end

  i += 1
end

# The code is trying to access an index that does not exist in things array.
# things is out of range, returning nil.
# To solve this problem we can check for things.length instead of colors.length.