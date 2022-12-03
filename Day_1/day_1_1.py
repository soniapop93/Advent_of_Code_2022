input_list = []

with open("input.txt", "r+") as f:
    input_list = [line.replace("\n", "") for line in f]

print(input_list)


def count_calories(input_list):
    list_of_calories = []
    temp_list = []
    for i in input_list:
        if i == "":
            temp_list = []
            list_of_calories.append(temp_list)
        else:
            temp_list.append(int(i))

    most_calories = max([sum(x) for x in list_of_calories])

    return most_calories


print(count_calories(input_list))
