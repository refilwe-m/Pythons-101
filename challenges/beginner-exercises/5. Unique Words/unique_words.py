"""Unique Words
Ask for a sentence, split it into words, and print a list of unique words."""

def unique_words():
    sentence = input('Your sentence: ').lower()
    words = set(sentence.split())
    return list(words)

print(unique_words())
    
    