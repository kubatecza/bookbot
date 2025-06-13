from stats import get_num_words, get_num_chars, get_sorted_chars_list
import sys

def get_book_text(book_path):
    with open(book_path) as book_file:
        return book_file.read()
 
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    book_text = get_book_text(path)
  
    num_words = get_num_words(book_text)
    num_chars = get_num_chars(book_text)
    char_count = get_sorted_chars_list(num_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in char_count:
        print(f"{char['char']}: {char['num']}")
    print("============= END ===============") 

main()
