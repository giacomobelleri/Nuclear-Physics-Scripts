import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import functions.nuclearfunc as nf

# Magnetic moment of nucleus:
[A, Z] = [43, 20]
[j, l] = [7*0.5, 5]
# mag_moment = round(nf.MagneticDipoleMoment(A, Z, j, l, s), 2)
mag_moment = nf.MagneticDipoleMoment(A, Z, j, l)
print(f"For a Nucleus with A = {A}, Z = {Z}, j = {j} and l = {l}:\n" +
      f"--Magnetic moment: {mag_moment} mu_N \n")

# Mass of electron
m_e = 9.11*10**(-31)  # kg
# Charge of electron
e = 1.602*10**(-19)  # C

B = 1  # T

# Magnetic resonance frequency
w = mag_moment*e*B/((2*m_e)*7/2)
print(w*10**(-14)/(2*np.pi))