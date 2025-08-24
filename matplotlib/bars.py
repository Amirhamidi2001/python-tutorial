# Matplotlib Bars

import matplotlib.pyplot as plt
import numpy as np


# Creating Bars
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.bar(x, y)
plt.show()

# Horizontal Bars
plt.barh(x, y)
plt.show()

# Bar Color
plt.bar(x, y, color="red")
plt.show()

# Color Names
plt.bar(x, y, color="hotpink")
plt.show()

# Color Hex
plt.bar(x, y, color="#4CAF50")
plt.show()

# Bar Width
plt.bar(x, y, width=0.1)
plt.show()

# Bar Height
plt.barh(x, y, height=0.1)
plt.show()
