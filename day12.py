import numpy as np
from get_inputs import GetInputs
from string import ascii_lowercase

data = GetInputs(12).lines()
ascii = ascii_lowercase + "E..S"
data_np = np.array([[ascii.index(x)+1 for x in list(line)] for line in data])
distance = np.full(np.shape(data_np),np.inf)
visited = np.zeros(np.shape(data_np))
dataset = np.stack((data_np,distance,visited,distance))

# unvisited = []
# for i in range(np.shape(data_np)[0]):
#     for j in range(np.shape(data_np)[0]):
#         unvisited.append((i,j))
start = tuple(np.argwhere(dataset[0]==30)[0])
dataset[0][start] = 1
dataset[1][start] = 0

moveset = [(0,1),(0,-1),(1,0),(-1,0)]
first_iteration=0
while True:
    cur_node = np.unravel_index(dataset[3].argmin(), dataset[3].shape)
    if first_iteration == 0:
        cur_node = start
        first_iteration=1
    print(cur_node)
    if dataset[0][cur_node] == 27:
        break
    for direction in moveset:
        visiting = cur_node[0]+direction[0],cur_node[1]+direction[1]
        if not any(np.array(visiting)<0) and not visiting[0] >= np.shape(dataset[0])[0] and not visiting[1] >= np.shape(dataset[0])[1]:
            if dataset[2][visiting]==0 and dataset[0][visiting]<=dataset[0][cur_node]+1:
                dataset[1][visiting] = dataset[1][cur_node]+1
                dataset[3][visiting]=dataset[1][visiting]
    dataset[2][cur_node]=1
    dataset[3][cur_node]=np.inf
print(dataset[1][tuple(np.argwhere(dataset[0]==27)[0])])
