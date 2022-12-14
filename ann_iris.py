# -*- coding: utf-8 -*-
"""ANN_Iris.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EROY2mEkEoRQ7L5V9RTHwpBoWyI_jp_3
"""

#Importing Packages
import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense
from sklearn import datasets

data=datasets.load_iris()
print(data)

x=data.data
y=data.target
z=data.target_names
print(data.feature_names)
print(x[0])

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)

print(x_train.shape)
print(x_test.shape)

#Building the Model
model=Sequential();
model.add(Dense(100,input_shape=(4,),activation="relu"))
model.add(Dense(3,activation="softmax"))

#compile model
model.compile(optimizer="sgd",loss="sparse_categorical_crossentropy",metrics=["accuracy"])

#Fit the model
model.fit(x_train,y_train,epochs=20)

#Evaluate the Model
model.evaluate(x_test,y_test)

pred=model.predict(x_test[:10])
print(pred)

p=np.argmax(pred,axis=1)
print(p)
print(y_test[:10])

for i in p:
  print("Predicted Class:{}, Name:{}".format(i,z[i]))