def count_word_occurrences(sahal):
    words = sahal.split()
    word_count = {}
    for word in words:
        word = word.lower()
        word_count[word] = word_count.get(word, 0) + 1
    return word_count
sahal = "This is a sample string with sample words and some repeated words."
result = count_word_occurrences(sahal)
print("Word occurrences:", result)

