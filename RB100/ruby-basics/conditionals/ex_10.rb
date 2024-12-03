# Reformat the following case statement so that it only takes up 5 lines.
stoplight = ['green', 'yellow', 'red'].sample

# case stoplight
# when 'green'
#   puts 'Go!'
# when 'yellow'
#   puts 'Slow down!'
# else
#   puts 'Stop!'
# end

case stoplight
when 'green'  then puts 'Go!'
when 'yellow' then puts 'Slow down!'
else               puts 'Stop!'
end

# https://docs.ruby-lang.org/en/3.2/syntax/control_expressions_rdoc.html#label-case+Expression