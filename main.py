import os

def count_words(text):
    words = text.split()
    return len(words)

def print_letter_count(text):
    letters = {}

    for letter in text:
        lowercased_letter = letter.lower()
        for char in lowercased_letter:
            if char.isalpha():
                if char in letters:
                    letters[char] += 1
                else:
                    letters[char] = 1

    # sort dictionary by key
    sorted_letters = dict(sorted(letters.items()))

    for letter, count in sorted_letters.items():
        print(f"{letter}: {count}")

    return sorted_letters

def analyze_books():
    books_folder = "books"

    files_in_folder = os.listdir(books_folder)

    for f in files_in_folder:
        with open(f"{books_folder}/{f}", "r") as file:
            file_contents = file.read()

        print(f"Analyzing {f}")
        print("------------------------")
        print("Word count:")
        print(count_words(file_contents))
        print("------------------------")
        print("Letter count:")
        print_letter_count(file_contents)


def main():
    analyze_books()

if __name__ == "__main__":
    main()