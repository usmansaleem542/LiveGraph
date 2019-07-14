import sys
sys.path.append("../")
from LiveGraph import LiveGraph
import numpy as np

lg = LiveGraph(plots=[2,2], figSize=(20, 10), windowSize=1000)
col = {'blue': '#1f77b4', 'orange': '#ff7f0e', 'green': '#2ca02c', 'red': '#d62728'}

sineWave = np.sin(np.linspace(0, 50 * np.pi, 3000))

for i in range(len(sineWave)):
    lg.plot(data=sineWave[i], channel=0, color='red', yLabel="1")
    lg.plot(data=sineWave[i], channel=1, color='blue', yLabel="2")
    lg.plot(data=sineWave[i], channel=2, color='green', yLabel="3")
    lg.plot(data=sineWave[i], channel=3, color='orange', yLabel="4")
    lg.draw()


