#  Word Counter Program 

# open word file
file = open("word1.txt", "r")

# read complete content
content = file.read()

# count words
words = len(content.split())

# count lines
lines = len(content.splitlines())

# count characters
characters = len(content)

print("Number of words:", words)
print("Number of Lines:", lines)
print("Number of characters:", characters)

file.close()