input_list = []

with open("input.txt", "r+") as f:
    input_list = [line.replace("\n", "") for line in f]

print(input_list)


def get_signal_strength(input_list):
    final_sum = 0
    cycle = 0
    x = 1
    for item in input_list:
        if "noop" in item:
            cycle += 1
            if ((cycle - 20) % 40) == 0:
                final_sum = final_sum + (cycle * x)
        else:
            value = int(item.split(" ")[1])
            for i in range(0, 2):
                cycle += 1
                if ((cycle - 20) % 40) == 0:
                    final_sum = final_sum + (cycle * x)
                if i == 1:
                    x += value

    return final_sum


print(get_signal_strength(input_list))
