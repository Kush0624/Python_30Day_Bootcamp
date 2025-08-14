# 🎯 Day 4 Mini Task

# 📌 Write a program to:

# Take a sentence from the user.

# Count the frequency of each word (case-insensitive).

# Print the dictionary with word counts.

sentence=input("enter any string").lower().split()

word_count={}

for word in sentence:
    word_count[word]=word_count.get(word,0)+1

print(word_count)

