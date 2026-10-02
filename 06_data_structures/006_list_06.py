o_text = "the quick brown fox jumps over the lazy dog the fox runs"
"""
Word frequency counter (lists + strings + loops + conditions, no dicts)

text = "the quick brown fox jumps over the lazy dog the fox runs"

Using only lists (no dictionaries — those come later), build two parallel lists: words (unique words, in first-appearance order) and counts (how many times each appeared). Then print the most frequent word and its count. On a tie, print the one that appeared first in the text. Your code must handle an empty string without crashing.
- By Claude."""

o_text = "the quick brown fox jumps over the lazy dog the fox runs"

words = o_text.split()

unique_words = []
counts = []

for word in words:
    pos = -1

    for i in range(len(unique_words)):
        if unique_words[i] == word:
            pos = i
            break

    if pos == -1:
        unique_words.append(word)
        counts.append(1)
    else:
        counts[pos] += 1

print(unique_words)
print(counts)

if unique_words:
    max_pos = 0

    for i in range(1, len(counts)):
        if counts[i] > counts[max_pos]:
            max_pos = i

    print("Most frequent word:", unique_words[max_pos])
    print("Count:", counts[max_pos])
else:
    print("The text is empty.")
