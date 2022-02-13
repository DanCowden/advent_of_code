count = 0
current_list = []
past_sum = 0

with open("/Users/dcowden/Repos/acvent_of_code/2021/1.txt", "r") as f:
    numbers = f.readlines()
    for index, number in enumerate(numbers):
        current_list.append(int(number))
        if len(current_list) == 3:
            current_sum = sum(current_list)

            if past_sum > 0:
                if current_sum > past_sum:
                    count += 1

            past_sum = current_sum
            current_list = []

print(count)
