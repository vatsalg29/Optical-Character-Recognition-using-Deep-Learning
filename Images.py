import numpy as np
import os
import cv2
import matplotlib.pyplot as plt 
import pandas as pd 
from tqdm import tqdm

X_train = np.zeros((115320, 64, 64))
i = 0
'''
for dir_name, sub_dir_list, file_list in tqdm(os.walk(dir)) :
	for image in file_list :
		data = cv2.imread(image)
		#print(data.shape)
		(m, n) = data.shape
		if (m > n) :
			temp = np.zeros((m, m-n))
			data = np.concatenate((data, temp), axis = 1)
		if (m < n) :
			temp = np.zeros((n-m, n))
			data = np.concatenate((data, temp))
		data = cv2.resize(data, (64, 64))
		X_train[i] = data
		i = i + 1
'''
dir = os.listdir("words")
dir.sort()
for a in tqdm(dir):
	d1 = os.listdir("words/" + a)
	d1.sort()
	for b in d1 :
		d2 = os.listdir("words/" + a + "/" + b)
		d2.sort()
		for c in d2 :
			data = cv2.imread("words/" + a + "/" + b + "/" + c, 0)
			try:
				(m, n) = data.shape
			except:
				data = np.zeros((10, 10))
				m = 10
				n = 10
			if (m > n) :
				temp = np.zeros((m, m-n))
				data = np.concatenate((data, temp), axis = 1)
			if (m < n) :
				temp = np.zeros((n-m, n))
				data = np.concatenate((data, temp))
			data = cv2.resize(data, (64, 64))
			X_train[i] = data
			i = i + 1
#X_train = np.asarray(X_train, dtype = 'float32')
plt.imshow(X_train[1])
plt.show()
print(X_train.shape)

X_train = np.reshape(X_train, (X_train.shape[0], -1))
print(X_train.shape)
res = pd.DataFrame(X_train)
res.to_csv("Train_X.csv")