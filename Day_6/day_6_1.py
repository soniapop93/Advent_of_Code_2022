input_list = []

with open("input.txt", "r+") as f:
    input_list = [line.replace("\n", "") for line in f]

print(input_list)


def identify_start_of_packet_marker(input_list):
    for item in input_list:
        for i in range(0, len(item)):
            if (item[i] == item[i + 1]) or (item[i] == item[i + 2]) or (item[i] == item[i + 3]) or \
                    (item[i + 1] == item[i + 2]) or (item[i + 1] == item[i + 3]) or (item[i + 2] == item[i + 3]):
                continue
            return i + 4


print(identify_start_of_packet_marker(input_list))
