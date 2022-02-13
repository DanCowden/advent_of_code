"""
This solution is working up to a 5 digit binary number but probalby not a good
solution to scale it up to the required 12.  View next solution instead using Pandas

The first parameter to check is the power consumption

use the binary numbers in the diagnostic report to generate two new binary numbers
    gamma rate
    epsilon rate

power consumption = gamma rate * epsilon rate

ach bit in the gamma rate can be determined by finding the most common bit in the 
corresponding position of all numbers in the diagnostic report

epsilon rate is teh opposite of gamma rate (least common bit in each position)

Be sure to represent your answer in decimal, not binary

3a.txt
gamma rate is the binary number 10110, or 22 in decimal
epsilon rate is 01001, or 9 in decimal
22 * 9 = 198
"""

from collections import Counter

first_bits  = []
second_bits = []
third_bits  = []
fourth_bits = []
fifth_bits  = []

with open("/Users/dcowden/Repos/acvent_of_code/2021/3.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        first_bits.append(line[0])
        second_bits.append(line[1])
        third_bits.append(line[2])
        fourth_bits.append(line[3])
        fifth_bits.append(line[4])

first_bit = Counter(first_bits)
first_bit = first_bit.most_common(1)[0][0]

second_bit = Counter(second_bits)
second_bit = second_bit.most_common(1)[0][0]

third_bit = Counter(third_bits)
third_bit = third_bit.most_common(1)[0][0]

fourth_bit = Counter(fourth_bits)
fourth_bit = fourth_bit.most_common(1)[0][0]

fifth_bit = Counter(fifth_bits)
fifth_bit = fifth_bit.most_common(1)[0][0]

gamma_rate_str = first_bit + \
    second_bit + \
    third_bit + \
    fourth_bit + \
    fifth_bit
gamma_rate = int(gamma_rate_str, base=2)

epsilon_rate_str = ''.join('1' if x == '0' else '0' for x in gamma_rate_str)
epsilon_rate = int(epsilon_rate_str, base=2)

power_consumption = gamma_rate * epsilon_rate
print(power_consumption)
