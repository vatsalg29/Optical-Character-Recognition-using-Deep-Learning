import numpy as np
import pandas as pd
import os
from bs4 import BeautifulSoup
from tqdm import tqdm
vocab = []
dir = os.listdir('xml')
dir.sort()
for file in tqdm(dir):
	with open('xml/' + file, "r") as f:
		contents = f.read()
		soup = BeautifulSoup(contents, "html5lib")
		for w in soup.find_all("word") :
			vocab.append(list('{:10}'.format(w.get("text"))))

Y_train = np.zeros((len(vocab), 10))

print(Y_train.shape)
for i in range(Y_train.shape[0]) :
	for j in range(10) :
		c = 0
		if (vocab[i][j] >= 'a' and vocab[i][j] <= 'z') :
			c = ord(vocab[i][j]) - 97
		elif (vocab[i][j] >= 'A' and vocab[i][j] <= 'Z') :
			c = ord(vocab[i][j]) - 65 + 26
		else :
			c = 52
		Y_train[i][j] = c

print(Y_train.shape)

res = pd.DataFrame(Y_train)
res.to_csv("Train_Y.csv")