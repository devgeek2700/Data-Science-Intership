
import pandas as pd

df = pd.read_csv("C:/Users/admin/Desktop/Data Science Neha/IRIS.csv")

#Identifying outliers by ploting
# from matplotlib import pyplot as plt
# import seaborn as sns
# sns.boxplot(df['sepal_length'])
# plt.show()



# 1)import
# 2)create alias
# 3) identify and preparing  X and Y
# 4)traning model split train and test set
# 5) present the results




#Dealing wih outliers using Interquantile Range

print(df['sepal_length'])
Q1 = df['sepal_length'].quantile(0.25)
Q3 = df['sepal_length'].quantile(0.75)

IQR = Q3 - Q1
print(IQR)

upper = Q3 + 1.5*IQR
lower = Q1 - 1.5*IQR

print(upper)
print(lower)

out1 = df[df['sepal_length'] < lower].values
out2 = df[df['sepal_length'] > upper].values

df['sepal_length'].replace(out1, lower, inplace=True)
df['sepal_length'].replace(out2, upper, inplace=True)

print(df['sepal_length'])