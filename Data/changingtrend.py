import cleaning
import matplotlib.pyplot as plt
import numpy as np

#inv_dash={v:k for k, v in cleaning.dash.items()}
newdic=dict()
for i in range(1,len(cleaning.x)):
	newdic[cleaning.x[i]]=cleaning.dash[cleaning.x[i]]-cleaning.dash[cleaning.x[i-1]]
	print i
x=newdic.keys()
y=newdic.values()

print y

#plt.plot(x,y,'r-o')
#plt.show()
#-----------------------------For plotting normal distribution curve and histogram-----------------------------------


'''plt.hist(y,bins=50,normed=True)
plt.xlabel("Value")
plt.ylabel("Probability")
#new plot
import numpy as np
import math
from scipy.stats import norm
x = np.linspace(-1000,1000,100)
print y
print len(y)
mu=np.mean(y)
svar=np.var(y)
new_var=svar*len(y)
p = norm.pdf(x, mu,(new_var)**0.5)
plt.plot(x, p, 'k', linewidth=2)
title = "Fit results: mu = %.2f,  std = %.2f" % (mu, (new_var)**0.5)
plt.title(title)

plt.show()'''
#---------------------Plotting Normal Quantile-Quantile Plots---------------------------------
''' 
import pylab 
import scipy.stats as stats
measurements = y
stats.probplot(measurements, dist="norm", plot=pylab,fit=True)
pylab.show() 
'''
#-------------------Plotting the Acf and Pacf Vs Lags-----------------------------------------
'''from statsmodels.tsa.stattools import acf, pacf
lag_acf = acf(cleaning.y, nlags=100,fft=True)
lag_pacf = pacf(cleaning.y, nlags=100, method='ols')
plt.subplot(121) 
plt.plot(lag_acf,"o-")
plt.axhline(y=0,linestyle='--',color='gray')
plt.axhline(y=-1.96/np.sqrt(len(cleaning.y)),linestyle='--',color='gray')
plt.axhline(y=1.96/np.sqrt(len(cleaning.y)),linestyle='--',color='gray')
plt.title('Autocorrelation Function')
plt.subplot(122)
plt.plot(lag_pacf,"o-")
plt.axhline(y=0,linestyle='--',color='gray')
plt.axhline(y=-1.96/np.sqrt(len(cleaning.y)),linestyle='--',color='gray')
plt.axhline(y=1.96/np.sqrt(len(cleaning.y)),linestyle='--',color='gray')
plt.title('Partial Autocorrelation Function')
plt.tight_layout()
plt.show()'''
#--------------------------------------------------------------------------------------------------
