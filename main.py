import numpy as np
from scipy.stats import poisson

hours = 1
simulation_len = hours * 60 # in minutes
patients_per_minute = poisson.rvs(mu=0.3, size=simulation_len) # approx 0.3 patients per minute at Charing Cross Hospital

values, counts = np.unique(patients_per_minute, return_counts=True)
print(values, counts)


# for current_min in range(0, simulation_len):
    