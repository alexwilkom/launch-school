# Let's do some "ASCII Art": a stone-age form of nerd artwork from back in the 
# days before computers had video screens.

# For this practice problem, write a program that outputs The Flintstones 
# Rock! 10 times, with each line prefixed by one more hyphen than the line 
# above it.

hyphen = '-'

for _ in range(10):
    print(f'{hyphen}The Flintstones Rock!')
    hyphen += '-'
