import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import functions.nuclearfunc as nf

# Computes Binding energy and mass for specific nucleus:
A = 4
Z = 2
print(f"For a Nucleus with A = {A} and Z = {Z}:\n"
      f"--Binding energy:  {nf.BindingEnergy(A,Z)} MeV \n" +
      f"--Nuclear mass:    {nf.NuclearMass(A,Z)} MeV/c^2 \n")

# Computes Q-Value of alpha decay for nuclei that adhere to SEMF
[A_i, Z_i] = [212, 84]
[A_f, Z_f] = [208, 82]
m_alpha = 4.00260325413 # MeV/c^2
m_u = 931.49410242 # MeV/c^2
Q = nf.NuclearMass(A_i, Z_i) - (nf.NuclearMass(A_f, Z_f) + m_alpha*m_u)
print(f"({A_i}, {Z_i}) --> ({A_f}, {Z_f}) + (4, 2)\n" +
      f"--Q-Value: {Q} MeV \n")

# Computes Q-Value of symmetric fission decay for nuclei that adhere to the SEMF
[A_i, Z_i] = [212, 84]
Q = nf.NuclearMass(A_i, Z_i) - 2*nf.NuclearMass(A_i/2, Z_i/2)
print(f"({A_i}, {Z_i}) --> ({A_f/2}, {Z_f/2}) + ({A_f/2}, {Z_f/2})\n" +
      f"--Q-Value: {Q} MeV \n")
