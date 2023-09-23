import numpy as np
import functions.nuclearfunc as nf

# Sets up data
proton_energies = np.array([3.50, 3.54, 3.85, 4.93, 6.23, 6.61, 7.53, 8.19])
theta = np.pi/2
M = 9326.772227
E_i = 10.02 

# Computes energy spacing wrt ground state
delta_E = nf.ProtonScattering(E_i, proton_energies, M, theta)

# Prints results
print(f"For an initial energy E_i = {E_i} MeV we have that: \n {delta_E}\n")