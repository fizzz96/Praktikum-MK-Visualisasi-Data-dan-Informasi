import matplotlib.pyplot as plt
import numpy as np

# a) data acak 1000 titik
x = np.random.rand(1000)
y = np.random.rand(1000)

# b) 5x5 inch
fig, ax = plt.subplots(figsize=(5, 5))
# c) scatter plot
ax.scatter(x, y, color='purple', alpha=0.6)
# e) judul & grid
ax.set_title("Scatter Plot Data Acak")
ax.grid(True)

plt.savefig('scatte_plot.png', dpi=300) # d) save 300 dpi
plt.show()
