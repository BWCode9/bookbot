def get_book_text(filepath):
    with open(filepath) as book:
        return book.read()      

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)

main()