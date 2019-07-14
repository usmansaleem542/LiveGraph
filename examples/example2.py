import sys
sys.path.append("../")
import pandas as pd
from LiveGraph import LiveGraph

lg = LiveGraph(plots=[2,1], figSize=(20, 10), windowSize=1000)
col = {'blue': '#1f77b4', 'orange': '#ff7f0e', 'green': '#2ca02c', 'red': '#d62728'}


for gm_chunk in pd.read_csv('100.csv',chunksize=1):
    lg.plot(data=gm_chunk['MLII'], channel=0, color='red', yLabel='MLII')
    lg.plot(data=gm_chunk['V5'], channel=1, color='blue', yLabel='V5')
    lg.draw()