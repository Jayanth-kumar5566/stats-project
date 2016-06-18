mydata=runif(n=50,min=10,max=45)
#--------Adding my data as a Vector-------------------------------------------
x=c(2504.6296296296296, 2650.0, 2665.3846153846152, 2448.2758620689656, 2583.3333333333335, 2752.3809523809523, 3140.0, 3200.0, 3200.0, 3150.0, 3200.0, 2568.9473684210525, 2930.3846153846152, 3100.0, 3021.4285714285716, 3745.0, 3877.7419354838707, 3830.0, 3759.6774193548385, 3800.0, 3341.0714285714284, 3436.6666666666665, 3263.3333333333335, 3579.1666666666665, 3396.7741935483873, 3401.818181818182, 3569.1666666666665, 3436.3636363636365, 3458.0, 3718.0, 3238.653846153846, 3526.6666666666665, 4293.333333333333, 4203.225806451613, 3460.0, 3856.6666666666665, 3491.935483870968, 3425.6, 3460.0, 4102.413793103448, 4150.0, 4548.275862068966, 4700.0, 4210.666666666667, 4577.241379310345, 4401.612903225807, 4316.0, 4600.0, 4353.548387096775, 4724.642857142857, 5244.333333333333, 5328.5, 5373.322580645161, 5332.9, 5561.758620689655, 6038.75, 5884.335, 5685.667, 5478.846153846154, 5708.862068965517, 5826.806451612903, 5952.928571428572, 5770.193548387097, 5445.076923076923, 5412.0, 5024.666666666667, 4853.225806451613, 4336.862068965517, 4219.0526315789475, 4205.733333333334, 4424.137931034483, 4241.741935483871, 4117.806451612903, 3995.1428571428573, 3939.2580645161293, 3958.0, 4132.4, 4358.28, 4166.0, 4503.580645161291, 5125.0, 4468.4, 4517.0, 4446.724137931034, 4375.0, 4375.0, 4451.612903225807, 4500.0, 5207.068965517241, 5746.133333333333, 5733.870967741936, 5604.8387096774195, 5678.333333333333, 5938.709677419355, 5000.0, 4677.419354838709)
class(x)
#------------Coverting my vector to a timeseries object-------------------------
mytimeseries=ts(data=x,start=2008, frequency=12)
#---------------Plotting my time series dataset-------------------------------------------
plot(mytimeseries)
#---------------Decomposing time series data assuming it is an additive model--------------- 
decomposed_timeseries=decompose(mytimeseries,"additive") #can change into multipicative by changing the object
plot(decompose(mytimeseries,"additive"))
#-----------Different Method for seasonal decomposition of data--------------------------
plot(stl(mytimeseries,s.window="periodic"))
#----------Removing seasonality from the Timeseries-------------------------------
adjusted_timeseries=mytimeseries-decomposed_timeseries$seasonal
plot(adjusted_timeseries)
#----------Plotting seasonality of timeseries-------------------------
library(forecast)
seasonplot(mytimeseries)
#----------Moving average methods------------------------------
#Trying to use moving average over 'n' months(Useful for non-seasonal datasets)
library(TTR)
timeseries_smoothed=SMA(mytimeseries,n=3);timeseries_smoothed
plot(mytimeseries)
plot(timeseries_smoothed)
#-------------Making time series data stationary-------------------------
#------------Differencing the time series data------------------------
stationary_timeseries=diff(mytimeseries,differences=1)
plot(stationary_timeseries)
#------------Checking for stationarity--------------------------------
#---------------Using Augmented Dickey Fuller Test-----------------------
library(tseries)
adf.test(stationary_timeseries)
#-------------Plotting the acf and pacf of the stationary timeseries---------------
library(forecast)
Acf(stationary_timeseries)
Pacf(stationary_timeseries)
auto.arima(stationary_timeseries,trace=TRUE)
