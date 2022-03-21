import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import pandas as pd
import sys

#Importing the file
if len(sys.argv) == 1:
    print("Not enough argument.")
    exit()

filepath = sys.argv[1]
df = pd.read_csv(filepath).iloc[:,1:-1] #We get rid of the last column.
#Convert all score in an range between -3 and 3.
df.iloc[:, :] = 6 - df.iloc[:, :]
df = df.mean() #We only get interest in the mean for each question.

#########################

QP = df.iloc[:8] #qualité pragmatique (QP)
QHS = df.iloc[8:15] #qualité hédonique-stimulation (QH-S)
QHI = df.iloc[15:22] #qualité hédonique-identité (QH-I)
QG = df.iloc[22:] #qualité globale (QG)

def portfolioResult():
    print("We get in portfolio")
    meanQP = QP.mean()
    meanQHS = QHS.mean()
    meanQHI = QHI.mean()
    meanQH = (meanQHS + meanQHI)/2
    plt.figure()
    plt.plot(meanQP, meanQH, 'o')
    x = np.linspace(-3,3,1000)
    plt.plot(x,np.zeros(1000)+1,color="black")
    plt.plot(x,np.zeros(1000)+3,color="black")
    plt.plot(x,np.zeros(1000)-1,color="black")
    plt.plot(np.zeros(1000)+1,x,color="black")
    plt.plot(np.zeros(1000)+3,x,color="black")
    plt.plot(np.zeros(1000)-1,x,color="black")
    plt.plot(np.zeros(1000)-3,x,color="black")
    plt.plot(x,np.zeros(1000)-3,color="black")

    plt.xlabel("QP")
    plt.ylabel("QH")
    plt.savefig("img/portfolio.png")
    plt.show()

def printDiagMoyenne(meanTab):
    plt.plot([1,2,3,4],meanTab)
    plt.plot([1,2,3,4],meanTab,'o')
    plt.xlim(0.9,4.1)
    plt.ylim(-3,3)
    #Modify label so as to get QP QHS QHI and QG
    plt.xticks([1,2,3,4],["QP","QHS","QHI","QG"])

    #Add a green rectangle that cover area from y = 1 to 2
    plt.gca().add_patch(plt.Rectangle((0,1),4.1,1,color="green",alpha=0.2))
    #Same but in dark green
    plt.gca().add_patch(plt.Rectangle((0,2),4.1,1,color="green",alpha=0.5))

    #Add a red rectangle that cover area from y = -1 to -2
    plt.gca().add_patch(plt.Rectangle((0,-2),4.1,1,color="red",alpha=0.2))
    #Same but in dark red
    plt.gca().add_patch(plt.Rectangle((0,-3),4.1,1,color="red",alpha=0.5))

    plt.savefig("img/diagMoyenne.png")
    plt.show()

def diagMoyenne():
    print("We get in diagMoyenne")
    meanQP = QP.mean()
    meanQHS = QHS.mean()
    meanQHI = QHI.mean()
    meanQG = QG.mean()
    

#portfolioResult()
printDiagMoyenne([-0.05,-0.9,0,-0.81])