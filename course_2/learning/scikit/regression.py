from sklearn.svm import SVC
from sklearn import datasets
import numpy
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.linear_model import LinearRegression

diabetes = datasets.load_diabetes()

diabetes_X = diabetes.data

diabetes_Y = diabetes.target

numpy.random.seed(2307)


indices = numpy.random.permutation(len(diabetes_X))


diabetes_X_train = diabetes_X[indices[:-10]]
diabetes_X_test = diabetes_X[indices[-10:]]

diabetes_Y_train = diabetes_Y[indices[:-10]]
diabetes_Y_test = diabetes_Y[indices[-10:]]


knn = KNeighborsClassifier()
knn.fit(diabetes_X_train, diabetes_Y_train)


regr = LinearRegression()
regr.fit(diabetes_X_train, diabetes_Y_train)


# classic way to calculate the error mean
print(numpy.mean((regr.predict(diabetes_X_test - diabetes_Y_test)) ** 2))
