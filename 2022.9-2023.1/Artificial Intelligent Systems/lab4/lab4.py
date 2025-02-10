import numpy as np
from keras import losses
from keras.layers import Input, Dense
from keras.models import Model
import matplotlib.pyplot as plt


np.random.seed(1024)


def get_data(startvalue_of_x, endValue_of_x, step_value, function):
    dataX = np.arange(startvalue_of_x, endValue_of_x, step_value)
    dataX = dataX.reshape(len(dataX), 1)
    dataY = function(dataX)
    return dataX, dataY


def get_dense_model(unitsCount, activationFunction):
    input = Input(shape=(1, ), name="input")
    dense = Dense(units=unitsCount,
                  name="dense",
                  activation=activationFunction)(input)
    output = Dense(units=1, name="denseOutput")(dense)
    model = Model(input, output)
    return model


def fun1(x):
    return np.absolute(np.sin(x))


def run_train_and_test(startvalue_of_x, endValue_of_x, step_value, function,
                       unitsCount, activationFunctionName):
    X, Y = get_data(startvalue_of_x, endValue_of_x, step_value, function)
    model = get_dense_model(unitsCount, activationFunctionName)
    model.compile(optimizer="adam",
                  loss=losses.mean_squared_error,
                  metrics=[losses.mean_absolute_error])
    model.fit(X, Y, batch_size=50, epochs=20000)

    result = model.predict(X)
    plt.plot(X, Y)
    plt.plot(X, result, '--')
    plt.show()


if __name__ == "__main__":
    run_train_and_test(-6.3, 6.3, 0.01, fun1, 100, "relu")
