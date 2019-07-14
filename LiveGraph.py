import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')

def animate(i):
	print('here1')

class LiveGraph:
	def __init__(self, plots, figSize, windowSize=2500):

		self.rows = plots[0]
		self.cols = plots[1]
		self.windowSize = windowSize
		self.numPlots = self.rows * self.cols
		self.currentX = []
		self.dataY = []
		self.dataX = []
		self.textList = []
		self.fig = plt.figure(num=None, figsize=figSize, dpi=50, facecolor='w', edgecolor='b')
		self.ax = []
		self.li = []
		self.textInit = []
		for i in range(self.numPlots):
			v = self.fig.add_subplot(self.rows, self.cols,i+1)
			self.ax.append(v)
			liTemp = self.ax[i].plot(0, 0)
			self.li.append(liTemp)
			self.dataY.append(np.empty([0]))
			self.dataX.append(np.empty([0]))
			self.currentX.append(0)
			self.textInit.append(False)
			self.textList.append(None)
		self.fig.canvas.draw()
		plt.show(block=False)


	def plot(self, data, channel=0, color='b', yLabel=" ", xlim=0, ylim=0):
		if hasattr(data, '__len__') and (not isinstance(data, str)):
			pass
		else:
			data = np.array([data])
		self.dataY[channel] = np.concatenate((self.dataY[channel], data))
		if len(self.dataY[channel]) > self.windowSize:
			self.dataY[channel] = self.dataY[channel][-self.windowSize:]
		self.dataX[channel] = np.array(range(0+self.currentX[channel], len(self.dataY[channel])+self.currentX[channel]))
		y = self.dataY[channel]
		self.li[channel][0].set_color(color)
		self.li[channel][0].set_xdata(self.dataX[channel])
		self.li[channel][0].set_ydata(y)
		self.ax[channel].relim()
		self.ax[channel].autoscale_view(True, True, True)
		self.ax[channel].set_xlim(left=0+self.currentX[channel], right= self.windowSize+self.currentX[channel])
		self.ax[channel].set_ylabel(yLabel, fontsize=35, rotation='horizontal', horizontalalignment="right")
		if xlim != 0 and ylim != 0:
			self.ax[channel].set_ylim(xlim, ylim)
		if len(self.dataX[channel]) == self.windowSize :
			self.currentX[channel]+= len(data)


	def setFigureTitle(self, text, size = 20):
		self.fig.suptitle(text, size=size)

	def plotText(self, x= 0.9, y=0.9, size=25, string="text", channel=0):
		if not self.textInit[channel]:
			self.textInit[channel] = True
			self.textList[channel] = plt.text(x, y, string, size = size, va='center', ha='center', transform=self.ax[channel].transAxes)
		else:
			self.textList[channel].set_text(string)

	def draw(self):
		self.fig.canvas.draw()
