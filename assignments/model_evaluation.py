from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score

iris = load_iris()
X,y=iris.data,iris.target

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

model =LogisticRegression(max_iter=200)
model.fit(X_train,y_train)

y_pred =model.predict(X_test)
# print("Prediction :",prediction)

print("True Labels:", y_test)
print("Predicted :", y_pred)

## computing Evaluation metrics 
acc =accuracy_score(y_test,y_pred) # it require true labels and predition 
print("Accuracy :",acc)
prec=precision_score(y_test,y_pred,average='macro')
print("Precision: ",prec)
rec=recall_score(y_test,y_pred,average='macro')
f1=f1_score(y_test,y_pred,average='macro')

## saving files
with open('assignments/evaluation_metrics.txt','w') as f:
    f.write(f"Accuracy: {acc:.4f}\n")
    f.write(f"Precision: {prec:.4f}\n")
    f.write(f"Recall: {rec:.4f}\n")
    f.write(f"F1 Score: {f1:.4f}\n")

