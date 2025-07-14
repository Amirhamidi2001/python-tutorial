# Chi Square Distribution

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


# Chi Square Distribution
x = random.chisquare(df=2, size=(2, 3))
print(x)

# Visualization of Chi Square Distribution
sns.displot(random.chisquare(df=1, size=1000), kind="kde")
plt.show()
