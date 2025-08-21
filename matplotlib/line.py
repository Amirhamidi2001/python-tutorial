# Matplotlib Line

import matplotlib.pyplot as plt
import numpy as np


# Linestyle
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, linestyle="dotted")
plt.show()

plt.plot(ypoints, linestyle="dashed")
plt.show()

# Shorter Syntax
plt.plot(ypoints, ls=":")
plt.show()

# Line Color
plt.plot(ypoints, color="r")
plt.show()

plt.plot(ypoints, c="#4CAF50")
plt.show()

plt.plot(ypoints, c="hotpink")
plt.show()

# Line Width
plt.plot(ypoints, linewidth="20.5")
plt.show()

# Multiple Lines

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)
plt.show()
