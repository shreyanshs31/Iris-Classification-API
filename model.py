import joblib
import numpy as np

#Load model 
model = joblib.load("iris_model.pkl")

#List of labels
class_names = ["setosa", "versicolor", "virginica"]

def predicts(features):
    input_array = np.array([[features.sepal_length, features.sepal_width, features.petal_length, features.petal_width]])
    prediction = model.predict(input_array)
    return class_names[prediction[0]]
