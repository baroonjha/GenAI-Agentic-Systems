from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler


#load data
iris =load_iris()
X,y= iris.data,iris.target

#

#split the data
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

#standardize features
scaler=StandardScaler()
X_train_scaled =scaler.fit_transform(X_train)
X_test_scaled =scaler.fit_transform(X_test)

#train model
model=LogisticRegression(max_iter=200)
model.fit(X_train_scaled,y_train)

#evaluate 
accuracy=model.score(X_test_scaled,y_test)

#save results
with open('assignments/scaled_accuracy.txt','w') as f:
    f.write(f'Test Accuracy:{accuracy:.4f}')


print(f'Test Accuracy: {accuracy:.4f}')    