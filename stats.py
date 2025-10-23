def get_num_words(file_string):
    num_words = len(file_string.split())
    print(f"Found {num_words} total words")
    return num_words

def get_num_characters(file_string):
    num_characters = {}
    for i in file_string.lower():
        num_characters[i] = num_characters.get(i, 0) + 1
    return num_characters

def sorted_num_characters(num_characters):
    list_of_dicts = []
    for char, count in num_characters.items():
        if char.isalpha():
            list_of_dicts.append({"char": char, "count": count})
    def sort_on(items):
        return items["count"]
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts
    