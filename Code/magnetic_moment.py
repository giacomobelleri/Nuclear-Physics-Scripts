import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import functions.nuclearfunc as nf

# Magnetic moment of nucleus:
[A, Z] = [197, 79]
[j, l] = [11*0.5, 5]
# mag_moment = round(nf.MagneticDipoleMoment(A, Z, j, l, s), 2)
mag_moment = nf.MagneticDipoleMoment(A, Z, j, l)
print(f"For a Nucleus with A = {A}, Z = {Z}, j = {j} and l = {l}:\n" +
      f"--Magnetic moment: {mag_moment} mu_N \n")