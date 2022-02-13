"""
forward X increases the horizontal position by X units.
down X increases the depth by X units.
up X decreases the depth by X units.

Your horizontal position and depth both start at 0

forward 5 adds 5 to your horizontal position, a total of 5.
down 5 adds 5 to your depth, resulting in a value of 5.
forward 8 adds 8 to your horizontal position, a total of 13.
up 3 decreases your depth by 3, resulting in a value of 2.
down 8 adds 8 to your depth, resulting in a value of 10.
forward 2 adds 2 to your horizontal position, a total of 15.

At th eend, you have a horizontal position of 15 and a depth of 10
(Multiplying these together produces 150.)
"""

x_pos = 0
y_pos = 0

with open("/Users/dcowden/Repos/acvent_of_code/2021/2a.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        command = line.split()[0]
        value = int(line.split()[1])

        if command == "forward":
            x_pos += value

        if command == "up":
            y_pos -= value

        if command == "down":
            y_pos += value

coordinate = x_pos * y_pos

print(coordinate)
