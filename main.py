import numpy as np
from scipy.stats import poisson
from generate_patient import gen_patient
from agentic import agentic_decision

hours = 1
simulation_len = hours * 60 # in minutes
patients_per_min = poisson.rvs(mu=0.3, size=simulation_len) # approx 0.3 patients per minute at Charing Cross Hospital

values, counts = np.unique(patients_per_min, return_counts=True)
print(values, counts)

current_order = [] #ordered list of strings representing each patient

for current_min, patients_this_min in enumerate(patients_per_min): # Current time index and how many patients in that minute
    for patient_min_idx in range(0,patients_this_min): # Loop through each new patient this minute
        patient_prompt = gen_patient()
        new_order = agentic_decision(current_order, patient_prompt)
        current_order = new_order
    # PLACEHOLDER
    # Code that allocates patients to doctors etc
        



    