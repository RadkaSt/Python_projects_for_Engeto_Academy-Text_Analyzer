import re

def plot_word_freq(text):
    # Split the text into words
    words = re.findall(r'\b\w+\b', text)

    # Initialize a dictionary to store word lengths and their frequencies
    word_lengths = {}

    # Count word lengths
    for word in words:
        length = len(word)
        if length in word_lengths:
            word_lengths[length] += 1
        else:
            word_lengths[length] = 1

    # Sort word lengths by frequency (from lowest to highest)
    sorted_lengths = sorted(word_lengths.items())

    # Print the header
    print("LEN |    OCCURRENCES    | NR.")
    print("-" * 28)

    # Print the sorted word lengths and their frequencies
    for length, frequency in sorted_lengths:
        print(f"{length:2}  | {'*' * frequency:<17} | {frequency}")
