import pandas as pd
import numpy as np

d = {"Col1": [2, 9, 4], "Col2": [7, 5, 3], "Col3": [6, 1, 8]}
df = pd.DataFrame(d)
x = df.sum(axis=0, skipna=True)
y = df.sum(axis=1, skipna=True)
df = df.rename_axis("ID").values
z = np.bincount(sum(np.indices(df.shape)).flat, df.flat)
df = np.fliplr(df)
h = np.bincount(sum(np.indices(df.shape)).flat, df.flat)
test1 = int((x.values[0] + x.values[1] + x.values[2]) / 3)
test2 = int((y.values[0] + y.values[1] + y.values[2]) / 3)
test3 = int(z[2])
test4 = int(h[2])

if test1 != test2 or test1 != test3 or test1 != test4 or test2 != test3 or test2 != test4 or test3 != test4:
    print("This is not a magic Square")
    input("Press Enter to exit...")
