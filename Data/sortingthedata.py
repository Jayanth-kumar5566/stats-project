'''This code helps to find the market place of highest data final input last value'''
import os
from xml.etree import ElementTree
import xmltodict
from glob import glob
import plotting
from collections import Counter


#folders=["Groundnut","Ladies_Finger","Sugarcane","Tomato"] # Name of the folders 
folders=["Groundnut"]
f=[]
mp_values=dict() #A dic containing market place as a key and arrival dates as a value
Market_place="Srikalahasti"
state="Tamil Nadu"
values=dict()
def dic_append(dic,marketplace,ddate): #takes in dictionary,keys and values 
	if not marketplace in dic:    #it appends the dictionary and keys with different values
		dic[str(marketplace)]=[ddate]
	else:
		dic[str(marketplace)].append(ddate)
	return dic
	
for i in folders:
	globpath = os.path.join(i,'*.xml') #joining the path of only xml files
	filelist = glob(globpath)
	f.append(filelist)
count=0
for i in f:
	for j in i:							#j denotes the file name of the xml file of all the folders 
		tree=ElementTree.parse(str(j))
		root=tree.getroot()
		
		for k in range(len(root[0][0][0][1][0])):
				#print k
				xmldict=xmltodict.XmlDictConfig(root[0][0][0][1][0][k])        #creates an dict with data of kth number
				
				try:
					dic_append(mp_values,xmldict["Market"],xmldict["Arrival_Date"])
				except KeyError:
					dic_append(mp_values,xmldict["Market"],xmldict["Min_x0020_Price"])
					print "error"
					pass
				
				##dic_append(mp_values,xmldict["Market"],xmldict["Arrival_Date"])
				
				if xmldict["Market"]==Market_place:                           #sorts according to market place  
				#if xmldict["State"]==state:										#sorts according to state
					try:	
						values[xmldict["Arrival_Date"]]=xmldict["Modal_x0020_Price"]
						#dic_append(values,xmldict["Arrival_Date"],str(xmldict["Modal_x0020_Price"]))
					except KeyError:
						values[xmldict["Arrival_Date"]]=xmldict["Min_x0020_Price"]
						#dic_append(values,xmldict["Arrival_Date"],str(xmldict["Min_x0020_Price"]))
				else:
					pass
print "length =" ,len(mp_values)
D=mp_values[str(Market_place)]
newVal=len(Counter(D))
Orginal_dates=Counter(D).keys() #a list containig orginal non-recurring dates
Keys=mp_values.keys()
places=dict() 
for i in Keys:
	length=len(mp_values[i])     #this is hashtagged because it contains identical elements so dict elements may contain recurring elements
	places[i]=length			
	#places[i]=newVal			#this creates the below dict()
print places #it contains place name as a key against the number of dates ie len(date)
print sorted(places.items(),key=lambda x:x[1]) #sorts the dict by values in ascending order
print "Total no of dates of "+str(Market_place)+" is ",newVal
refined_values=dict()
for i in Orginal_dates:
	refined_values[i]=values[i]

R=plotting.plt.boxplot([float(i) for i in refined_values.values()])
# -----------------------Finding Outliers -------------------------------------
outliers=R["fliers"][0].get_data()[1]
print "outliers are ", outliers
#----------------Removing Outliers----------------------------------------------
for i in outliers:
	for j in range(len(refined_values.values())):
		if refined_values.values()[j] == i:
			index=j
			key=refined_values.keys()[j]
			del refined_values[key]
		else:
			pass
#------------------------------------------------------------------			
List=plotting.dictolist(refined_values)
plotting.plot(List)
plotting.plt.show()
