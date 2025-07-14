# Pareto Distribution

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


# Pareto Distribution
x = random.pareto(a=2, size=(2, 3))
print(x)

# Visualization of Pareto Distribution
sns.displot(random.pareto(a=2, size=1000))
plt.show()
