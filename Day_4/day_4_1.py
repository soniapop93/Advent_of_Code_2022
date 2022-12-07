input_list = []

with open("input.txt", "r+") as f:
    input_list = [line.replace("\n", "") for line in f]

print(input_list)


def check_pairs(input_list):
    final_sum = 0
    for item in input_list:
        splited_pair = item.split(",")
        pair1 = splited_pair[0].split("-")
        pair2 = splited_pair[1].split("-")

        pair1_range = [i for i in range(int(pair1[0]), int(pair1[1]) + 1)]
        pair2_range = [i for i in range(int(pair2[0]), int(pair2[1]) + 1)]

        if all(elem in pair1_range for elem in pair2_range) or all(elem in pair2_range for elem in pair1_range):
            final_sum = final_sum + 1

    return final_sum


print(check_pairs(input_list))
