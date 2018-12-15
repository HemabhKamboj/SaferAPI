import numpy as np
import pandas as pd

from scipy import spatial

df = pd.read_csv('data/loc_data.csv')

X = df[["Latitude", "Longitude"]].values

def get_index(pt):
    x = X[spatial.KDTree(X).query(pt)[1]]
    # print(x)
    index = df.loc[( df["Longitude"] == x[1]) & (df["Latitude"] == x[0] ) ]["Danger_index"]
    # print("index",index)
    return index.values[0]

def final_index(path):
    sum = 0
    for pt in path:
        # print(pt)
        sum += get_index(pt)
        # print(get_index(pt))
    
    index = round(sum/len(path),4)
    # print(index)
    return index

