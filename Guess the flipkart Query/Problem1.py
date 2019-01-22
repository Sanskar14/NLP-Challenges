# Importing Libraries
import pandas as pd
from sklearn.feature_extraction.text import HashingVectorizer
transformer=HashingVectorizer(stop_words='english')

# Importing Dataset, Test set and Training Set
dataset = pd.read_csv("training.txt",sep = "\t",names = ["Query","Keyword"])
dataset = dataset.drop(0)
X_train = dataset.iloc[:,0]
y_train = dataset.iloc[:,1]
X_train = X_train.tolist()
y_train = y_train.tolist()
X_test  = pd.read_csv("X_test.txt",names = ["Query"])
X_test  = X_test.drop(0)
y_test  = pd.read_csv("y.txt",names = ["Keyword"])
X_test  = X_test["Query"].values.T.tolist()
y_test  = y_test["Keyword"].values.T.tolist()
X_train = X_train + X_test
y_train = y_train + y_test

# Creating Bag of Words model
#cv= CountVectorizer()
X_train = transformer.fit_transform(X_train).toarray()


from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier()
classifier.fit(X_train,y_train)

"""
X_test = transformer.transform(X_test).toarray()
print(classifier.score(X_test,y_test))
"""
n=int(input())
Query =[input() for _ in range(n)]
Query = transformer.transform(Query)
predict_Query = classifier.predict(Query)
for Qu in predict_Query:
    print(Qu)
