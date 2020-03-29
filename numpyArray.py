import numpy as np
import cv2 # pip install opencv-python
import random
import os
import pickle
import matplotlib.pyplot as plt

DATADIR = './CopiedRavenImages'
CATEGORIES = ['Corvuscorax', 'background']
IMG_SIZE = 50

def main():
    trainingData = []
    for category in CATEGORIES:
        path = os.path.join(DATADIR, category)
        index = CATEGORIES.index(category)
        for img in os.listdir(path): # path to images
            img_array = cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE)
            new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
            trainingData.append([new_array, index])

    random.shuffle(trainingData)
    X = []
    Y = []
    for feaures, label in trainingData:
        X.append(features)
        Y.append(label)

    X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1)

    pickle_out = open('Xarray.txt', 'wb')
    pickle.dump(X, pickle_out)
    pickle_out.close()

    pickle_out = open('Yarray.txt', 'wb')
    pickle.dump(Y, pickle_out)
    pickle_out.close())

main()
