def get_book_text(filepath):
    with open(filepath) as book:
        return book.read()  

def get_words_in_text(text):
    num_words = len(text.split())
    return f"{num_words} words found in the document"

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    total_words = get_words_in_text(text)
    print(total_words)

main()