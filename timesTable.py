import matplotlib.pyplot as plt
import numpy as np

class plot:
	def __init__(self,num,multiplier,pauseInt=0.05):
		self.num = num
		self.multiplier = multiplier
		self.pauseInt = pauseInt
		theta = np.arange(np.pi, -2*np.pi, -2*np.pi/num)
		self.pts = {'x': np.cos(theta), 'y': np.sin(theta)}
		self.fig, self.ax = plt.subplots()

	def plot_fx(self,x,multiplier=None):
		if multiplier is None:
			multiplier = self.multiplier
		fx = (x*multiplier)%self.num
		self.ax.plot([self.pts['x'][x], self.pts['x'][fx]], [self.pts['y'][x], self.pts['y'][fx]] )
		#self.ax.annotate(str(x), [self.pts['x'][x],self.pts['y'][x]])

	def slow_plot(self):
		self.ax.set_title("Number:"+str(self.num)+" Multiplier: "+str(self.multiplier))
		for x in range(0,self.num):
			self.plot_fx(x,self.multiplier)
			plt.pause(self.pauseInt)
		plt.show()

	def multiplierInc_plot(self,limit):
		print("Table: "+ str(self.num))
		for multiplier in range(self.multiplier,limit):
			for x in range(0,self.num):
				self.plot_fx(x,multiplier)
			self.ax.set_title("Number:"+str(self.num)+" Multiplier: "+str(multiplier))
			print("->" + str(self.num) + " x " + str(multiplier))
			plt.pause(self.pauseInt)
			plt.cla()
				

#NOTE: Use only either of slow_plot or multiplierInc_plot for every instance of plot
#plot(100,2,0.001).slow_plot()
plot(100,2,0.001).multiplierInc_plot(200)
