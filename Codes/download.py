import os
import urllib2
lf_url=["https://data.gov.in/sites/default/files/Bhindi(Ladies_Finger)_2001-2002.xml",]
Sugar_url=["https://data.gov.in/sites/default/files/Sugarcane_as_on_date.xml"]
Ground_url=["https://data.gov.in/sites/default/files/Groundnut_(Split)_2001-2012.xml"]
Tomato_url=[]
url1="https://data.gov.in/sites/default/files/Bhindi(Ladies_Finger)_"
url2="https://data.gov.in/sites/default/files/Groundnut_(Split)_"
url3="https://data.gov.in/sites/default/files/Sugarcane_"
url4="https://data.gov.in/sites/default/files/Tomato_"
year=range(2001,2016)
for i in year:
	lf_url.append(url1+str(i)+".xml")
	Ground_url.append(url2+str(i)+".xml")
	Sugar_url.append(url3+str(i)+".xml")
	Tomato_url.append(url4+str(i)+".xml")
filenames=[["Groundnut",Ground_url],["Ladies_Finger",lf_url],["Sugarcane",Sugar_url],["Tomato",Tomato_url]]

for i in filenames:
	
	os.system("mkdir"+i[0]+"/"")
	os.chdir(i[0]+"/")	
	count=0
	print i
	print count
	for j in i[1]:
		f=open(str(count)+".xml","w")
		try:
			xml_file=urllib2.urlopen(j)
			a=xml_file.read()
		except urllib2.HTTPError:
			pass
		except httplib.IncompleteRead:
			xml_file=urllib2.urlopen(j)
			a=xml_file.read()
		count=count+1
		f.write(a)
		f.close()
		print j
		print "Done"+str(count)
