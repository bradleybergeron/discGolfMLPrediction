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

X2 = tf.constant([-7.0, -4.0, -1.0, 2.0, 5.0, 8.0, 11.0, 14.0])
y2 = tf.constant([3.0, 6.0, 9.0, 12.0, 15.0, 18.0, 21.0, 24.0])

plt.scatter(X2, y2)
plt.show()

input_shape = X2[0].shape
output_shape = y[0].shape

print(input_shape, output_shape)

print(X2[0], y[0])

#
# Steps in modelling with TensorFlow
#
tf.random.set_seed(42)

model = tf.keras.Sequential([
    tf.keras.layers.Dense(1)
])

model.compile(loss=tf.keras.losses.mae,
              optimizer=tf.keras.optimizers.SGD(),
              metrics=["mae"])

X2np = np.array(X2)
y2np = np.array(y2)
model.fit(tf.expand_dims(X2np, axis=-1), y2np, epochs=100)

print(X2np)
print(y2np)

pValue = np.array([17.0])
print(model.predict(pValue))


#
#
#

x = np.arange(-100, 100, 4)
y = np.arange(-90, 110, 4)
print(x)
print(y)
print(len(x))

xTrain = x[:40]
yTrain = y[:40]

xTest = x[40:]
yTest = y[40:]

print(len(xTrain), len(xTest))

plt.figure(figsize=(10,7))
plt.scatter(xTrain, yTrain, c='b', label='Training data')
plt.scatter(xTest, yTest, c='g', label='Testing data')
plt.legend()
plt.show()

tf.random.set_seed(42)

model=tf.keras.Sequential([
    #tf.keras.layers.Dense(1)
    tf.keras.layers.Dense(1, input_shape=[1])
])

model.compile(loss=tf.keras.losses.mae,
              optimizer=tf.keras.optimizers.SGD(),
              metrics=["mae"])

model.fit(xTrain, yTrain, epochs=100, verbose=0)

print(model.summary())

#from tensorflow.keras.utils import plot_model
#plot_model(model, show_shapes=True)

yPreds = model.predict(xTest)
print(yPreds)

def plot_predictions(train_data=xTrain,
                     train_labels=yTrain,
                     test_data=xTest,
                     test_labels=yTest,
                     predictions=yPreds):
  """
  Plots training data, test data and compares predictions.
  """
  plt.figure(figsize=(10, 7))
  # Plot training data in blue
  plt.scatter(train_data, train_labels, c="b", label="Training data")
  # Plot test data in green
  plt.scatter(test_data, test_labels, c="g", label="Testing data")
  # Plot the predictions in red (predictions were made on the test data)
  plt.scatter(test_data, predictions, c="r", label="Predictions")
  # Show the legend
  plt.legend()
  plt.show()

plot_predictions(train_data=xTrain,
                 train_labels=yTrain,
                 test_data=xTest,
                 test_labels=yTest,
                 predictions=yPreds)

print(model.evaluate(xTest, yTest))

mae = tf.metrics.mean_absolute_error(y_true=yTest,
                                     y_pred=yPreds)
print(f"mae: {mae}")
print(f"yTest: {yTest}")
print(f"yPreds: {yPreds}")
print(f"shapes: {yTest.shape}, {yPreds.shape}")

print(yPreds.squeeze().shape)

print(f"yTest: {yTest}, yPreds: {yPreds.squeeze()}")

mae = tf.metrics.mean_absolute_error(y_true=yTest,
                                     y_pred=yPreds.squeeze())
print(f"mae: {mae}")

mse = tf.metrics.mean_squared_error(y_true=yTest,
                                    y_pred=yPreds.squeeze())
print(f"mse: {mse}")


def mae(y_test, y_pred):
    """
    Calculuates mean absolute error between y_test and y_preds.
    """
    return tf.metrics.mean_absolute_error(y_test,
                                          y_pred)


def mse(y_test, y_pred):
    """
    Calculates mean squared error between y_test and y_preds.
    """
    return tf.metrics.mean_squared_error(y_test,
                                         y_pred)

#
# Running experiments to improve the model
#

tf.random.set_seed(42)

model1 = tf.keras.Sequential([
    tf.keras.layers.Dense(1)
])
model1.compile(loss=tf.keras.losses.mae,
               optimizer=tf.keras.optimizers.SGD(),
               metrics=['mae'])
model1.fit(tf.expand_dims(xTrain, axis=-1), yTrain, epochs=100)

yPreds1 = model1.predict(xTest)
plot_predictions(predictions=yPreds1)

mae1 = mae(yTest, yPreds1.squeeze()).numpy()
mse1 = mse(yTest, yPreds1.squeeze()).numpy()
print(f"model1: {mae1}, {mse1}")


tf.random.set_seed(42)

model2 = tf.keras.Sequential([
    tf.keras.layers.Dense(1),
    tf.keras.layers.Dense(1)
])

model2.compile(loss=tf.keras.losses.mae,
               optimizer=tf.keras.optimizers.SGD(),
               metrics=['mae'])

model2.fit(tf.expand_dims(xTrain, axis=-1), yTrain, epochs=100, verbose=0)

yPreds2 = model2.predict(xTest)
plot_predictions(predictions=yPreds2)

mae2 = mae(yTest, yPreds2.squeeze()).numpy()
mse2 = mse(yTest, yPreds2.squeeze()).numpy()
print(f"model2: {mae2}, {mse2}")


tf.random.set_seed(42)

model3 = tf.keras.Sequential([
    tf.keras.layers.Dense(1),
    tf.keras.layers.Dense(1)
])

model3.compile(loss=tf.keras.losses.mae,
               optimizer=tf.keras.optimizers.SGD(),
               metrics=['mae'])

model3.fit(tf.expand_dims(xTrain, axis=-1), yTrain, epochs=500, verbose=0)

yPreds3 = model3.predict(xTest)
plot_predictions(predictions=yPreds3)

mae3 = mae(yTest, yPreds3.squeeze()).numpy()
mse3 = mse(yTest, yPreds3.squeeze()).numpy()
print(f"model3: {mae3}, {mse3}")

model_results = [
    ["Model1", mae1, mse1],
    ["Model2", mae2, mse2],
    ["Model3", mae3, mse3]
]

import pandas as pd
allResults = pd.DataFrame(model_results, columns=["model", "mae", "mse"])
print(f"allResults:\n {allResults}")