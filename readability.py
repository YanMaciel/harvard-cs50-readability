from cs50 import get_string
import sys


def main():
    text = get_string("Text: ")
    q_letters = count_letters(text)        # Stores the number of letters in one variable
    q_words = count_words(text)            # Stores the number of words in one variable
    q_sentences = count_sentences(text)    # Stores the number of words in one variable

    avg_letters = (q_letters * 100) / q_words       # Calculates average number of letters per 100 words.
    avg_sentences = (q_sentences * 100) / q_words   # Calculates average number of sentences per 100 words.
    index = ((0.0588 * avg_letters) - (0.296 * avg_sentences)) - 15.8    # Calculates Coleman-Liau index

    coleman_liau(index)


def count_letters(text):
    counter = 0
    for element in range(0, len(text)):
        if text[element].isalpha():
            counter += 1

    return counter


def count_words(text):
    counter = 1  # to count the last word of the text that doesnt end in ' ' even after ponctuation
    for element in range(0, len(text)):
        if text[element] == ' ':
            counter += 1

    return counter


def count_sentences(text):
    counter = 0
    for element in range(0, len(text)):
        if text[element] == '.' or text[element] == '!' or text[element] == '?':
            counter += 1

    return counter


def coleman_liau(index):
    if index < 1:
        print("Before Grade 1")
    elif index > 1 and index < 16:
        index = round(index)
        print(f"Grade {index}")
    else:
        print("Grade 16+")


if __name__ == "__main__":
    main()