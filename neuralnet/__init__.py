import sys
sys.path.insert(0, 'neuralnet/')

from sketch_rnn_class import *
from model_class import Model

#load pathways
data_dir = 'neuralnet/datasets/'
models_root_dir = '' #same directory we're in now
model_dir = 'four_class_checkpoint/'

def load_trained_classifier():
    # print 'loading datasets...'
    # _, _, test_set, _, eval_hps_model, _ = load_env(data_dir, model_dir)
    # print 'loaded datasets.'

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
