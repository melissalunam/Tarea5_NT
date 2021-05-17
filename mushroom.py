# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 13:15:07 2020

@author: melis

Melissa Aimé Luna Marroquín
1810668
"""
import pandas as pd
from sklearn import metrics
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from id3 import Id3Estimator
from id3 import export_graphviz

en = preprocessing.LabelEncoder()

#Leemos el Excel
df = pd.read_csv('mushroomm.csv')
df.head()

#Leemos los datos de si es venenoso o no
y = df['class'].values
y[0:5]

#Transformamos los datos
df = df.apply(en.fit_transform)
X = df[['cap-shape', 'cap-surface', 'cap-color', 'bruises%3F','odor', 'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color', 'stalk-shape', 'stalk-surface-above-ring', 'stalk-surface-below-ring', 'stalk-color-above-ring', 'stalk-color-below-ring','veil-type','veil-color', 'ring-type', 'spore-print-color', 'population', 'habitat']].values
X[0:5]

#Split data
X_trainset, X_testset, y_trainset, y_testset = train_test_split(X, y, test_size=0.5, random_state=3)

#Entrenar mdelo
mushroomTree = Id3Estimator()
mushroomTree

#predercir
mushroomTree.fit(X_trainset,y_trainset)
predTree = mushroomTree.predict(X_testset)
print (predTree [0:21])
print (y_testset [0:21])

#Evaluate
print("Accuracy del árbol de decisión: ", metrics.accuracy_score(y_testset, predTree))
#Visualizing tree
featureNames = df.columns[0:21]
export_graphviz(mushroomTree.tree_, 'mushroom.dot',featureNames)