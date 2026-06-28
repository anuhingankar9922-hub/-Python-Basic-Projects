import math

try:
    sentence = input("\nEnter a sentence: ")
    words = sentence.split()
    unique_words = set(words)
    sorted_words = sorted(unique_words)

    print("\nUnique Words in Sorted Order:")
    for word in sorted_words:
        print(word)

    total_unique = len(unique_words)
    result = math.pow(total_unique, 2)

    print("\nTotal Unique Words:", total_unique)
    print("\nUnique Words Raised to Power 2:", result)
    print()
except Exception as e:
    print("Error:", e)