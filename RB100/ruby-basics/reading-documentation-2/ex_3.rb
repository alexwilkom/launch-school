# Assume you have the following code:
s = 'abc def ghi,jkl mno pqr,stu vwx yz'
puts s.split.inspect # ["abc", "def", "ghi,jkl", "mno", "pqr,stu", "vwx", "yz"]
puts s.split(',').inspect # ["abc def ghi", "jkl mno pqr", "stu vwx yz"]
puts s.split(',', 2).inspect # Could not figure out from the docs. Used irb -> ["abc def ghi", "jkl mno pqr,stu vwx yz"]
# What will each of the 3 puts statements print?