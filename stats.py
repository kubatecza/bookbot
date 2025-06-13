def get_num_words(book):
    words = book.split()
    return len(words)

def get_num_chars(book):
    char_count = {}
  
    chars = list(book)
    for char in chars:
        lowered_char = char.lower()
        if lowered_char not in char_count:
            char_count[lowered_char] = 1
        else:
            char_count[lowered_char] += 1
  
    return char_count

 
def get_sorted_chars_list(char_dict):
    dicts_list = []

    for char in char_dict:
        if not char.isalpha():
            continue

        dicts_list.append({"char": char, "num": char_dict[char]})

    def sort_on(dict):
        return dict["num"]
  
    dicts_list.sort(key=sort_on, reverse=True)

    return dicts_list