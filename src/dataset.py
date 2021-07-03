import numpy as np
from tensorflow import keras
from tensorflow.keras import layers

def get_dataset():
	# the data, split between train and test sets
	(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
	print('---------------------download dataset suceeded----------------')
	return (x_train, y_train), (x_test, y_test)
