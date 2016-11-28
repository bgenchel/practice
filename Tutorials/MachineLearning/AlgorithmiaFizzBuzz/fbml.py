from sklearn.preprocessing import LabelBinarizer
from sklearn.linear_model import LogisticRegression
import numpy as np
import pickle

import Algorithmia
client = Algorithmia.client()

WINDOW_SIZE = 15


def fizz_buzz(i):
    return ("i", "Fizz", "Buzz", "FizzBuzz")[(not i%3) + (not i%5)*2]


def build_samples(samples):
    padding = ['PAD']*WINDOW_SIZE
    for i in xrange(len(samples) - WINDOW_SIZE - 1):
        yield [padding + samples[max(0, i - WINDOW_SIZE):i], samples[i]]
        padding = padding[1:]


def learn():
    num_samples = 15000
    fizzbuzz_samples = [fizz_buzz(i) for i in range(1, num_samples+1)]
    print fizzbuzz_samples
    print "creating data set from samples ..."
    data = list(build_samples(fizzbuzz_samples))
    print "done."

    print "creating binarizer ..."
    lb = LabelBinarizer()
    lb.fit(fizzbuzz_samples + ['PAD'])
    print "done."

    print "transforming dataset for input ..."
    X = np.array([np.array(lb.transform(x)).flatten() for x, y in data])  # flatten may not be necessary
    Y = np.array([y for x, y in data])
    print "done."

    print "dividing data into train and test ..."
    X_train, X_test, Y_train, Y_test = X[0:10000], X[10000:15000], Y[0:10000], Y[10000:15000]
    print "done."

    # Learn a simple logistic regression classifier
    print "training classifier ..."
    classifier = LogisticRegression(tol=1e-6)
    classifier.fit(X_train, Y_train)
    print "done."

    print "\nscore on test set: {}".format(classifier.score(X_test, Y_test))

    # save (pickle) sklearn entities
    with open('binarizer.pkl', 'wb') as binarizer_file:
        pickle.dump(lb, binarizer_file)

    with open('classifier.pkl', 'wb') as classifier_file:
        pickle.dump(classifier, classifier_file)

if __name__ == '__main__':
    learn()
