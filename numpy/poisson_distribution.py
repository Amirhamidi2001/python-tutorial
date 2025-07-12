# Poisson Distribution

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


# Poisson Distribution
x = random.poisson(lam=2, size=10)
print(x)

# Visualization of Poisson Distribution
sns.displot(random.poisson(lam=2, size=1000))
plt.show()

# Difference Between Normal and Poisson Distribution
data = {
    "normal": random.normal(loc=50, scale=7, size=1000),
    "poisson": random.poisson(lam=50, size=1000),
}
sns.displot(data, kind="kde")
plt.show()

# Difference Between Binomial and Poisson Distribution
data = {
    "binomial": random.binomial(n=1000, p=0.01, size=1000),
    "poisson": random.poisson(lam=10, size=1000),
}
sns.displot(data, kind="kde")
plt.show()
