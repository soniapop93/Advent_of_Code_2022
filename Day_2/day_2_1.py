input_list = []

with open("input.txt", "r+") as f:
    input_list = [line.replace("\n", "") for line in f]

print(input_list)


def total_score(input_list):
    # A, X -> Rock, 1
    # B, Y -> Paper, 2
    # C, Z -> Scissors, 3
    # 6 -> if is a win

    total_score_sum = 0
    for item in input_list:
        splited_item_array = item.split(" ")

        # Rock <-> Paper
        if splited_item_array[0] == "A" and splited_item_array[1] == "Y":
            total_score_sum = total_score_sum + 2 + 6
        # Rock <-> Scissors
        elif splited_item_array[0] == "A" and splited_item_array[1] == "Z":
            total_score_sum = total_score_sum + 3 + 0
        # Rock <-> Rock
        elif splited_item_array[0] == "A" and splited_item_array[1] == "X":
            total_score_sum = total_score_sum + 1 + 3
        # Paper <-> Paper
        elif splited_item_array[0] == "B" and splited_item_array[1] == "Y":
            total_score_sum = total_score_sum + 2 + 3
        # Paper <-> Rock
        elif splited_item_array[0] == "B" and splited_item_array[1] == "X":
            total_score_sum = total_score_sum + 1 + 0
        # Paper <-> Scissors
        elif splited_item_array[0] == "B" and splited_item_array[1] == "Z":
            total_score_sum = total_score_sum + 3 + 6
        # Scissors <-> Rock
        elif splited_item_array[0] == "C" and splited_item_array[1] == "X":
            total_score_sum = total_score_sum + 1 + 6
        # Scissors <-> Paper
        elif splited_item_array[0] == "C" and splited_item_array[1] == "Y":
            total_score_sum = total_score_sum + 2 + 0
        # Scissors <-> Scissors
        elif splited_item_array[0] == "C" and splited_item_array[1] == "Z":
            total_score_sum = total_score_sum + 3 + 3

    return total_score_sum


print(total_score(input_list))
