import pandas as pd

df = pd.read_csv("C:/Users/admin/Desktop/Data Science Neha/IRIS.csv")

#preapering X and Y

X = df.drop('species', axis=1)
Y = df['species']

# print(X)
# print(Y)

# Feature Selection 1
# from sklearn.feature_selection import SelectKBest
# from sklearn.feature_selection import chi2
#
# bestfeatures = SelectKBest(score_func=chi2, k = 'all')
# fit = bestfeatures.fit(X,Y)  # training
# dfscores = pd.DataFrame(fit.scores_) # scores store
# dfcolumns = pd.DataFrame(X.columns)  # 4 col value scores
# featurescores = pd.concat([dfcolumns, dfscores], axis=1) # concat scores and cols
# featurescores.columns = ['attributes', 'Score'] #label this cols for results
# print(featurescores)


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


#numerical to cateogical


df['sepal_length'] = pd.cut(df['sepal_length'],3,labels=['0', '1', '2'])
df['sepal_width'] = pd.cut(df['sepal_width'],3,labels=['0', '1', '2'])
df['petal_length'] = pd.cut(df['petal_length'],3,labels=['0', '1', '2'])
df['petal_width'] = pd.cut(df['petal_width'],3,labels=['0', '1', '2'])
print(df)

# cateogical to  numerical




#Dealing with missing value
# 1) use drop(df.drop())
# 2)use replace (df.replace("back","DOS"))
# 3) fill NA()
# df.['Item_weight'].fillna((df['Item_weight'].mean()/.median()/.mode()), inplace = True)
# df['Outle_size'].fillna(('Medium'), inplace = true)  ---> cat

