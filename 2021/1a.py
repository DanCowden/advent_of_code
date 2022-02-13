with open("/Users/dcowden/Repos/acvent_of_code/2021/1.txt", "r") as f:
    depths: list = [int(x) for x in f.readlines()]

count: int = 0

for index, value in enumerate(depths):
    try:
        if depths[index + 1] + \
            depths[index + 2] + \
            depths[index + 3] > \
            depths[index] + \
            depths[index + 1] + \
            depths[index + 2]:
                count += 1
    except IndexError:
        pass

print(count)
