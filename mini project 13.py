from collections import Counter

elements = [1, 2, 3, 4, 5]
frequency = Counter(elements)

print("Frequency of elements:")
for key, value in frequency.items():
    print(f"{key}: {value}")
