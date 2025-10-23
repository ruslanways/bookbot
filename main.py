import sys
from stats import get_num_words, get_num_characters, sorted_num_characters

def text_to_string(path_to_file):
    with open(path_to_file) as f:
        file_string = f.read()
    return file_string

def main():

    if len(sys.argv)<2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text_str = text_to_string(path)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    get_num_words(text_str)

    print("--------- Character Count -------")
    num_characters = get_num_characters(text_str)
    # print(num_characters)
    for item in sorted_num_characters(num_characters):
        print(f"{item['char']}: {item['count']}")
    print("============= END ===============")

main()