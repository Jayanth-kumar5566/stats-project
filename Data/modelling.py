from statsmodels.tsa.arima_model import ARIMA
import changingtrend
import matplotlib.pyplot as plt
#---------------------Plotting AR Model--------------------------------------------------
model = ARIMA(changingtrend.y, order=(15, 1 , 0)) #(p,q,d)  
results_AR = model.fit(disp=-1)

plt.plot(changingtrend.y,"-o")
plt.plot(results_AR.fittedvalues, color='red')
#plt.title('RSS: %.4f'% sum((results_AR.fittedvalues-Y)**2))
plt.show()

