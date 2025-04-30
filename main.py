from stats import word_count, character_count, char_sort
import sys

def get_book_text(file):
    with open(file) as f:
        return f.read()



def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])
    character_dict = character_count(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(book_text)} total words")
    print("--------- Character Count -------")
    
    sorted_list = char_sort(character_dict)
    for char_dict in sorted_list:
        char = char_dict["char"]
        count = char_dict["num"]
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")
    return 0

main()
