# Given the following code...
x = "hi there"
my_hash = {x: "some value"}
my_hash2 = {x => "some value"}
# What's the difference between the two hashes that were created?

# my_hash uses the symbol x because uses a colon instead of the hash rocket.
# my_hash2 uses the value that is in the 'x' variable as a key. A string in this case.
p my_hash
p my_hash2