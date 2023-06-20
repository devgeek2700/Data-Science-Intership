import pandas as pd

df = pd.read_csv("C:/Users/admin/Desktop/Data Science Neha/IRIS.csv")
# print(df.isnull().sum())
# print('\n')
# print(df.notnull().sum())


# df['sepal_length'].fillna((df['sepal_length'].median()), inplace=True)
# df['sepal_width'].fillna((df['sepal_width'].mean()), inplace=True)
# df['petal_length'].fillna((df['petal_length'].max()), inplace=True)
# df['petal_width'].fillna((df['petal_width'].min()), inplace=True)

# print(df.count())


#Inbalance in dataset
#Overampling & Undersampling

from collections import Counter
X = df.drop('species', axis=1)
Y = df['species']

print(Counter(Y))

print("\n")


# from imblearn.over_sampling import RandomOverSampler  # -----> OverSampling 1
# ros = RandomOverSampler(random_state=0)
# X,Y = ros.fit_resample(X, Y)
# print(Counter(Y))








from imblearn.over_sampling import RandomOverSampler  # -----> OverSampling 2
sms = RandomOverSampler(random_state=0)
X,Y = sms.fit_resample(X, Y)
print(Counter(Y))


# from imblearn.over_sampling import RandomOverSampler  # -----> UnderSampling 1
# ros = RandomOverSampler(random_state=0)
# X,Y = ros.fit_resample(X, Y)
#
# print("Iris-setosa: ",a)
# print("Iris-versicolor: ",b)
# print("Iris-virginica: ",c)