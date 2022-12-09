from get_inputs import GetInputs
import numpy as np


def move_head(arr, direction):
    match direction:
        case "U":
            return arr + np.array([0, 1])
        case "D":
            return arr + np.array([0, -1])
        case "R":
            return arr + np.array([1, 0])
        case "L":
            return arr + np.array([-1, 0])
        case _:
            raise Exception("no direction")


def move_tail(head, tail):
    diff = head - tail
    if np.sum(np.abs(diff)) > 2:
        return tail + np.sign(diff)
    if np.sum(np.abs(diff)) == 2 and not all(np.abs(diff) == np.array([1, 1])):
        return tail + np.sign(diff)
    return tail


data = GetInputs(9).lines()
positions = {(0, 0)}
pos_h = np.array([0, 0])
pos_t = np.array([0, 0])


for line in data:
    inputs = line.split()
    for _ in range(int(inputs[1])):
        pos_h = move_head(pos_h, inputs[0])
        pos_t = move_tail(pos_h, pos_t)
        positions.add(tuple(pos_t))
print(len(positions))

# part 2

positions = {(0, 0)}
pos_snake = np.array(
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
)

for line in data:
    inputs = line.split()
    for _ in range(int(inputs[1])):
        pos_snake[0] = move_head(pos_snake[0], inputs[0])
        for i in range(1, 10):
            pos_snake[i] = move_tail(pos_snake[i - 1], pos_snake[i])
        positions.add(tuple(pos_snake[9]))
print(len(positions))
