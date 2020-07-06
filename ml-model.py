import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import accuracy_score
import pickle

df=pd.read_csv('dataframe.csv')

cv=CountVectorizer(max_features=1900)

clf3=BernoulliNB()


X=cv.fit_transform(df.review).toarray()
y=df.iloc[:,-1].values
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)
clf3.fit(X_train,y_train)
y_pred3=clf3.predict(X_test)

pickle.dump(cv,open('mystrings.pkl','wb'))
pickle.dump(clf3,open('model.pkl','wb'))



