# What does the following code print?

def scream(words):
    words = words + '!!!!'
    return
    print(words)

scream('Yipeee') # Nothing. The print function inside the body is placed after the return keyword, which exits the function and ignores the following lines.