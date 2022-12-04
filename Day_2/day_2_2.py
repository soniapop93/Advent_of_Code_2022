input_list = []

with open("input.txt", "r+") as f:
    input_list = [line.replace("\n", "") for line in f]

print(input_list)


def total_score(input_list):
    # A -> Rock, 1
    # B -> Paper, 2
    # C -> Scissors, 3
    # 6 -> it's a win
    # X -> Lose
    # Y -> Draw
    # Z -> Win

    total_score_sum = 0
    for item in input_list:
        splited_item = item.split(" ")

        # Rock <-> Draw, Rock
        if splited_item[0] == "A" and splited_item[1] == "Y":
            total_score_sum = total_score_sum + 1 + 3
        # Rock <-> Lose, Scissors
        elif splited_item[0] == "A" and splited_item[1] == "X":
            total_score_sum = total_score_sum + 3 + 0
        # Rock <-> Win, Paper
        elif splited_item[0] == "A" and splited_item[1] == "Z":
            total_score_sum = total_score_sum + 2 + 6
        # Paper <-> Lose, Rock
        elif splited_item[0] == "B" and splited_item[1] == "X":
            total_score_sum = total_score_sum + 1 + 0
        # Paper <-> Draw, Paper
        elif splited_item[0] == "B" and splited_item[1] == "Y":
            total_score_sum = total_score_sum + 2 + 3
        # Paper <-> Win, Scissors
        elif splited_item[0] == "B" and splited_item[1] == "Z":
            total_score_sum = total_score_sum + 3 + 6
        # Scissors <-> Lose, Paper
        elif splited_item[0] == "C" and splited_item[1] == "X":
            total_score_sum = total_score_sum + 2 + 0
        # Scissors <-> Win, Scissors
        elif splited_item[0] == "C" and splited_item[1] == "Y":
            total_score_sum = total_score_sum + 3 + 3
        # Scissors <-> Draw, Rock
        elif splited_item[0] == "C" and splited_item[1] == "Z":
            total_score_sum = total_score_sum + 1 + 6

    return total_score_sum


print(total_score(input_list))
