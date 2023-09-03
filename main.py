with open("books/frankenstein.txt") as f:
    file_contents = f.read()

def word_count(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    print(count)

def count_letters(text):
    text = str(text.lower())
    letter_count = {}
    for letter in text:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count


def text_analysis(text):
    letter_count = count_letters(text)
    for letter, count in letter_count.items(): # change this line
        print(f"The '{letter}' character was found {count} times") # change this line


word_count(file_contents)

count_letters(file_contents)

text_analysis(file_contents)

