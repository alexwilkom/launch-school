# Look at Ruby's merge method. Notice that it has two versions.
# What is the difference between merge and merge!?
# Write a program that uses both and illustrate the differences.

# The merge method returns a new has merging two hashes passed as arguments
# Each duplicate-key entry’s value overwrites the previous value (from docs)
group_one = { black: 2, white: 5, orange: 3 }
group_two = { black: 1, red: 4, blue: 6 }
group_three = { white: 1, purple: 7, yellow: 8 }
groups_merged = group_one.merge(group_two, group_three)
# If using a block, the return value becomes the new value for the entry
groups_merged_with_block = group_one.merge(group_two, group_three) do
  |key, old_value, new_value| old_value + new_value
end

p groups_merged  
p groups_merged_with_block

# The merge! method is like merge method but mutates the original hash
# example from the docs
h = {foo: 0, bar: 1, baz: 2}
h1 = {bat: 3, bar: 4}
h2 = {bam: 5, bat:6}
h.merge!(h1, h2) # => {:foo=>0, :bar=>4, :baz=>2, :bat=>6, :bam=>5}

p h