# Intro to Deep Learning 
from tensorflow import keras
from tensorflow.keras import layers

# Create a network with 1 linear unit
model = keras.Sequential([
    layers.Dense(units=1, input_shape=[3])
])
model.summary()
#from tensorflow import keras
#from tensorflow.keras import layers

# 3 features in your input vector -> shape=(3,)
#model = keras.Sequential([
#    keras.Input(shape=(3,)),
#    layers.Dense(1)          # one linear unit
#])

#model.summary()
