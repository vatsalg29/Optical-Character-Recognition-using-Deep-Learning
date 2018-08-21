# -*- coding: utf-8 -*-
"""OCR.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_DYFu440zgSozaS2W5i7LH018UQU-C1y
"""

import tensorflow as tf
tf.test.gpu_device_name()

!pip install -U -q PyDrive
 
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials
 
# 1. Authenticate and create the PyDrive client.
auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)

file_list = drive.ListFile({'q': "'1iW1GMIWmDm6h6uGxJPjk2bt-7JcQJETM' in parents and trashed=false"}).GetList()
for file1 in file_list:
  print('title: %s, id: %s' % (file1['title'], file1['id']))

train_downloaded = drive.CreateFile({'id': '1HfeTC65KaW3FOE2httDR6wYySvdUbF4o'})
train_downloaded.GetContentFile('train.csv')
test_downloaded = drive.CreateFile({'id': '12dgVBkW6GCa-1dQkSMrLQ55ee-FUgv3M'})
test_downloaded.GetContentFile('test.csv')

import numpy as np
import keras
import matplotlib.pyplot as plt
import pandas as pd
import os

data_train = pd.read_csv("train.csv").values
data_test = pd.read_csv("test.csv").values

X_train = data_train[:, 1:]
Y_train = data_train[:,0]
X_test = data_test[:, 1:]
Y_test = data_test[:,0]

X_train = np.reshape(X_train, (X_train.shape[0], 28, 28, 1)) / 255
X_test = np.reshape(X_test, (X_test.shape[0], 28, 28, 1)) / 255
Y_train = np.reshape(Y_train, (Y_train.shape[0], 1))
Y_test = np.reshape(Y_test, (Y_test.shape[0], 1))

Y_train = keras.utils.to_categorical(Y_train, 47)
Y_test = keras.utils.to_categorical(Y_test, 47)

print(X_train.shape)
print(Y_train.shape)
print(X_test.shape)
print(Y_test.shape)

def make_model(input_shape):
  X_input = keras.layers.Input(input_shape)
  X = keras.layers.Conv2D(32, (3,3), padding = 'same')(X_input)
  X = keras.layers.BatchNormalization(axis = 3)(X)
  X = keras.layers.Activation('relu')(X)
  
  X = keras.layers.MaxPooling2D((2,2))(X)
  
  X = keras.layers.Conv2D(64, (3,3), padding = 'same')(X)
  X = keras.layers.BatchNormalization(axis = 3)(X)
  X = keras.layers.Activation('relu')(X)
  
  X = keras.layers.MaxPooling2D((2,2))(X)
  
  X = keras.layers.Conv2D(128, (4,4))(X)
  X = keras.layers.BatchNormalization(axis = 3)(X)
  X = keras.layers.Activation('relu')(X)
  
  X = keras.layers.Flatten()(X)
  X = keras.layers.Dropout(0.5)(X)
  X = keras.layers.Dense(256, activation = 'relu')(X)
  X = keras.layers.Dropout(0.5)(X)
  X = keras.layers.Dense(47, activation = 'softmax')(X)
  
  model = keras.models.Model(inputs = X_input, outputs = X, name = "model")
  model.summary()
  
  return model

model = make_model((28, 28, 1))

opt = keras.optimizers.Adam(lr = 0.0001)
model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

model.fit(X_train, Y_train, batch_size = 512, epochs = 20, validation_data = (X_test, Y_test))


