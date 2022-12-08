from get_inputs import GetInputs
import numpy as np
from time import perf_counter

t1 = perf_counter()
data = GetInputs(8).lines()

data_np = np.array([list(line) for line in data]).astype(int)
data_2 = data_np.copy()
flags = np.zeros(np.shape(data_np))
for i in range(4):
    flags = np.rot90(flags)
    data_np = np.rot90(data_np)
    flags[0] = 1
    for i in range(1, len(flags[0])):
        flags[i] = np.maximum(data_np[0] < data_np[i], flags[i])
        data_np[0] = np.maximum(data_np[0], data_np[i])

print(np.sum(np.sum(flags)))
t2 = perf_counter()
print(t2 - t1)  # 5.8 ms
...
# part 2. start from scratch i guess

t3 = perf_counter()
score_flags = np.zeros(np.shape(data_2))

for i in range(data_2.shape[0]):
    for j in range(data_2.shape[1]):
        scores = [0, 0, 0, 0]
        x = i + 1
        while x < data_2.shape[0]:
            scores[0] += 1
            if data_2[x, j] >= data_2[i, j]:
                break
            x += 1
        x = i - 1
        while x >= 0:
            scores[1] += 1
            if data_2[x, j] >= data_2[i, j]:
                break
            x -= 1
        x = j + 1
        while x < data_2.shape[1]:
            scores[2] += 1
            if data_2[i, x] >= data_2[i, j]:
                break
            x += 1
        x = j - 1
        while x >= 0:
            scores[3] += 1
            if data_2[i, x] >= data_2[i, j]:
                break
            x -= 1
        score_flags[i, j] = np.prod(scores)

print(np.max(score_flags))
t4 = perf_counter()
print(t4 - t3)  # 100.0 ms
