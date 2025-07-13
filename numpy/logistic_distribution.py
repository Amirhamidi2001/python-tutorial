# Logistic Distribution

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


# Logistic Distribution
x = random.logistic(loc=1, scale=2, size=(2, 3))
print(x)

# Visualization of Logistic Distribution
sns.displot(random.logistic(size=1000), kind="kde")
plt.show()

# Difference Between Logistic and Normal Distribution
data = {
    "normal": random.normal(scale=2, size=1000),
    "logistic": random.logistic(size=1000),
}
sns.displot(data, kind="kde")
plt.show()
