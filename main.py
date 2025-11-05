from stats import get_num_words


def get_book_text(filepath: str):
    with open(filepath, "r") as file:
        file_contents = file.read()
        return file_contents


def main():
    filepath = "./books/frankenstein.txt"
    print(get_book_text(filepath))
    get_num_words(text=get_book_text(filepath=filepath))


if __name__ == "__main__":
    main()
