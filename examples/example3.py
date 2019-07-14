import sys
sys.path.append("../")

from LiveGraph import LiveGraph
import pandas as pd
import random


lg = LiveGraph(plots=[2,1], figSize=(20, 10), windowSize=1000)
col = {'blue': '#1f77b4', 'orange': '#ff7f0e', 'green': '#2ca02c', 'red': '#d62728'}
lg.setFigureTitle("FIGURE TITLE")

for gm_chunk in pd.read_csv('100.csv',chunksize=4):
    lg.plot(data=gm_chunk['MLII'], channel=0, color='red', yLabel='MLII')
    lg.plot(data=gm_chunk['V5'], channel=1, color='blue', yLabel='V5')
    lg.plotText(string="HR: "+ str(random.randint(67,70)), channel=0)       #generating random HR
    lg.plotText(string="♥ "+ str(random.randint(67,70)), channel=1, size=50, x=0.5, y=0.5)   #generating random HR
    lg.draw()
    print("print after draw")