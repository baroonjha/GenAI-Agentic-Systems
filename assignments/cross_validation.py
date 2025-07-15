import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression


#load iris data
iris =load_iris()
X,y =iris.data,iris.target

#initialize the model
model=LogisticRegression(max_iter=200)

#perform 5-fold cross validation
scores=cross_val_score(model,X,y,cv=5)


#compute mean and sd
mean_accuracy =np.mean(scores)
std_dev = np.std(scores)


#save result

with open('assignments/cross_val_results.txt','w') as f:
    f.write(f'Mean Accuracy : {mean_accuracy:.4f}\n')
    f.write(f'Std Deviation: {std_dev:.4f}')


print(f'Mean Accuracy: {mean_accuracy:.4f}')
print(f'Std Deviation : {std_dev:.4f}')    