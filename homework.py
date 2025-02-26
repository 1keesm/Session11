import requests # library to download book from web link

# Links for the two books
link_1 = "https://gutenberg.org/cache/epub/2600/pg2600.txt" # War and PEace
link_2 = "https://gutenberg.org/cache/epub/1184/pg1184.txt" # Count of Monte Cristo

result1 = requests.get(link_1)
result2 = requests.get(link_2)

unique_words_1 = {}
unique_words_2 = {}
punctuations = ";:,.'!?-=()[]/|{}"

# War and Peace analysis
# Looping over each line and replace punctuations
for line in result1.text.splitlines():
    for p in punctuations:
        line = line.replace(p, " ")
    words = line.split()
# Looping over each word to count occurrences of unique words
    for word in words:
        word = word.lower()
        unique_words_1[word] = unique_words_1.get(word, 0) + 1

# Count of Monte Cristo analysis
# Looping over each line and replace punctuations
for line in result2.text.splitlines():
    for p in punctuations:
        line = line.replace(p, " ")
    words = line.split()
# Looping over each word to count occurrences of unique words
    for word in words:
        word = word.lower()
        unique_words_2[word] = unique_words_2.get(word, 0) + 1

# Saving values of unique word frequencies in a list to compare between the books
freq_1 = list(unique_words_1.items())
freq_2 = list(unique_words_2.items())

print(f"War and Peace has {len(freq_1)} unique words while The Count of Monte Cristo has {len(freq_2)} unique words")
#War and Peace has more unique words