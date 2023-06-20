import pandas as pd
from sklearn.datasets import load_iris

# irs = load_iris()
# print(irs)

# print(irs.keys())
# print(irs.values())
# print(irs.data)
# print(irs.target)
# print(irs.feature_names)
# print(irs.target_names)
# print(irs.DESCR)



# dataset from kaggle

df = pd.read_csv("C:/Users/admin/Desktop/Data Science Neha/IRIS.csv")
# print(df)
# print(df.head(20))
# print(df.tail(30))
# print(df.columns.values)
print(df.describe())