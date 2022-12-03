input_list = []

with open("input.txt", "r+") as f:
    input_list = [line.replace("\n", "") for line in f]


def count_calories(input_list):
    list_of_calories = []
    temp_list = []
    for i in input_list:
        if i == "":
            temp_list = []
            list_of_calories.append(temp_list)
        else:
            temp_list.append(int(i))

    list_of_sum_calories_sorted = sorted([sum(x) for x in list_of_calories], reverse=True)

    return list_of_sum_calories_sorted[0] + \
           list_of_sum_calories_sorted[1] + \
           list_of_sum_calories_sorted[2]


print(count_calories(input_list))
