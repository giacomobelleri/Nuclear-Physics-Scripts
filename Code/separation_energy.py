import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import functions.nuclearfunc as nf

# Neutron and Proton separation energy
A = 40
Z = 20
S_n = nf.BindingEnergy(A,Z) - nf.BindingEnergy(A-1,Z)
S_p = nf.BindingEnergy(A,Z) - nf.BindingEnergy(A-1,Z-1)
S_n_predicted = 15.6
S_p_predicted = 8.3
print(f"For a Nucleus with A = {A} and Z = {Z}:\n" + 
      f"--Calculated Neutron separation energy: {round(S_n, 1)} MeV \n" +
      f" --> Difference from predicted value: {round(S_n - S_n_predicted, 1)} MeV \n"
      f"--Calculated Proton separation energy:  {round(S_p, 1)} MeV \n" + 
      f" --> Difference from predicted value: {round(S_p - S_p_predicted, 1)} MeV \n")