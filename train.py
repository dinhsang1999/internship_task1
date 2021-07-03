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
(x_train, y_train), (_, _) = preprocess(x_train, y_train, x_test, y_test, num_classes)
model = get_model(input_shape, num_classes)

batch_size = 128
epochs = 15

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=0.1)

model.save("minst_model")
