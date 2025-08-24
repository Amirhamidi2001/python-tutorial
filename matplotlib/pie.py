# Matplotlib Pie Charts

import matplotlib.pyplot as plt
import numpy as np


# Creating Pie Charts
y = np.array([35, 25, 25, 15])
plt.pie(y)
plt.show()

# Labels
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.pie(y, labels=mylabels)
plt.show()

# Start Angle
plt.pie(y, labels=mylabels, startangle=90)
plt.show()

# Explode
myexplode = [0.2, 0, 0, 0]
plt.pie(y, labels=mylabels, explode=myexplode)
plt.show()

# Shadow
plt.pie(y, labels=mylabels, explode=myexplode, shadow=True)
plt.show()

# Colors
mycolors = ["black", "hotpink", "b", "#4CAF50"]
plt.pie(y, labels=mylabels, colors=mycolors)
plt.show()

# Legend
plt.pie(y, labels=mylabels)
plt.legend()
plt.show()

# Legend With Header
plt.pie(y, labels=mylabels)
plt.legend(title="Four Fruits:")
plt.show()
