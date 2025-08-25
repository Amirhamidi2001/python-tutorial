# Machine Learning - Mean Median Mode

import numpy
from scipy import stats

# Mean, Median, and Mode
speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

# Mean
x = numpy.mean(speed)
print(x)

# Median
x = numpy.median(speed)
print(x)

# Mode
x = stats.mode(speed)
print(x)
