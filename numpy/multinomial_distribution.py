# Multinomial Distribution

from numpy import random


# Multinomial Distribution
x = random.multinomial(n=6, pvals=[1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6])
print(x)
