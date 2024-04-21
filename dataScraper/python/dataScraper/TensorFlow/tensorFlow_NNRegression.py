#
# https://dev.mrdbourke.com/tensorflow-deep-learning/01_neural_network_regression_in_tensorflow/
#

import tensorflow as tf
print(tf.__version__)

import datetime
print(f"Notebook last run (end-to-end): {datetime.datetime.now()}")

import numpy as np
import matplotlib.pyplot as plt

x = np.array([-7.0, -4.0, -1.0, 2.0, 5.0, 8.0, 11.0, 14.0])
y = np.array([3.0, 6.0, 9.0, 12.0, 15.0, 18.0, 21.0, 24.0])

plt.scatter(x,y)
plt.show()

house_info = tf.constant(['bedroom', 'bathroom', 'garage'])
house_price = tf.constant([939700])
print(house_info, house_price)

print(house_info.shape)

x2 = tf.constant([-7.0, -4.0, -1.0, 2.0, 5.0, 8.0, 11.0, 14.0])
y2 = tf.constant([3.0, 6.0, 9.0, 12.0, 15.0, 18.0, 21.0, 24.0])

plt.scatter(x2, y2)
plt.show()

input_shape = x[0].shape
output_shape = y[0].shape

print(input_shape, output_shape)

print(x[0], y[0])
