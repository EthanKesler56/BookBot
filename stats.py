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


def dict_sort(char_dict):
    new_list = []
    for key,value in char_dict.items():     
        new_dict = {"char":key, "num":value}
        new_list.append(new_dict)
        
    new_list.sort(reverse=True,key=helper)

    for item in new_list: 
        if item["char"].isalpha(): 
            print(f'{item["char"]}: {item["num"]}')

    





