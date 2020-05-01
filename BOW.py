from parser import readData
import numpy as np
from pyts.datasets import load_gunpoint
from pyts.bag_of_words import BagOfWords
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import sys
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
np.set_printoptions(threshold=sys.maxsize)
#print("shape is", data_train.shape)
# km = KMeans(
#     n_clusters=3, init='random',
#     n_init=10, max_iter=300,
#     tol=1e-04, random_state=0
# )
# y_km = km.fit(data_train)
instances = readData("./venezia/Punta_Salute_1983_2015/Punta_Salute_2015.csv")

data_train, data_test, target_train, target_test = load_gunpoint(return_X_y=True)



window_size, word_size = 50, 5
bow = BagOfWords(window_size=window_size, word_size=word_size,
                 window_step=window_size, numerosity_reduction=False)
X_bow = bow.transform(data_train)
test_bow = bow.transform(data_test)


frequencyDictListX = []
frequencyDictListTest = []

for i in range(len(X_bow)):
    frequencyDict = {}
    localCodeWordArr = X_bow[i].split(" ")
    for word in localCodeWordArr:
        if word not in frequencyDict:
            frequencyDict[word] = 1
        elif word in frequencyDict.keys():
            frequencyDict[word] += 1
    frequencyDictListX.append(frequencyDict)

for i in range(len(test_bow)):
    frequencyDict = {}
    localCodeWordArr = X_bow[i].split(" ")
    for word in localCodeWordArr:
        if word not in frequencyDict:
            frequencyDict[word] = 1
        elif word in frequencyDict.keys():
            frequencyDict[word] += 1
    frequencyDictListTest.append(frequencyDict)



#print(frequencyDictList)
# make sure to normalize histograms
#histogram = plt.hist(frequencyDict.keys(), bins=len(frequencyDict.keys()))

model = KNeighborsClassifier(n_neighbors=1,
	n_jobs=-1)
#model.fit(trainFeat, trainLabels)


width = 1.0
plt.bar(frequencyDict.keys(), frequencyDict.values(), width, color='g')
plt.xticks(rotation=90)
#plt.show()
#