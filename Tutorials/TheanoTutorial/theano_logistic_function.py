#logistic Function tutorial
import theano
from theano import tensor as T 


x = T.dmatrix('x')
s = 1/(1 + T.exp(-x))

logistic = function([x], s)
logistic([0, 1], [-1, -2])



