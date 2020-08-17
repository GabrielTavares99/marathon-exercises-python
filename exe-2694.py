import re

rounds = input()
for round_index in range(int(rounds)):
    line = input()
    numbers = re.compile("(\\d+)").findall(line)
    sum_count = 0
    for number in numbers:
        sum_count += int(number)
    print(sum_count)
