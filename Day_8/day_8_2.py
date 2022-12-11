input_list = []

with open("input.txt", "r+") as f:
    input_list = [line.replace("\n", "") for line in f]

print(input_list)


def get_scenic_score(input_list, i, j):
    visible_up = 0
    visible_down = 0
    visible_right = 0
    visible_left = 0

    # up
    if i != 0:
        for x in range(i - 1, -1, -1):
            if (input_list[i][j] > input_list[x][j]):
                visible_up += 1
            elif (input_list[i][j] <= input_list[x][j]):
                visible_up += 1
                break

    # down
    if i != (len(input_list) - 1):
        for x in range(i + 1, len(input_list)):
            if (input_list[i][j] > input_list[x][j]):
                visible_down += 1
            elif (input_list[i][j] <= input_list[x][j]):
                visible_down += 1
                break
    # right
    if j != (len(input_list[i]) - 1):
        for x in range(j + 1, len(input_list[0])):
            if (input_list[i][j] > input_list[i][x]):
                visible_right += 1
            elif (input_list[i][j] <= input_list[i][x]):
                visible_right += 1
                break

    # left
    if j != 0:
        for x in range(j - 1, -1, -1):
            if (input_list[i][j] > input_list[i][x]):
                visible_left += 1
            elif (input_list[i][j] <= input_list[i][x]):
                visible_left += 1
                break

    return visible_up * visible_down * visible_right * visible_left


def count_scenic_score(input_list):
    count_scenic_list = []

    for i in range(len(input_list)):
        for j in range(len(input_list[i])):
            count_scenic_list.append(get_scenic_score(input_list, i, j))

    return max(count_scenic_list)


print(count_scenic_score(input_list))
