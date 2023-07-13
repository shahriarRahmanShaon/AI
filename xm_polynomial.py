# -*- coding: utf-8 -*-
"""xm_polynomial.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Msc5ETxxROD5FLme5dcRevjA8r6jeKLg
"""

import tensorflow as tf
from tensorflow.keras.layers import Dense
from tensorflow.keras import Sequential
import numpy as np
import matplotlib.pyplot as plt
from numpy import random

X = []
Y = []
for i in range(100):
    num = random.randint(-5,5)

    X.append(num)
    num_y = 3*num*num*num + 7*num*num - 12*num +2
    print(num, num_y)
    Y.append(num_y)

model = Sequential()
model.add(Dense(128,input_dim = 1, activation='relu',name="dense_layer_1"))
model.add(Dense(64, activation='relu',name="dense_layer_2"))
model.add(Dense(32, activation='relu',name="dense_layer_3"))
model.add(Dense(16, activation='relu',name="dense_layer_4"))
model.add(Dense(8, activation='relu',name="dense_layer_5"))
model.add(Dense(4, activation='relu',name="dense_layer_6"))
model.add(Dense(1,name="Output"))

model.summary()

model.compile(loss = 'mean_squared_error', optimizer='adam',metrics=['accuracy'])

model.fit(X,Y,epochs = 50)

def call(num):
    ans = 3*num*num*num + 7*num*num - 12*num +2
    print('predicted value for : ',num,' is ',ans)

for i in range(5):
    x = random.randint(-5,5)
    predictions = model.predict([x],verbose=0)
    print('Predicted value by model : ',predictions)
    call(x)