from get_inputs import GetInputs
import re

data = GetInputs(4).lines()
total = 0
total_part2 = 0
for line in data:
    ranges = [int(s) for s in re.findall(r'\d+', line)]
    assert(ranges[0] <= ranges[1])
    assert(ranges[2] <= ranges[3])
    if ranges[0] == ranges[2]:
        total+=1
    elif ranges[0] < ranges[2]:
        if ranges[1] >= ranges[3]:
            total+=1
    elif ranges[0] > ranges[2]:
        if ranges[1] <= ranges[3]:
            total+=1
    # part 2
    if ranges[0] == ranges[2]:
        total_part2 += 1
    elif ranges[0] < ranges[2]:
        if ranges[1] >= ranges[2]:
            total_part2 += 1
    elif ranges[0] > ranges[2]:
        if ranges[0] <= ranges[3]:
            total_part2 += 1

print(total)
print(total_part2)

