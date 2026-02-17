# Finding the most frequent character in a string

s = "abxgytdvjjgfcdxgbnaaa"
chars = list(s)

counts = {}
for ch in chars:
    if ch not in counts:
        counts[ch] = 1
    else:
        counts[ch] += 1

max_char = max(counts, key=counts.get)
print(max_char, counts[max_char])  # a 4


# 'in' operator checks if something exists in a collection
#  Is item (ch) present in counts? → True or False

