"""
Here are the test scores of 10 students in physics and history:

Physics Scores  15  12  8   8   7   7   7   6   5   3
History Scores  10  25  17  11  13  17  20  13  9   15
Compute the slope of the line of regression obtained while treating Physics as the independent variable. Compute the answer correct to three decimal places.

Output Format

In the text box, enter the floating point/decimal value required. Do not leave any leading or trailing spaces. Your answer may look like: 0.255

This is NOT the actual answer - just the format in which you should provide your answer.
"""

import math


def mean(nums):
    return float(sum(nums))/len(nums)


def center_data(nums):
    m = mean(nums)
    return [(n - m) for n in nums]


def variance(nums):
    m = mean(nums)
    variance = mean([(n - m)**2 for n in nums])
    return variance


def standard_deviation(nums):
    stdev = math.sqrt(variance(nums))
    return stdev


def correlation(X, Y):  # pearson's correlation
    assert len(X) == len(Y)
    x = center_data(X)
    y = center_data(Y)
    top = sum([x[i]*y[i] for i in xrange(len(x))])
    bottom = math.sqrt(sum([n**2 for n in x])*sum([n**2 for n in y]))
    return float(top)/bottom

physics = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
history = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]
slope = correlation(physics, history)*standard_deviation(history)/standard_deviation(physics)
print "%.3f"%slope
