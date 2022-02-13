import pandas as pd

with open('/Users/dcowden/Repos/acvent_of_code/2021/3.txt', 'r') as f:
    binary_digits: list = f.readlines()

# Convertijng list of binary strings into a lis of lists where the inner list
# is a list of each character in the original binary string element
for i, num in enumerate(binary_digits):
    binary_digits[i] = [int(x) for x in num.strip()]

gamma_rate_str   = ''
epsilon_rate_str = ''

df = pd.DataFrame(binary_digits)

# Each binary number string has 12 characters
for i in range(0, 12):
    gamma_rate_str   += str(df[i].value_counts().idxmax())
    epsilon_rate_str += str(df[i].value_counts().idxmin())

# Convert string into integar of the equivalent binary number
gamma_rate = int(gamma_rate_str, base=2)
epsilon_rate = int(epsilon_rate_str, base=2)
power_consumption = gamma_rate * epsilon_rate
print(power_consumption)
