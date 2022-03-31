import os
from xml.etree import ElementTree
import xmltodict
from glob import glob
import plotting
import sortingthedata

#folders=["Groundnut","Ladies_Finger","Sugarcane","Tomato"] # Name of the folders 
folders=["Groundnut"]
f=[]
Market_place="Srikalahasti"
state="Madhya Pradesh"
values=dict()
mp_values=dict()
	
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
				
				if xmldict["Market"]==Market_place and xmldic["Arrival_Date"]==l:                           #sorts according to market place  
				#if xmldict["State"]==state:										#sorts according to state
					for l in sortingthedata.Orginal_dates:	
						try:
							values[xmldict[l]]=xmldict["Modal_x0020_Price"]
						except KeyError:
							print l
							values[xmldict[l]]=xmldict["Min_x0020_Price"] 
							pass
						
				else:
					pass

List=plotting.dictolist(values)

plotting.plot(List)

