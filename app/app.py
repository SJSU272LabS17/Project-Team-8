from flask import Flask, render_template, request, redirect, url_for
from werkzeug import secure_filename
import os

from keras.models import model_from_json
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD
from keras.utils import np_utils, generic_utils
import auTool
genres = ['Blues','Classical','Country','Disco','Hip-hop','Jazz','Metal','Pop','Reggae','Rock']

UPLOAD_FOLDER = 'upload'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__,)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    data = request.get_data()
    track = auTool.Au('example/'+data+'.au')
    feat = np.reshape(track.feat(),(1,156))
    classes = model.predict_classes(feat, batch_size=32)
    result = genres[classes[0]]
    print result
    return result

@app.route('/upload', methods=['POST'])
def upload():
#    print request.files.filename()
#    upload_file.save(os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], filename))
    f = request.files['file']
    fname = secure_filename(f.filename)
    f.save(os.path.join(UPLOAD_FOLDER, fname))
    track = auTool.Au('upload/'+ fname)
    feat = np.reshape(track.feat(),(1,156))
    classes = model.predict_classes(feat, batch_size=32)
    result = genres[classes[0]]
    print result
    return result



if __name__ == '__main__':
    model = Sequential()
    # model = model_from_json(open('model/my_model_architecture.json').read())
    model.add(Dense(200, input_dim=156, kernel_initializer='uniform'))
    model.add(Activation('tanh'))
    model.add(Dropout(0.5))
    model.add(Dense(50, kernel_initializer='uniform'))
    model.add(Activation('tanh'))
    model.add(Dense(100, kernel_initializer='uniform'))
    model.add(Activation('tanh'))
    model.add(Dropout(0.5))
    model.add(Dense(10, kernel_initializer='uniform'))
    model.add(Activation('softmax'))

    sgd = SGD(lr=0.0001, decay=1e-6, momentum=0.9, nesterov=True)
    model.compile(loss='categorical_crossentropy',
                  optimizer=sgd)

    # model.save_weights('model/dummy_weights.h5')
    model.load_weights('model/my_model_weights.h5')
    print 'Model loaded'
    app.debug = True
    app.run(threaded=True)
