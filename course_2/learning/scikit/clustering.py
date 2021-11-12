from sklearn.svm import SVC
from sklearn import datasets
import numpy
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.cluster import KMeans

numpy.random.seed(2307)
iris = datasets.load_iris()
iris_X = iris.data
iris_Y = iris.target


indices = numpy.random.permutation(len(iris_X))

km = KMeans(n_clusters=3)
km.fit(iris_X)

print(km.labels_[::10])
print(iris_Y[::10])
