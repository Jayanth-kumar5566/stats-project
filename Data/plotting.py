import datetime
import matplotlib.pyplot as plt
from matplotlib.dates import date2num
def dictolist(x):
	return [x.keys(),x.values()] #a list contaning x(Date) and y(price) values as a list
def plot(List):
	x=[]
	y=[]
	Date=[]
	for i in range(len(List[0])):
		daate=datetime.datetime.strptime(List[0][i],"%d/%m/%Y")
		Date.append(daate)
		daates=date2num(daate)
		x.append(daates)
		y.append(float(List[1][i]))
	fig = plt.figure()
	graph = fig.add_subplot(111)
	graph.plot(x,y,'ro')
	graph.set_xticks(x)
	graph.set_xticklabels(Date)
	return plt.show()
	
		
