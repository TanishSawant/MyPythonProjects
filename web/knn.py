import pandas as pd

data = pd.read_csv('C:\\Users\\milindsawant\\Downloads\\breast-cancer-wisconsin.data')
cols = ['Sample code number', 'Clump Thickness', 'Uniformity of Cell Size', 'Uniformity of Cell Shape', 'Marginal Adhesion', 'Single Epithelial Cell Size', 'Bare Nuclei', 'Bland Chromatin', 'Normal Nucleoli', 'Mitoses', 'Class']
data.columns = cols
print(data.head())

import sklearn
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing, cross_validation
import numpy as np

data.replace('?', -99999, inplace = True)
data.drop(['id'], 1 , inplace = True)

X = np.array(data.drop(['class'], 1))
y= np.array(data['class'])

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size = 0.2)

clf = KNeighborsClassifier()