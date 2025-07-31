# SciPy Statistical Significance Tests

import numpy as np
from scipy.stats import ttest_ind, kstest, describe, skew, kurtosis, normaltest


# T-Test
v1 = np.random.normal(size=100)
v2 = np.random.normal(size=100)
res = ttest_ind(v1, v2)
print(res)

# pvalue
res = ttest_ind(v1, v2).pvalue
print(res)

# KS-Test
v = np.random.normal(size=100)
res = kstest(v, "norm")
print(res)

# Statistical Description of Data
v = np.random.normal(size=100)
res = describe(v)
print(res)

# Kurtosis
v = np.random.normal(size=100)
print(skew(v))
print(kurtosis(v))

# normaltest
v = np.random.normal(size=100)
print(normaltest(v))
