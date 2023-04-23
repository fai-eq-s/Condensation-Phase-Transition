import pandas as pd
import numpy as np

# Read the CSV file
df = pd.read_csv('cpt_mass_dist_rho=0.2.csv')

exp_m1 = np.exp(-0.1732*df['m'])
exp_m2 = np.exp(-0.19*df['m'])
df['exp_m1'] = exp_m1
df['exp_m2'] = exp_m2


# Write the updated DataFrame back to a new CSV file
df.to_csv('cpt_mass_dist_rho=0.2.csv', index=False)