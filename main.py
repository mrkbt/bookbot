import sys
from stats import get_num_words, get_num_characters, sort_num_characters


def get_book_text(filepath: str):
    with open(filepath, "r") as file:
        file_contents = file.read()
        return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    get_num_words(text=get_book_text(filepath=filepath))
    print("--------- Character Count -------")

    text = get_book_text(filepath)
    num_characters = get_num_characters(text)
    sorted_list = sort_num_characters(num_characters)
    for item in sorted_list:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


if __name__ == "__main__":
    main()
