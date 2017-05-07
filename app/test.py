from keras.models import model_from_json
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD
from keras.utils import np_utils, generic_utils
import auTool

model = Sequential()
model = model_from_json(open('model/my_model_architecture.json').read())
model.load_weights('model/my_model_weights.h5')
f = auTool.Au('example/rock.00000.au')
feat = np.reshape(f.feat(),(1,156))
classes = model.predict_classes(feat, batch_size=32)
genres = ['blues','classical','country','disco','hiphop','jazz','metal','pop','reggae','rock']
print genres[classes[0]]
