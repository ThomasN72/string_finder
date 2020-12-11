import math


def string_finder(sentence: str, params: list) -> str:
    result = ""
    if not sentence or not params:
        return result

    length = len(sentence)
    sub_string = sentence
    final_first_index = length
    final_last_index = 0
    diff = 0
    while True:
        first_index = length
        last_index = 0

        for param in params:
            index = sub_string.find(param)
            if index == -1:
                return sentence[final_first_index: final_last_index]
            if index > last_index:
                last_index = index + len(param) + diff
            if index < first_index:
                first_index = index + diff

        index = sub_string.find(params[0])
        diff += len(params[0]) + 1
        sub_string = sub_string[:index - 1] + \
            sub_string[index + len(params[0]):]

        if abs(final_last_index - final_first_index) > last_index - first_index:
            final_first_index = first_index
            final_last_index = last_index
