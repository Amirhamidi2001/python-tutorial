# Normal (Gaussian) Distribution

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


# Normal Distribution
x = random.normal(size=(2, 3))
print(x)

x = random.normal(loc=1, scale=2, size=(2, 3))
print(x)

# Visualization of Normal Distribution
sns.displot(random.normal(size=1000), kind="kde")
plt.show()
