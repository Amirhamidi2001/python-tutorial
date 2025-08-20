# Matplotlib Markers

import matplotlib.pyplot as plt
import numpy as np


# Markers
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker="o")
plt.show()

# Format Strings fmt
plt.plot(ypoints, "o:r")
plt.show()

# Marker Size
plt.plot(ypoints, marker="o", ms=20)
plt.show()

# Marker Color mec
plt.plot(ypoints, marker="o", ms=20, mec="r")
plt.show()

# Marker Color mfc
plt.plot(ypoints, marker="o", ms=20, mfc="r")
plt.show()

plt.plot(ypoints, marker="o", ms=20, mec="#4CAF50", mfc="hotpink")
plt.show()
