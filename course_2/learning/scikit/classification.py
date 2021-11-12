from sklearn.svm import SVC
from sklearn import datasets
import numpy
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report

iris = datasets.load_iris()

# print(iris.data)
# print(iris.target)
# print(iris.feature_names)
# print(iris.target_names)

# dividing test and training data

iris_X = iris.data

# there are 3 target_names which are the flower species
# target is an array of the target_names indexes
iris_Y = iris.target


# permute index to create random data
indices = numpy.random.permutation(len(iris_X))

# print(indices)

# assign 10 data to train data and the orthers to test
# combinig target and test data
iris_X_train = iris_X[indices[:-10]]
iris_X_test = iris_X[indices[-10:]]

iris_Y_train = iris_Y[indices[:-10]]
iris_Y_test = iris_Y[indices[-10:]]


knn = KNeighborsClassifier()
# train the classifier with data giving input and output
knn.fit(iris_X_train, iris_Y_train)

# print(knn.predict(iris_X_test))
# print(iris_Y_test)


svc = SVC(kernel='linear')
svc.fit(iris_X_train, iris_Y_train)

# print(svc.predict(iris_X_test))
# print(iris_Y_test)


# for printing data
print(classification_report(
    iris_Y_test,
    svc.predict(iris_X_test),
    target_names=iris.target_names
))
