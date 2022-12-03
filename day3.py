from get_inputs import GetInputs
from string import ascii_letters

total = 0

data = GetInputs(3).lines()
for line in data:
    assert len(line) % 2 == 0
    halfway = int(len(line) / 2)
    first = line[:halfway]
    second = line[halfway:]
    for char in first:
        if char in second:
            total += ascii_letters.index(char) + 1
            break
print(total)

# pt 2
new_total = 0
for i in range(0, len(data), 3):
    for char in data[i]:
        if char in data[i + 1]:
            if char in data[i + 2]:
                new_total += ascii_letters.index(char) + 1
                break
print(new_total)
