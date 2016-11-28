"""
General form linear regression with no optimization in python.
Learning rate and number of iterations hand selected through testing.
"""
import numpy as np

def compute_cost(ins, outs, params):
    return (1.0/(2*len(ins)))*np.sum((np.dot(ins, params) - outs)**2)


def update_params(alpha, ins, outs, params):
    for j in xrange(len(params)):
        params[j] -= alpha*(1.0/len(ins))*np.sum((np.dot(ins, params) - outs)*x[:, j])
    return


def linear_regression(ins, outs):
    # print "ins = {}".format(ins)
    # print "outs = {}".format(outs)
    params = np.zeros(len(ins[0]))
    alpha = 0.02
    for _ in xrange(17500):
        update_params(alpha, ins, outs, params)
    return params

feats, num_dp = map(int, raw_input().split())
data = [map(float, raw_input().split()) for _ in xrange(num_dp)]
# print "data read in: {}".format(data)
x = []
y = []
for p in data:
    x.append([1] + p[:-1])
    y.append(p[-1])

x = np.array(x)
y = np.array(y)
params = linear_regression(x, y)

num_test_cases = int(raw_input())
for _ in xrange(num_test_cases):
    inpt = map(float, raw_input().split())
    outpt = np.dot(params, np.array([1] + inpt))
    print "%.2f"%outpt
