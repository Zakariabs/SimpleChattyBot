word1 = input()
word2 = input()

# How many letters does the longest word contain?
# print(len(word1))
# print(len(word2))

longest_word = max(len(word1), len(word2))
print(longest_word)