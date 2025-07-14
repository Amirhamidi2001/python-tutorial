# Zipf Distribution

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


# Zipf Distribution
x = random.zipf(a=2, size=(2, 3))
print(x)

# Visualization of Zipf Distribution
x = random.zipf(a=2, size=1000)
sns.displot(x[x < 10])
plt.show()
