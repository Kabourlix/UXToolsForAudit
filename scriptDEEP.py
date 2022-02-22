import matplotlib.pyplot
import plotly.express as px
import pandas as pd
import sys

#Importing the file
if len(sys.argv) == 1:
    print("Not enough argument.")
    exit()

filepath = sys.argv[1]
df = pd.read_csv(filepath)
#########################

#inversion des scores 12 et 15
df.iloc[:, 12] = 6 - df.iloc[:, 12]
df.iloc[:, 15] = 6 - df.iloc[:, 15]

area = []
area.append(df.iloc[:, 1:5])  #content
area.append(df.iloc[:, 5:8]) #structure
area.append(df.iloc[:, 8:11]) #navigation
area.append(df.iloc[:, 11:14]) #cognitive effort
area.append(df.iloc[:, 14:17]) #coherence
area.append(df.iloc[:, 17:]) #visual guiding

meanPerArea = []
for table in area:
    meanPerArea.append(table.mean().sum()/len(table.columns))

radar = pd.DataFrame(dict(
    r=meanPerArea,
    theta=["content", "structure", "navigation", "cognitive effort", "coherence", "visual guiding"]
))

fig = px.line_polar(radar, r='r', theta='theta', line_close=True)
fig.show()

