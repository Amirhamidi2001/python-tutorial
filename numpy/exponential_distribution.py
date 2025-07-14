# Exponential Distribution

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


# Exponential Distribution
x = random.exponential(scale=2, size=(2, 3))
print(x)

# Visualization of Exponential Distribution
sns.displot(random.exponential(size=1000), kind="kde")
plt.show()
