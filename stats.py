def get_book_test(filepath):
    with open(filepath) as file:
        file_contents = file.read()

    return file_contents


def word_count(book_contents):
    count = 0
    words = get_book_test(book_contents)
    word_list = words.split()
    for word in word_list:
        count += 1
    print(f'Found {count} total words')

def character_count(book_contents):
    character_dict = {}
    count = 0
    characters = get_book_test(book_contents)
    lower_characters = characters.lower()
    for char in lower_characters:
        if char not in character_dict:
            character_dict[char] = char.count(char)
        else:
            character_dict[char] += 1
    return character_dict

def helper(items):
    return items["num"]

def dict_sort(dictionary):
    new_dict = sorted(dictionary.items())
    final_dict = dict(new_dict)
    return final_dict


text = character_count('books/frankenstein.txt')
print(dict_sort(text))



