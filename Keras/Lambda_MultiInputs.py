from keras.layers import Dense, Input, concatenate, Reshape, Embedding, Activation, Dropout, GRU, Flatten, LSTM
from keras.layers.core import Lambda
from keras import backend as K
import tensorflow as tf

# GPU config
from keras.backend.tensorflow_backend import set_session
config = tf.ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.3
set_session(tf.Session(config=config))

# since there is no parameter needed to be estimated from data, so just put all the inputs into a list
# and get every elment from list.
# Notice that the elment should be tensor

def concat_test(input,axis):
    a = input[0]
    b = input[1]
    return K.concatenate([a, b], axis=axis)

var_1 = Input(shape=(1,))
var_2 = Input(shape=(2,))

var = Lambda(concat_test, name='concat_test', arguments={'axis': 1})([var_1, var_2])

model = Model(inputs=[var_1, var_2], outputs=[var])
model.compile(optimizer='adam', loss='mse')

print(model.summary())
