import os
from xml.etree import ElementTree
import xmltodict
from glob import glob
import plotting


#folders=["Groundnut","Ladies_Finger","Sugarcane","Tomato"] # Name of the folders 
folders=["Groundnut"]
f=[]
Market_place="SriKalahasti"
state="Madhya Pradesh"
values=dict()
	
for i in folders:
	globpath = os.path.join(i,'*.xml') #joining the path of only xml files
	filelist = glob(globpath)
	f.append(filelist)
for i in f:
	for j in i:							#j denotes the file name of the xml file of all the folders 
		tree=ElementTree.parse(str(j))
		root=tree.getroot()
		for k in range(len(root[0][0][0][1][0])):
				print k
				xmldict=xmltodict.XmlDictConfig(root[0][0][0][1][0][k])        #creates an dict with data of kth number
				print xmldict
				
				if xmldict["Market"]==Market_place:                           #sorts according to market place  
				#if xmldict["State"]==state:										#sorts according to state
						values[xmldict["Arrival_Date"]]=xmldict["Modal_x0020_Price"]
						
				else:
					pass

List=plotting.dictolist(values)

plotting.plot(List)

