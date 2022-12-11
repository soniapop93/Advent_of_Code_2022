input_list = []

with open("input.txt", "r+") as f:
    input_list = [line.replace("\n", "") for line in f]

print(input_list)


def check_if_tree_is_visible(input_list, i, j):
    visible_up = True
    visible_down = True
    visible_right = True
    visible_left = True

    if i == 0 or i == (len(input_list) - 1) or j == 0 or j == (len(input_list[i]) - 1):
        return True

    # up
    for x in range(i - 1, -1, -1):
        if (input_list[i][j] <= input_list[x][j]):
            visible_up = False
            break

    # down
    for x in range(i + 1, len(input_list)):
        if (input_list[i][j] <= input_list[x][j]):
            visible_down = False
            break

    # right
    for x in range(j + 1, len(input_list[0])):
        if (input_list[i][j] <= input_list[i][x]):
            visible_right = False
            break

    # left
    for x in range(j - 1, -1, -1):
        if (input_list[i][j] <= input_list[i][x]):
            visible_left = False
            break

    if visible_up or visible_down or visible_left or visible_right:
        return True

    return False


def count_trees_visible(input_list):
    tree_count = 0

    for i in range(len(input_list)):
        for j in range(len(input_list[i])):
            if check_if_tree_is_visible(input_list, i, j):
                tree_count += 1

    return tree_count


print(count_trees_visible(input_list))
