def letter_pairs(line):
    words = line.strip().split()

    for word in words:
        word = word.lower()
        for i in range(len(word) - 1):
            yield word[i] + word[i + 1]


def three_unique_pairs_per_line(filename):
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            pairs = list(letter_pairs(line))
            unique = list(dict.fromkeys(pairs))
            yield unique[:3]
if __name__ == "__main__":
    filename = "text.txt"

    for row_num, pairs in enumerate(three_unique_pairs_per_line(filename), start=1):
        print(f"Рядок {row_num}: {pairs}")