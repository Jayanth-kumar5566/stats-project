'''This code helps to find the market place of highest data final input last value'''
import os
from xml.etree import ElementTree
import xmltodict
from glob import glob
import plotting


#folders=["Groundnut","Ladies_Finger","Sugarcane","Tomato"] # Name of the folders 
folders=["Groundnut"]
f=[]
mp_values=dict() #A dic containing market place as a key and arrival dates as a value
Market_place="Anantapur"
state="Madhya Pradesh"
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
for i in f:
	for j in i:							#j denotes the file name of the xml file of all the folders 
		tree=ElementTree.parse(str(j))
		root=tree.getroot()
		for k in range(len(root[0][0][0][1][0])):
				#print k
				xmldict=xmltodict.XmlDictConfig(root[0][0][0][1][0][k])        #creates an dict with data of kth number
				#print xmldict
				dic_append(mp_values,xmldict["Market"],xmldict["Arrival_Date"])
				#if xmldict["Market"]==Market_place:                           #sorts according to market place  
				if xmldict["State"]==state:										#sorts according to state
						values[xmldict["Arrival_Date"]]=xmldict["Modal_x0020_Price"]
						
				else:
					pass
print "length =" ,len(mp_values)
Keys=mp_values.keys()
places=dict() 
for i in Keys:
	length=len(mp_values[i])
	places[i]=length
print places #it contains place name as a key against the number of dates ie len(date)
print sorted(places.items(),key=lambda x:x[1]) #sorts the dict by values in ascending order

#List=plotting.dictolist(values)

#plotting.plot(List)

