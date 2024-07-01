import re

def analyze_text(text):
    # Split the text into words
    words = re.findall(r'\b\w+\b', text)

    # Initialize variables for statistics
    total_words = len(words)
    capitalized_words = 0
    uppercase_words = 0
    lowercase_words = 0
    numbers = []
    sum_of_numbers = 0

    # Iterate through words and collect statistics
    for word in words:
        if word.istitle():
            capitalized_words += 1
        elif word.isupper():
            uppercase_words += 1
        elif word.islower():
            lowercase_words += 1
        elif word.isdigit():
            numbers.append(int(word))
            sum_of_numbers += int(word)

    # Output statistics
    print(f"Total words: {total_words}")
    print(f"Words starting with a capital letter: {capitalized_words}")
    print(f"Words written in all uppercase: {uppercase_words}")
    print(f"Words written in all lowercase: {lowercase_words}")
    print(f"Numbers: {len(numbers)}")
    print(f"Sum of numbers: {sum_of_numbers}")