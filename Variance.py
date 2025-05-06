# Import the necessary library
import numpy as np

# Create a list of the given values
values = [45000, 36000, 63000, 47000, 50000, 65000, 41000, 48000, 42000]

# Calculate the variance using numpy's var function
variance = np.var(values, ddof=0)

# Print the variance
print("Variance:", variance)
input("Press ENTER to exit")
