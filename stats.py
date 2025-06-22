def get_num_words(book):
    word_list = book.split()
    return len(word_list)


def get_num_char(book):
    count_dict = {}
    for character in book:
        char_lowered = character.lower()
        if char_lowered not in count_dict:
            count_dict.update({char_lowered: 1})
        else:
            count_dict[char_lowered] += 1
    return count_dict


def get_sorted_report_list(count_dict):
    report_list = []
    for key, value in count_dict.items():
        temp_dict = {"char": key, "num": value}
        report_list.append(temp_dict)
    return sorted(report_list, key= lambda item: item["num"], reverse=True)
