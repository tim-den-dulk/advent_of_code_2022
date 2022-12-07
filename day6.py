from get_inputs import GetInputs
import numpy as np
import pandas as pd

data = GetInputs(6).lines()[0]

data_np = np.array(list(data))
data_pd = pd.DataFrame(data_np)
data_pd["shift1"] = data_pd[0].shift(1)
data_pd["shift2"] = data_pd[0].shift(2)
data_pd["shift3"] = data_pd[0].shift(3)
data_pd["eq1"] = data_pd[0] == data_pd["shift1"]
data_pd["eq2"] = data_pd[0] == data_pd["shift2"]
data_pd["eq3"] = data_pd[0] == data_pd["shift3"]
data_pd["eq4"] = data_pd['shift1'] == data_pd["shift2"]
data_pd["eq5"] = data_pd['shift1'] == data_pd["shift3"]
data_pd["eq6"] = data_pd['shift2'] == data_pd["shift3"]
data_pd["sum"] = data_pd.iloc[:,4:].any(axis=1)
res = data_pd.loc[5:,"sum"].idxmin()
print(res)
...

# more efficient solution for part 2
for i in range(len(data_np)-14):
    if len(np.unique(data_np[i:i+14])) == 14:
        print(data_np[i:i + 14])
        print(i+14)
        break
