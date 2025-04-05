from stats import get_words_in_text

def get_book_text(filepath):
    with open(filepath) as book:
        return book.read()  

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    total_words = get_words_in_text(text)
    print(total_words)

main()