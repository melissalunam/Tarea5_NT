# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 13:49:59 2020

@author: melis

Melissa Aimé Luna Marroquín
1810668
"""

import numpy as np 
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt
from six import StringIO
import pydotplus
import matplotlib.image as mpimg
from sklearn import tree
from sklearn import preprocessing
en = preprocessing.LabelEncoder()
#Leemos el Excel
df = pd.read_csv('mushroom.csv')
df.head()
#Leemos los datos de si es venenoso o no
y = df['class'].values
y[0:5]
#Transformamos los datos
df = df.apply(en.fit_transform)
X = df[['cap-shape', 'cap-surface', 'cap-color', 'bruises%3F','odor', 'gill-attachment', 'gill-spacing'
        , 'gill-size', 'gill-color', 'stalk-shape', 'stalk-surface-above-ring',
        'stalk-surface-below-ring', 'stalk-color-above-ring', 'stalk-color-below-ring','veil-type','veil-color',
        'ring-type', 'spore-print-color', 'population', 'habitat']].values
X[0:5]
#Split data
X_trainset, X_testset, y_trainset, y_testset = train_test_split(X, y, test_size=0.5, random_state=3)
#Entrenar mdelo
fuelTree = DecisionTreeClassifier(criterion="entropy", max_depth = 4)
fuelTree
#predercir
fuelTree.fit(X_trainset,y_trainset)
predTree = fuelTree.predict(X_testset)
print (predTree [0:20])
print (y_testset [0:20])
#Evaluate
print("DecisionTrees's Accuracy: ", metrics.accuracy_score(y_testset, predTree))
#Visualizing tree
dot_data = StringIO()
filename = "mushroom.png"
featureNames = df.columns[0:20]
targetNames = df["class"].unique().tolist()
out=tree.export_graphviz(fuelTree,feature_names=featureNames, out_file=dot_data, class_names= np.unique(y_trainset), filled=True,  special_characters=True,rotate=False)  
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png(filename)
img = mpimg.imread(filename)
plt.figure(figsize=(100, 200))
plt.imshow(img,interpolation='nearest')