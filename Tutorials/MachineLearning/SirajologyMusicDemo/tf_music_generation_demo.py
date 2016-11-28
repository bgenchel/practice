# Generate Music in TensorFlow
# https://www.youtube.com/watch?v=ZE7qWXX05T0

import numpy as np
import pandas as pd
import tensorflow as tf
from tqdm import tqdm
import midi_manipulation
from rbm_chords import *

## 4 steps to generate music! (Using restricted boltzmann machine)

##############################
### Step 1 - HyperParameters
##############################
lowest_note = midi_manipulation.lowerBound
highest_note = midi_manipulation.upperBound
note_range = highest_note - lowest_note

# number of timesteps that we will create at a time
num_timesteps = 15
# this is the size of the visible layer
n_visible = 2*note_range*num_timesteps
# this is the size of the hidden layer
n_hidden = 50

# the number of training epochs that we are going to run.
# for each epoch, we go through the entire data set
num_epochs = 200

# the number of training examples that we are going to send through the
# RBM at a time.
batch_size = 100

# the learning rate of our model
lr = tf.constant(0.005, tf.float32)

##################################
### Step 2 - Tensorflow Variables
##################################

# the placeholder variable that holds our data
x = tf.placeholder(tf.float32, [None, n_visible], name='x')
# the weight matrix that stores the edge weights
W = tf.Variable(tf.random_normal([n_visible, n_hidden], 0.01), name="W")
# the bias vector for the hidden layer
bh = tf.Variable(tf.zeros([1, n_hidden], tf.float32, name="bh"))
# the bias vector for the visible layer
bv = tf.Variable(tf.zeros([1, n_visible], tf.float32, name="bv"))

######################################
### Step 3 - Our Generative Algorithm
######################################

# the sample of x
x_sample = gibbs_sample(1)
# the sample of the hidden nodes, starting from the visible state of x
h = sample(tf.sigmoid(tf.matmul(x, W) + bh))
# the sample of the hidden nodes, starting from the visible state of x_sample
h_sample = sample(tf.sigmoid(tf.matmul(x_sample, W) + bh))

# Next we update the values of W, bh, and bv;
# based on the difference between the samples that
# we drew and the original values
size_bt = tf.cast(tf.shape(x)[0], tf.float32)
W_adder = tf.mul(
    lr/size_bt,
    tf.sub(
        tf.matmul(tf.transpose(x), h),
        tf.matmul(tf.transpose(x_sample), h_sample)
    )
)
bv_adder = tf.mul(lr/size_bt, tf.reduce_sum(tf.sub(x, x_sample), 0, True))
bh_adder = tf.mul(lr/size_bt, tf.reduce_sum(tf.sub(h, h_sample), 0, True))

# When we do sess.run(updt), TensorFlow will run all 3 update steps
update = [W.assign_add(W_adder), bv.assign_add(bv_adder), bh.assign_add(bh_adder)]


###############################################
### Step 4 (Final) - Run the Computation Graph
###############################################
with tf.Session() as sess:
    # initialize the variables of the model
    init = tf.initialize_all_variables()
    sess.run(init)
    # Run through all of the training data num_epochs times
    for epoch in tqdm(range(num_epochs)):
        for song in songs:
            # the songs are stored in a time x notes format.
            # the size of each song is timesteps_in_song x 2*note_range
            # Here we reshape the songs so that each training example
            # is a vector with num_timesteps x 2*note_range elements
            song = np.array(song)
            # train the RBM on batch_size samples at a time
            for i in range(1, len(song), batch_size):
                tr_x = song[i:i+batch_size]
                sess.run(update, feed_dict={x: tr_x})

    # now the model is fully trained, so let's make some music!
    # run a gibbs chain where the visible nodes are initialized to 0
    sample = gibbs_sample(1).eval(session=sess, feed_dict={x: np.zeros((10, n_visible))})
    for i in range(sample.shape[0]):
        if not any(sample[i, :]):
            continue
        # Here we reshape the vector to be time x notes, and
        # then save the vector as a midi file.
        S = np.reshape(sample[i, :], (num_timesteps, 2*note_range))
        midi_manipulation.noteStateMatrixToMidi(S, "generated_chord{}".format(i))
