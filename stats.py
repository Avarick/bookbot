def word_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    text_list = list(text)
    characters = {}

    for letter in text_list:
        char = f'{letter.lower()}'
        characters[char] = characters.get(char,0) + 1
    
    return characters

def sort_on(dict):
    return dict["num"]

def char_sort(char_dict):
    
    char_list = []

    for char in char_dict:
        char_list.append({"char": char, "num": char_dict[char]})
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list