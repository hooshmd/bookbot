import sys
from stats import word_count # type: ignore
from stats import character_count # type: ignore
from stats import dict_sort # type: ignore

def get_book_text(path):
    file_contents = open(path).read()
    return file_contents

def main(path):
    sorted_dict = dict_sort(character_count(get_book_text(path)))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(get_book_text(path))} total words")
    print("--------- Character Count -------")
    for letter in sorted_dict:
        if letter.isalpha():
            print(f"{letter}: {sorted_dict[letter]}")
    print("============= END ===============")

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    path = sys.argv[1]
    main(path)