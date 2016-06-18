import sortingthedata
import datetime
import matplotlib.pyplot as plt
import numpy as np
dates=[] 

# make dates to have elements in datetime format
for i in sortingthedata.Orginal_dates:
	dates.append(datetime.datetime.strptime(i,"%d/%m/%Y"))
#creating a months and year list
months=range(1,13)
#year=range(2001,2017)  #Uncomment this line for other commodities other than groundnut
year=range(2008,2016)
finaldic=dict()
monthdates_dic=dict()
#Looping and adding values to a dict
def Dicc(Year,dates,months):
	monthdates_dic=dict()
	for k in months:
			for i in dates:
				if i.year == Year :
					a=sortingthedata.dic_append(monthdates_dic,str(i.month),sortingthedata.refined_values[str(i.strftime("%d/%m/%Y"))])
					print i , i.month 				
				else:
					pass			
	return monthdates_dic
for j in year:
	a=Dicc(j,dates,months)
	finaldic[j]=a#(monthdates_dic[k]=i)
#------------------------Fixing of missing data in finaldic------------------------------------------------------------------
def linfun(y,m):
	return 27.3373*((y*12)+m)-6.55869e+5
finaldic[2012]['9']=5884.335
finaldic[2012]['10']=5685.667
#-----------------------------------------------------------------------------------------------------------------------------			
def average(List):
	return reduce(lambda x, y: x + y, List) / float(len(List))							
#Averaging over the Values of a month
dash=dict()

for i in sorted(finaldic.keys()):
	for j in sorted(finaldic[i].keys()):
		try:
			a=average([float(k)for k in finaldic[i][str(j)]])
		except TypeError:
			a=finaldic[i][str(j)]
		print (i,j,a)
		dash[(int(i)*12)+int(j)]=a
		#except KeyError:
			#pass

x=dash.keys()
y=dash.values()
#plt.plot(x,y,'ro')
#plt.show()
