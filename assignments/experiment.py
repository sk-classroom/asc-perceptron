# %% Load the penguin data
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
from assignment import *

# %% Creating an instance of the Perceptron class with learning rate 0.1 and 100 iterations

# %% Load the penguin data


# %% Draw the decision regions by using `plot_decision_regions` function from utils.property

fig, ax = plt.subplots(figsize=(5, 5))

plot_decision_regions(X, y, classifier=model)

# Add the x and y axis labels!!!
plt.xlabel("...")
plt.ylabel("...")

# Save the figure as png
fig.savefig("../figs/decision_region.png", dpi=300)
