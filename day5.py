import re

from get_inputs import GetInputs

data = GetInputs(5).lines()

input_blocks = data[0:8]
input_blocks.reverse()
towers = [[],[],[],[],[],[],[],[],[],[]]

for line in input_blocks:
    for tower, char in enumerate(range(1,34,4)):
        if line[char] != " ":
            towers[tower+1].append(line[char])
print(towers)

for line in data[10:]:
    print(line)
    move_from_to = [int(s) for s in re.findall(r'\d+', line)]
    assert (len(move_from_to) == 3)
    (move, frm, to) = move_from_to
    assert(len(towers[frm]) >= move)
    towers[to].extend(towers[frm][-move:])
    del towers[frm][-move:]

outcome = ""
for tower in towers:
    if len(tower)>0:
        outcome += str(tower[-1])
print(outcome)