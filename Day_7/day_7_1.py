input_list = []

with open("input.txt", "r+") as f:
    input_list = [line.replace("\n", "") for line in f]

print(input_list)


def sum_of_total_directories(input_list):
    path = ""
    dict_of_paths = {}

    count = -1
    for item in input_list:
        count += 1
        if "$" in item:
            if "cd " in item:
                if "cd /" in item:
                    path = "/"
                elif "cd .." in item:
                    splited_path = path.split("/")[:-2]
                    path = "/".join(splited_path) + "/"
                else:
                    path = path + item.split("cd ")[1] + "/"
                if path not in dict_of_paths.keys():
                    dict_of_paths[path] = 0
            elif " ls" in item:
                folder_size = 0
                for i in range(count + 1, len(input_list)):
                    if "$" in input_list[i]:
                        break
                    elif "dir " not in input_list[i]:
                        size_item = input_list[i].split(" ")[0]
                        folder_size += int(size_item)
                for key in dict_of_paths.keys():
                    if key in path:
                        dict_of_paths[key] += folder_size

    sum_size = 0
    for key in dict_of_paths.keys():
        if dict_of_paths[key] <= 100000:
            sum_size += dict_of_paths[key]

    return sum_size


print(sum_of_total_directories(input_list))
