"""
In addition to horizontal position and depth, you'll also need to track a 
third value, aim, which also starts at 0

# New rules
down X increases your aim by X units.
up X decreases your aim by X units.
forward X does two things:
    It increases your horizontal position by X units.
    It increases your depth by your aim multiplied by X.

# Test case with new rules
horizontal position of 15
depth of 60
Multiplying these produces 900

"""

x_pos = 0
y_pos = 0
aim   = 0

with open("/Users/dcowden/Repos/acvent_of_code/2021/2a.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        command = line.split()[0]
        value = int(line.split()[1])

        match command:
            case "forward":
                x_pos += value
                y_pos = y_pos + (aim * value)
            case "up":
                aim -= value
            case "down":
                aim += value

coordinate = x_pos * y_pos

print(coordinate)
