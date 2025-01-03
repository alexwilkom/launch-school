# Loop over the elements of the fish_list list below, logging each one. 
# Terminate the loop immediately after printing the string 'Nemo'.

fish_list = ['Dory', 'Marlin', 'Gill', 'Nemo', 'Bruce']

for fish in fish_list:
    print(fish)
    if fish == 'Nemo':
        break

# while loop
index = 0

while index < len(fish_list):
    fish = fish_list[index]
    print(fish)
    if fish == 'Nemo':
        break
    index += 1