import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from src.dataset import get_dataset
from src.utils import preprocess
from src.model import get_model


# Model / data parameters
num_classes = 10
input_shape = (28, 28, 1)

(x_train, y_train), (x_test, y_test) = get_dataset()
(_, _), (x_test, y_test) = preprocess(x_train, y_train, x_test, y_test, num_classes)

model = keras.models.load_model('minst_model')
score = model.evaluate(x_test, y_test, verbose=0)

print("Test loss:", score[0])
print("Test accuracy:", score[1])
