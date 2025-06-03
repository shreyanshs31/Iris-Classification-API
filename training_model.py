from sklearn import datasets, tree, neighbors
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

iris = datasets.load_iris()

x = iris.data #features
y = iris.target #lables

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=.5)

#build the model choose between decision tree or kneighbors
#cls = tree.DecisionTreeClassifier()
cls = neighbors.KNeighborsClassifier()

#train the model 
cls.fit(x_train, y_train)

#make predictions
predictions = cls.predict(x_test)

#measure accuracy_score
print(accuracy_score(y_test, predictions))

#Saving the model
joblib.dump(cls, "iris_model.pkl")