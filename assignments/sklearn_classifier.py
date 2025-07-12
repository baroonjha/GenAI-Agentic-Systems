import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

#Load iris dataset

iris =load_iris()
X,y =iris.data,iris.target

#split data
X_train,X_test, y_train,y_test =train_test_split(X,y,test_size=0.2)

#Train model
model=LogisticRegression(max_iter=200)
model.fit(X_train,y_train)

# evalute accuracy
accuracy =model.score(X_test,y_test)

# save accuracy
with open('assignments/iris_accuracy.txt','w') as f:
    f.write(f'Accuracy:{accuracy:.4f}')

print(f'Model accuracy: {accuracy:.4f}')