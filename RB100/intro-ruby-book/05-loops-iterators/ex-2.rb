# Write a while loop that takes input from the user, performs an action,
# and only stops when the user types "STOP". Each loop can get info from the user.

while true
  5.times { puts "You are adorable!" }

  puts "Type STOP if you do not want me to say it anymore."
  user_choice = gets.chomp

  if user_choice == "STOP"
    puts "Bye!"
    break
  end
end

