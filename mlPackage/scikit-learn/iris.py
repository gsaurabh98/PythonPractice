from sklearn import datasets,metrics
# evrything in the scikit learn we call classifier and in real world we call support vector machine
from sklearn.svm import SVC

#load_iris() function is loading the iris datasets from the datasets
ds = datasets.load_iris()

# fit a SVM model to the data
model = SVC()
model.fit(ds.data,ds.target)
#print model

#make predictions
expected = ds.target
predicted = model.predict(ds.data)

#summarize the fit of the model
print metrics.classification_report(expected,predicted)