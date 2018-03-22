# Imports
import numpy as np
import pandas as pd
import itertools

%matplotlib inline
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn.linear_model import SGDClassifier
from sklearn.neural_network import MLPClassifier

from sklearn.metrics import accuracy_score, confusion_matrix, roc_curve, roc_auc_score
from sklearn.model_selection import train_test_split, GridSearchCV

import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.utils import np_utils
from keras import backend as K
K.set_image_dim_ordering('th')
from keras.models import load_model

def cnn_model():
    # create model
    model = Sequential()
    model.add(Conv2D(30, (5, 5), input_shape=(1, 28, 28), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(15, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.2))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dense(50, activation='relu'))
    model.add(Dense(num_classes, activation='softmax'))
    # Compile model
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

if __name__ == "__main__":
	#DATA PREPROCESSING
	# load the data
	ear = np.load('datasets/ear.npy')
	eye = np.load('datasets/eye.npy')
	mouth = np.load('datasets/mouth.npy')
	nose = np.load('datasets/nose.npy')

	# add a column with labels
	ear = np.c_[ear, np.zeros(len(ear))]
	eye = np.c_[eye, np.ones(len(eye))]
	mouth = np.c_[mouth, 2*np.ones(len(mouth))]
	nose = np.c_[nose, 3*np.ones(len(nose))]

	# store the label codes in a dictionary
	label_dict = {0:'ear', 1:'eye', 2:'mouth', 3:'nose'}

	#PREPARE DATA FOR SCIKIT-LEARN

	X = np.concatenate((ear[:72500,:-1], eye[:72500,:-1], mouth[:72500,:-1], nose[:72500,:-1]), axis=0).astype('float32') # all columns but the last
	y = np.concatenate((ear[:72500,-1], eye[:72500,-1], mouth[:72500,-1], nose[:72500,-1]), axis=0).astype('float32') # the last column

	# train/test split (divide by 255 to obtain normalized values between 0 and 1)
	# I will use a 50:50 split, since I want to start by training the models on 5'000 samples and thus have plenty of samples to spare for testing.
	X_train, X_test, y_train, y_test = train_test_split(X/255.,y,test_size=0.2,random_state=0)

	# one hot encode outputs
	y_train_cnn = np_utils.to_categorical(y_train)
	y_test_cnn = np_utils.to_categorical(y_test)
	num_classes = y_test_cnn.shape[1]

	# reshape to be [samples][pixels][width][height]
	X_train_cnn = X_train.reshape(X_train.shape[0], 1, 28, 28).astype('float32')
	X_test_cnn = X_test.reshape(X_test.shape[0], 1, 28, 28).astype('float32')

	# build the model
	model = cnn_model()
	# Fit the model
	model.fit(X_train_cnn, y_train_cnn, validation_data=(X_test_cnn, y_test_cnn), epochs=30, batch_size=100)
	#save the model
	model.save("checkpoint_path/checkpoint_300K.h5")
	#model = load_model('my_model.h5')



