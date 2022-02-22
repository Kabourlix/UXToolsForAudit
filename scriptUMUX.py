import pandas as pd
import sys


#Importing the file
if len(sys.argv) == 1:
    print("Not enough argument.")
    exit()

filepath = sys.argv[1]
df = pd.read_csv(filepath)
#########################

#Formula : 0.65 * (UMUX1 + UMUX2 - 2) * (100/12) + 22.9

df["susEq"] = 0.65*(df.iloc[:, 1] + df.iloc[:, 2] - 2) * (100/12) + 22.9

susSCORE = df["susEq"].mean()

print(susSCORE)