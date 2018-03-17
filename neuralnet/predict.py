# import the required libraries
import numpy as np
import time
import random
import cPickle
import codecs
import collections
import os
import math
import json
import tensorflow as tf
from six.moves import xrange
from sketch_rnn_class import *
from model_class import *
from utils_class import *
from rnn import *
# os.environ["CUDA_VISIBLE_DEVICES"]="1"
# libraries required for visualisation:
from IPython.display import SVG, display
import svgwrite # conda install -c omnia svgwrite=1.1.6
import PIL
from PIL import Image
import matplotlib.pyplot as plt
# set numpy output to something sensible
np.set_printoptions(precision=8, edgeitems=6, linewidth=200, suppress=True)
tf.logging.info("TensorFlow Version: %s", tf.__version__)

#HELPER FUNCTIONS
#function that displays vector images and saves them to .svg
def draw_strokes(data, factor=0.2, svg_filename = '/tmp/sketch_rnn/svg/sample.svg'):
  tf.gfile.MakeDirs(os.path.dirname(svg_filename))
  min_x, max_x, min_y, max_y = get_bounds(data, factor)
  dims = (50 + max_x - min_x, 50 + max_y - min_y)
  dwg = svgwrite.Drawing(svg_filename, size=dims)
  dwg.add(dwg.rect(insert=(0, 0), size=dims,fill='white'))
  lift_pen = 1
  abs_x = 25 - min_x 
  abs_y = 25 - min_y
  p = "M%s,%s " % (abs_x, abs_y)
  command = "m"
  for i in xrange(len(data)):
    if (lift_pen == 1):
      command = "m"
    elif (command != "l"):
      command = "l"
    else:
      command = ""
    x = float(data[i,0])/factor
    y = float(data[i,1])/factor
    lift_pen = data[i, 2]
    p += command+str(x)+","+str(y)+" "
  the_color = "black"
  stroke_width = 1
  dwg.add(dwg.path(p).stroke(the_color,stroke_width).fill("none"))
  dwg.save()
  display(SVG(dwg.tostring()))

# generate a 2D grid of many vector drawings
def make_grid_svg(s_list, grid_space=10.0, grid_space_x=16.0):
  def get_start_and_end(x):
    x = np.array(x)
    x = x[:, 0:2]
    x_start = x[0]
    x_end = x.sum(axis=0)
    x = x.cumsum(axis=0)
    x_max = x.max(axis=0)
    x_min = x.min(axis=0)
    center_loc = (x_max+x_min)*0.5
    return x_start-center_loc, x_end
  x_pos = 0.0
  y_pos = 0.0
  result = [[x_pos, y_pos, 1]]
  for sample in s_list:
    s = sample[0]
    grid_loc = sample[1]
    grid_y = grid_loc[0]*grid_space+grid_space*0.5
    grid_x = grid_loc[1]*grid_space_x+grid_space_x*0.5
    start_loc, delta_pos = get_start_and_end(s)

    loc_x = start_loc[0]
    loc_y = start_loc[1]
    new_x_pos = grid_x+loc_x
    new_y_pos = grid_y+loc_y
    result.append([new_x_pos-x_pos, new_y_pos-y_pos, 0])

    result += s.tolist()
    result[-1][2] = 1
    x_pos = new_x_pos+delta_pos[0]
    y_pos = new_y_pos+delta_pos[1]
  return np.array(result)

def encode(input_strokes):
	strokes = to_big_strokes(input_strokes,max_len=125).tolist()
	print(np.shape(strokes))
	strokes.insert(0, [0, 0, 1, 0, 0])
	seq_len = [len(input_strokes)]
	draw_strokes(to_normal_strokes(np.array(strokes)))
	return sess.run(eval_model.batch_z, feed_dict={eval_model.input_data: [strokes], eval_model.sequence_lengths: seq_len})[0]

def decode(z_input=None, draw_mode=True, temperature=0.1, factor=0.2):
  z = None
  if z_input is not None:
    z = [z_input]
  sample_strokes, m = sample(sess, sample_model, seq_len=eval_model.hps.max_seq_len, temperature=temperature, z=z)
  strokes = to_normal_strokes(sample_strokes)
  if draw_mode:
    draw_strokes(strokes, factor)
  return strokes

#preprocess a single stroke (a single drawing)
def preprocess_single(stroke, scale_factor = 46.5):
	stroke[:, 0:2] /= scale_factor
	return stroke



if __name__ == '__main__':
	#load pathways
	data_dir = 'datasets/'
	models_root_dir = '' #same directory we're in now
	model_dir = 'checkpoint_path/classifier'
	[train_set, valid_set, test_set, hps_model, eval_hps_model, sample_hps_model] = load_env(data_dir, model_dir)
	# construct the sketch-rnn model:
	reset_graph()
	model = Model(hps_model)
	eval_model = Model(eval_hps_model, reuse=True)
	sample_model = Model(sample_hps_model, reuse=True)
	#run session
	sess = tf.InteractiveSession()
	sess.run(tf.global_variables_initializer())
	# loads the weights from checkpoint into our model
	load_checkpoint(sess, model_dir)

	#SAMPLE CLASSIFICATIONS:
	#Single Classification
	'''
	stroke = test_set.random_sample()
	#produces drawing and saves it to filename
	draw_strokes(stroke, "test.svg")
	prediction = predict_model(sess, eval_model, stroke, 125)
	print(prediction)
	'''
	#Test Set
	'''

	'''









