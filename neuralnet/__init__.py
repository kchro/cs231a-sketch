import sys
sys.path.insert(0, 'neuralnet/')

from sketch_rnn_class import *
from model_class import Model
from svg_util import *

#load pathways
data_dir = 'neuralnet/datasets/'
models_root_dir = '' #same directory we're in now
model_dir = 'four_class_checkpoint/'

def load_trained_classifier():
    _, eval_hps_model, _ = load_model(model_dir)

    # construct the sketch-rnn model:
    reset_graph()
    eval_model = Model(eval_hps_model, reuse=tf.AUTO_REUSE)

    # run session
    sess = tf.InteractiveSession()
    sess.run(tf.global_variables_initializer())

    # load checkpoints
    load_checkpoint(sess, model_dir)

    # return session and evaluation model
    return sess, eval_model

class FeatureClassifier:
    def __init__(self, thresh=0):
        sess, eval_model = load_trained_classifier()
        self.sess = sess
        self.model = eval_model
        self.labels = ['ear', 'eye', 'mouth', 'nose']
        self.thresh = thresh

    def predict(self, stroke, verbose=False):
        dist = pred(self.sess, self.model, stroke, 125)[0]
        if verbose:
            print dist
        ind = predict_model(self.sess, self.model, stroke, 125)
        label = self.labels[ind]
        confidence = dist[ind]

        if confidence < self.thresh:
            return None, confidence
        if label == 'ear':
            return None, confidence

        return label, confidence

    def draw(self, stroke):
        draw_strokes(stroke)
