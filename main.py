from stats import get_word_count

def get_books_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()

    return file_contents



## main starts here ##

book = get_books_text("books/frankenstein.txt")

word_count = get_word_count(book)

print(f"{word_count} words found in the document")
