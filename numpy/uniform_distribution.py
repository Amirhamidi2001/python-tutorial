# Uniform Distribution

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


# Uniform Distribution
x = random.uniform(size=(2, 3))
print(x)

# Visualization of Uniform Distribution
sns.displot(random.uniform(size=1000), kind="kde")
plt.show()
