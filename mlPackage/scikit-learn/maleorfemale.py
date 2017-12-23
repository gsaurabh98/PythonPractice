import numpy as np
from sklearn.tree import DecisionTreeClassifier
#[height, weight , shoe size]
x = [[181,80,44,22],[174,70,40,34],[160,60,35,23],[154,54,37,14],
     [166,65,45,21],[190,90,47,19],[175,64,47,18],[181,85,43,16],
             [167,55,38,20],[176,77,42,17]]

y = np.array(['male','female','female','male',
     'male','male','female','female',
     'male','female'])

# Decision tree classifier
clf = DecisionTreeClassifier()

# x is basically features and y is label, means based on the given features we will predict the labels
# giving the training data and it learn with patterns
clf = clf.fit(x,y)

# prediction is basically to expect output by giving input training data
prediction = clf.predict([[10,5,2,1]])

for item in prediction:
    print item

from sklearn.naive_bayes import GaussianNB
