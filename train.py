import pandas as pd

df = pd.read_csv("C:/Users/admin/Desktop/Data Science Neha/IRIS.csv")

#training the model
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

logr = LogisticRegression()
pca = PCA(n_components=2)

X = df.drop('species', axis=1)
Y = df['species']

pca.fit(X)
X = pca.transform(X)

print(X)

x_train, x_test, y_train, y_test = train_test_split(X, Y, random_state=0, test_size=0.3)
logr.fit(x_train, y_train)

y_pred = logr.predict(x_test)
print(accuracy_score(y_test, y_pred)*100)