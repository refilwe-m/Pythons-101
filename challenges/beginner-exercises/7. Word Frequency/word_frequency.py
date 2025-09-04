'''Word Frequency
Ask for a sentence and count how many times each word appears. Store results in a dictionary.
Example:
"the cat and the dog" → { "the": 2, "cat": 1, "and": 1, "dog": 1 }'''

def word_frequency():
    sentence = input('Your sentence: ').lower()
    words = set(sentence.split())
    counts = {}
    for entry in words:
         counts[entry] = sentence.count(entry)
    return counts
         
print(word_frequency())