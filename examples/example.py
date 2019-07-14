from LiveGraph import LiveGraph
import numpy as np

lg = LiveGraph(plots=[2,2], figSize=(20, 10), maxWindow=1000)
col = {'blue': '#1f77b4', 'orange': '#ff7f0e', 'green': '#2ca02c', 'red': '#d62728'}

sineWave = np.sin(np.linspace(0, 50 * np.pi, 3000))

for i in range(len(sineWave)):
    lg.plot(data=sineWave[i], channel=0, color='red')
    lg.plot(data=sineWave[i], channel=1, color='blue')
    lg.plot(data=sineWave[i], channel=2, color='green')
    lg.plot(data=sineWave[i], channel=3, color='orange')
    lg.draw()


