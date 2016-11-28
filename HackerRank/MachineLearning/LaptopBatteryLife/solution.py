# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import numpy as np

def compute_cost(ins, outs, params):
    return (1.0/(2*len(ins)))*np.sum((np.dot(ins, params) - outs)**2)
    
def update_params(alpha, ins, outs, params):
    for j in xrange(len(params)):
        params[j] -= alpha*(1.0/len(ins))*np.sum((np.dot(ins, params) - outs)*x[:, j])
    return
    
def linear_regression(ins, outs):
    params = np.zeros(2)
    alpha = 0.01
    for _ in xrange(4000):
        update_params(alpha, ins, outs, params)
    return params
    
x = []
y = []
data = [map(float, line.strip().split(',')) for line in open('trainingdata.txt', 'r').readlines()]
for p in data:
    if p[1] == 8.0:
        continue
    x.append([1, p[0]])
    y.append(p[1])
    
x = np.array(x)
y = np.array(y)
params = linear_regression(x, y)

inpt = float(sys.stdin.readline())
outpt = np.dot(params, np.array([1, inpt]))
print "%.2f"%(outpt, 8.0)[outpt > 8.0]

