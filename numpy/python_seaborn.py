# Seaborn

import matplotlib.pyplot as plt
import seaborn as sns


# Plotting a Displot
sns.displot([0, 1, 2, 3, 4, 5])
plt.show()

# Plotting a Displot Without the Histogram
sns.displot([0, 1, 2, 3, 4, 5], kind="kde")
plt.show()
