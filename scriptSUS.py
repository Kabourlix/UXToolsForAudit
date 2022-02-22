import numpy as np
import pandas as pd
import sys

#Importing the file
if len(sys.argv) == 1:
    print("Not enough argument.")
    exit()

filepath = sys.argv[1]
df = pd.read_csv(filepath)
#########################

print(df.head())
df["score"] = 0
columnsName = df.columns
for i in range(1, len(columnsName)-1):
    if i % 2 == 1: #impair
        df["score"] += df[columnsName[i]] - 1
    else:
        df["score"] += 5 - df[columnsName[i]]

df["score"] *= 2.5

SUSScore = df["score"].mean() #We get the sus score

print(SUSScore)

