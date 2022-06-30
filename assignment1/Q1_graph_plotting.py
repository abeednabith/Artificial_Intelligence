from pandas.errors import InvalidIndexError
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

df = pd.read_csv("sbp_dataset.csv")
df

reg = linear_model.LinearRegression()
reg.fit(df[['Age', 'Weight']], df.SBP)

m = reg.coef_
print(f"coeffiecients : {m}")
c = reg.intercept_
print(f"intercepts : {c}")
print(f"predicted SBP for 65 and 85: {reg.predict([[65, 85]])}")
print(f"predicted SBP for 79 and 80: {reg.predict([[79, 80]])}")

y1 = m[0]*65 + m[1]*85 + c
y2 = m[0]*79 + m[1]*80 + c
print(f"predicted linear regression for 65 and 85:: {y1}")
print(f"predicted linear regression for 79 and 80: {y2}")

%matplotlib inline
plt.xlabel('Age')
plt.ylabel('SBP')
plt.scatter(df.Age, df.SBP, color='red')
plt.scatter(df.Weight, df.SBP, color='blue')
plt.plot(df.Age, reg.predict(df[['Age', 'Weight']]), color='blue')
