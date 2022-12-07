input_list = []

with open("input.txt", "r+") as f:
    input_list = [line.replace("\n", "") for line in f]

print(input_list)


def sum_of_priorities_items(input_list):
    lowercase_letters = [chr(lower_letter) for lower_letter in range(ord('a'), ord('z') + 1)]
    uppercase_letters = [chr(upper_letter) for upper_letter in range(ord('A'), ord('Z') + 1)]

    combined_letters = lowercase_letters + uppercase_letters

    final_sum = 0
    for item in range(0, len(input_list), 3):
        common_item = ""

        for i in input_list[item]:
            if (i in input_list[item + 1]) and (i in input_list[item + 2]):
                common_item = i
                break

        if common_item in combined_letters:
            final_sum = final_sum + (int(combined_letters.index(common_item) + 1))

    return final_sum


print(sum_of_priorities_items(input_list))
