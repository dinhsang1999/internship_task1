# intenship_task1

This repository uses MNIST digits dataset to demonstrate what I learned about projects organization and sourcecode management.

# Installation
```
conda create -n intenship_env python=3.6
conda activate intenship
```

# Install dependencies:
```
pip install -r requirements.txt
```

# Usage
- Run
```
python train.py
```
Expected output:
```
---------------------download dataset suceeded----------------
x_train shape: (60000, 28, 28, 1)
60000 train samples
10000 test samples
-------------preprocess suceeded-----------------
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #
=================================================================
conv2d (Conv2D)              (None, 26, 26, 32)        320
_________________________________________________________________
max_pooling2d (MaxPooling2D) (None, 13, 13, 32)        0
_________________________________________________________________
conv2d_1 (Conv2D)            (None, 11, 11, 64)        18496
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 5, 5, 64)          0
_________________________________________________________________
flatten (Flatten)            (None, 1600)              0
_________________________________________________________________
dropout (Dropout)            (None, 1600)              0
_________________________________________________________________
dense (Dense)                (None, 10)                16010
=================================================================
Total params: 34,826
Trainable params: 34,826
Non-trainable params: 0
_________________________________________________________________
--------get model suceeded------------
Epoch 1/15
2021-07-03 14:07:53.287701: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library libcublas.so.10
2021-07-03 14:07:53.402821: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library libcudnn.so.7
422/422 [==============================] - 2s 5ms/step - loss: 0.3671 - accuracy: 0.8858 - val_loss: 0.0860 - val_accuracy: 0.9757
Epoch 2/15
422/422 [==============================] - 2s 5ms/step - loss: 0.1121 - accuracy: 0.9661 - val_loss: 0.0631 - val_accuracy: 0.9825
Epoch 3/15
422/422 [==============================] - 2s 5ms/step - loss: 0.0865 - accuracy: 0.9733 - val_loss: 0.0505 - val_accuracy: 0.9867
Epoch 4/15
422/422 [==============================] - 2s 5ms/step - loss: 0.0738 - accuracy: 0.9772 - val_loss: 0.0431 - val_accuracy: 0.9882
Epoch 5/15
422/422 [==============================] - 2s 5ms/step - loss: 0.0634 - accuracy: 0.9801 - val_loss: 0.0387 - val_accuracy: 0.9897
Epoch 6/15
422/422 [==============================] - 2s 5ms/step - loss: 0.0562 - accuracy: 0.9819 - val_loss: 0.0381 - val_accuracy: 0.9900
Epoch 7/15
422/422 [==============================] - 2s 5ms/step - loss: 0.0507 - accuracy: 0.9834 - val_loss: 0.0372 - val_accuracy: 0.9907
Epoch 8/15
422/422 [==============================] - 2s 5ms/step - loss: 0.0483 - accuracy: 0.9856 - val_loss: 0.0343 - val_accuracy: 0.9915
Epoch 9/15
422/422 [==============================] - 2s 5ms/step - loss: 0.0437 - accuracy: 0.9862 - val_loss: 0.0310 - val_accuracy: 0.9917
Epoch 10/15
422/422 [==============================] - 2s 5ms/step - loss: 0.0419 - accuracy: 0.9869 - val_loss: 0.0322 - val_accuracy: 0.9910
Epoch 11/15
422/422 [==============================] - 2s 5ms/step - loss: 0.0406 - accuracy: 0.9867 - val_loss: 0.0354 - val_accuracy: 0.9910
Epoch 12/15
422/422 [==============================] - 2s 5ms/step - loss: 0.0386 - accuracy: 0.9876 - val_loss: 0.0299 - val_accuracy: 0.9922
Epoch 13/15
422/422 [==============================] - 2s 5ms/step - loss: 0.0354 - accuracy: 0.9891 - val_loss: 0.0317 - val_accuracy: 0.9922
Epoch 14/15
422/422 [==============================] - 2s 5ms/step - loss: 0.0347 - accuracy: 0.9881 - val_loss: 0.0314 - val_accuracy: 0.9920
Epoch 15/15
422/422 [==============================] - 2s 5ms/step - loss: 0.0309 - accuracy: 0.9899 - val_loss: 0.0293 - val_accuracy: 0.9915
```

- After the models are trained, run:
```
python test.py
```
for accuracy result

Expected output:
```
Test loss: 0.02708388678729534
Test accuracy: 0.991100013256073
```

