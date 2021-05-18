# Data Science from Scratch by Joel Grus
from collections import defaultdict, Counter

phrase = 'Do consectetur qui proident aliqua enim pariatur.'

letter_counts = defaultdict(int)  # int() produces 0
for letter in phrase:
    letter_counts[letter] += 1

print(letter_counts)

letter_counter = Counter(phrase)
print(letter_counter)

letter_set = set(phrase)
num_distinct_letters = len(letter_set)
print(num_distinct_letters)

# in-place sorting vs pure sorted function
sorted_phrase = sorted(phrase)
print(sorted_phrase)

phrase_as_list = list(phrase)
phrase_as_list.sort()
print(phrase_as_list)
