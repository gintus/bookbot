import sys

from stats import get_sorted_report_list, get_num_char, get_num_words

def get_book_text(filepath):
    with open(filepath) as f:
        book_string = f.read()
        return book_string

def print_report(sorted_report_list, book_name, total_number):
    report_string = ("============ BOOKBOT ========="
    "===\nAnalyzing book found at books/frankenstein."
    "txt...\n----------- Word Count ----------\nFound "
    "75767 total words\n--------- Character Count -------\n"
    "{sorted_report_list}============= END ===============")
    data_string = "".join([f"{dictionary["char"]}: {dictionary["num"]}\n" for dictionary in sorted_report_list if dictionary["char"].isalpha()])
    report_string = (
        "============ BOOKBOT ============\n"
        f"Analyzing book found at {book_name}...\n"
        "----------- Word Count ----------\n"
        f"Found {total_number} total words\n"
        "--------- Character Count -------\n"
        f"{data_string}"
        "============= END ==============="
        )
    print(report_string)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        book_string = get_book_text(sys.argv[1])
        total_num_words = get_num_words(book_string)
        count_dict = get_num_char(book_string)
        sorted_report_list = get_sorted_report_list(count_dict)
        print_report(sorted_report_list, sys.argv[1], total_num_words)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)