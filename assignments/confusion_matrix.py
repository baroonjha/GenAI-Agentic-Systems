import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,ConfusionMatrixDisplay
import matplotlib.pyplot as plt

#load data
iris=load_iris()
X,y =iris.data ,iris.target

#split data
X_train,X_test,y_train,y_test =train_test_split(X,y,test_size=0.2,random_state=42)

#train model
model=LogisticRegression(max_iter=200)
model.fit(X_train,y_train)

#predict
y_pred =model.predict(X_test)

# plot confusion matrix

cm=confusion_matrix(y_test,y_pred)
disp=ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=iris.target_names)
disp.plot(cmap='Blues')
plt.title('Confusion Matrix:Iris Classifier')
plt.savefig('assignments/confusion_matrix.png')
plt.close()