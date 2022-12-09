input_list = []

with open("input.txt", "r+") as f:
    input_list = [line.replace("\n", "") for line in f]

print(input_list)


def count_characters_number(input_list):
    for item in input_list:
        for i in range(0, len(item)):
            get_items = [item[x] for x in range(i, i + 14)]
            set_items = set(get_items)
            if len(set_items) == 14:
                return i + 14


print(count_characters_number(input_list))
