def word_count(word_list):
    words = word_list.split()
    return len(words)

def character_count(book_text):
    book = book_text.lower()
    char_count = {}
    for char in book:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def dict_sort(char_count):
    sorted_dict = dict(sorted(char_count.items()))
    return sorted_dict