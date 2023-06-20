import pandas  as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier

df = pd.read_csv("C:/Users/admin/Desktop/Data Science Neha/titanic.csv")
# print(df)

#preapering X and Y
X = df.drop('PassengerId', axis=1)
X = X.drop('Ticket', axis=1)
X = X.drop('Cabin', axis=1)
X = X.drop('Name', axis=1)
X = X.drop('Survived', axis=1)
Y = df['Survived']
#
# print(X)
# print(Y)

# replacing values
le = LabelEncoder()
le.fit(X['Sex'])
X['Sex'] = le.transform(X['Sex'])

le = LabelEncoder()
le.fit(X['Embarked'])
X['Embarked'] = le.transform(X['Embarked'])

# print(X)

#Missing values
X['Pclass'].fillna((X['Pclass'].mean()), inplace=True)
X['Pclass'].fillna((X['Pclass'].mean()), inplace=True)
X['Age'].fillna((X['Age'].mean()), inplace=True)
X['SibSp'].fillna((X['SibSp'].mean()), inplace=True)
X['Parch'].fillna((X['Parch'].mean()), inplace=True)
X['Fare'].fillna((X['Fare'].mean()), inplace=True)
X['Embarked'].fillna((X['Embarked'].mean()), inplace=True)

# print(X)

# Feature Selection 2
# from sklearn.ensemble import ExtraTreesClassifier
# import matplotlib.pyplot as plt
#
# model = ExtraTreesClassifier()
# model.fit(X,Y)
# print(model.feature_importances_)
#
# feat_importace =pd.Series(model.feature_importances_, index=X.columns)
# feat_importace.nlargest(4).plot(kind='barh')
# plt.show()


#Inbalance in dataset

from collections import Counter
# print(Counter(Y))

# print("\n")

from imblearn.over_sampling import RandomOverSampler  # -----> OverSampling 2
sms = RandomOverSampler(random_state=0)
X,Y = sms.fit_resample(X, Y)
# print(Counter(Y))

#Identifying outliers by ploting
#
# from matplotlib import pyplot as plt
# import seaborn as sns
# sns.boxplot(df['Fare'])
# plt.show()


#Dealing wih outliers using Interquantile Range  (CHECK OUTLIERS)

print(X['Fare'])
Q1 = X['Fare'].quantile(0.25)
Q3 = X['Fare'].quantile(0.75)

IQR = Q3 - Q1
print(IQR)

upper = Q3 + 1.5*IQR
lower = Q1 - 1.5*IQR

print(upper)
print(lower)

out1 = X[X['Fare'] < lower].values
out2 = X[X['Fare'] > upper].values

X['Fare'].replace(out1, lower, inplace=True)
X['Fare'].replace(out2, upper, inplace=True)

print(X['Fare'])

#training the model

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

logr = LogisticRegression()
Ran  = RandomForestClassifier()

print(X)

x_train, x_test, y_train, y_test = train_test_split(X, Y, random_state=0, test_size=0.3)
logr.fit(x_train, y_train)

y_pred = logr.predict(x_test)
print(accuracy_score(y_test, y_pred)*100)

Ran.fit(x_train, y_train)

y_pred1 = Ran.predict(x_test)
print(accuracy_score(y_test, y_pred1)*100)