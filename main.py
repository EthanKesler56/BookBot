from stats import get_book_test, word_count,character_count,dict_sort
import sys

def main():
   if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
   else: 
     book = sys.argv[1]
     word_count(book)
     text = character_count(book)
     dict_sort(text)

main()

