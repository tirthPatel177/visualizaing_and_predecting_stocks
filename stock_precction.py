predict stock price using ML model

import quandl
import numpy as np
from sklearn.linear model import LinearRegression
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split

#GET DATA
df = quadl.get("WIKI/FB")
print(df.head())

#for predict the future stock prices

forecast_ot = 1 //variable for n days
df['Prediction'] = df[['column_name']].shift(-1)

#create the indeoendent data set
X=np.array(df.drop(['column_name_tobe_drop'],1))

X= X[:-forecast_ot]

#create dependent data set
y = np.array(df['Prediction'])

y= y[:-forecast_ot]

x_train, x_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

#create the SVM(regressor)

svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
svr_rbf.fit(x_train, y_train)




#test model score returns coefficient of determination of R^2
#best prediction is 1.0
svm_confidence=svr_rbf.score(x_test, y_test)
print("svm_confidence: ",svm_confidence)



#linear regression model
lr=LinearRegression()
lr.fit(x_train, y_train)

lr_confidence=lr.score(x_test, y_test)
print("lr_confidence: ",lr_confidence)


 x_forecast=np.array(df.drop(['Prediction'],1))[-forecast_ot:]
lr_prediction =lr_predict(x_forecast)
svm_prediction=svr_rbf.predict(x_forecast)


