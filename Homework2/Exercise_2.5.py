# Let S be a long string (many lines).
S = """The only way to do great work is to love what you do."""

# Find the number of black characters in S [not whitespace, see the method S.isspace()].
black_char = sum(1 for c in S if not c.isspace())
print(black_char) #41

# Find the number of words in S (a word is a sequence of black characters).
words = S.split()
print(len(words)) #13

# Find the longest word in S.
longest = max(words, key=len)
print(longest) # 'great'

# Sort words from S according to (1) the lexicographic order, (2) the length. 
print(sorted(words)) # ['The', 'do', 'do.', 'great', 'is', 'love', 'only', 'to', 'to', 'way', 'what', 'work', 'you']
