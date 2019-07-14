import sys
sys.path.append("../")
from LiveGraph import LiveGraph
import numpy as np

lg = LiveGraph(plots=[1,1], figSize=(20, 10), windowSize=500)
col = {'blue': '#1f77b4', 'orange': '#ff7f0e', 'green': '#2ca02c', 'red': '#d62728'}

sineWave = np.sin(np.linspace(0, 50 * np.pi, 3000))

for i in range(len(sineWave)):
    lg.plot(data=sineWave[i], channel=0, color='red', yLabel="ylabel")
    lg.draw()


