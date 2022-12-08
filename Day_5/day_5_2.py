input_list = []

with open("input.txt", "r+") as f:
    input_list = [line.replace("\n", "") for line in f]

print(input_list)


def get_crates(input_list):
    final_string = ""
    dict_of_columns = {}
    move_list_actions = []
    for item in input_list:
        if "move" not in item and "[" in item:
            column_count = 1
            for i in range(1, len(item), 4):
                if item[i] != " ":
                    if column_count not in dict_of_columns.keys():
                        dict_of_columns[column_count] = []
                    dict_of_columns[column_count].append(item[i])
                column_count = column_count + 1
        elif "move" in item:
            new_item_array = item.replace("move ", "").replace(" from ", "-").replace(" to ", "-").split("-")
            move_list_actions.append(new_item_array)

    for key, value in dict_of_columns.items():
        new_value = value[::-1]
        dict_of_columns[key] = new_value

    for action_item in move_list_actions:
        list_of_crates = []
        for i in range(0, int(action_item[0])):
            crate_item = dict_of_columns[int(action_item[1])].pop()
            list_of_crates.append(crate_item)
        dict_of_columns[int(action_item[2])] += list_of_crates[::-1]

    for index_key in range(1, len(dict_of_columns) + 1):
        final_string = final_string + dict_of_columns[index_key][-1]

    return final_string


print(get_crates(input_list))
