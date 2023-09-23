import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Defines function to check nucleus type
def NucleusType(A, Z):
    """ Assigns 0 to even-even, 1 to odd-odd nuclei, and 2 to even-odd"""
    
    if A % 2 == 0 and Z % 2 == 0:
        nucl_type = 0 # even-even
    if A % 2 == 0 and Z % 2 != 0:
        nucl_type = 1 # odd-odd
    else:
        nucl_type = 2 # even-odd
    return nucl_type

# Defines Bethe Weiszäcker formula
def BindingEnergy(A, Z):
    
    # Defines constants
    a = 15.835 # MeV
    b = 18.33 # MeV
    d = 0.7140 # MeV
    s = 23.20 # MeV
    delta_list = [-11.2, -11.2, 0] # MeV
    
    # Assigns value of delta depending on nucleus type
    nucl_type = NucleusType(A, Z)
    delta = delta_list[nucl_type] # MeV
        
    # Computes binding energy
    B  = a*A - b*A**(2/3) - d*(Z**2)/(A**(1/3)) - s*((A-2*Z)**2)/A - delta/(A**(1/2))
    return B

# Defines function to compute nuclear mass
def NuclearMass(A, Z):
    
    # Defines constants
    m_p = 938.2720813 # MeV/c^2
    m_n = 939.5654133 # MeV/c^2
    m_e = 0.51099895 # MeV/c^2
    m_u = 931.49410242 # MeV/c^2
    
    # Computes mass
    M = Z*m_p + (A-Z)*m_n - BindingEnergy(A,Z) # MeV/c^2
    return M

# Defines function to compute nuclear radius
def NuclearRadius(A):
    return 1.12*A**(1/3) #- 0.86*A**(-1/3) # fm

# Defines function to compute nuclear magentic dipole moment
def MagneticDipoleMoment(A, Z, j, l):
    """ Works for even-even, even-odd, and odd-even nuclei."""
    
    # Checks that A, Z and j are valid
    error_msg_0 = ("A must be greater than or equal to Z"+ 
                   "and greater than or equal to 1")
    error_msg_1 = "j must be greater than or equal to 0.5"
    assert A >= 1 and A >= Z, error_msg_0
    # assert j >= 0.5, error_msg_1
    
    s = 0.5 # Spin of nucleon
    g_p = 5.586 # Proton g-factor
    g_n = -3.826 # Neutron g-factor
    
    # Check nucleus type
    nucl_type = NucleusType(A, Z)
    if nucl_type == 0:
        moment = 0 # Nuclear magneton
    if nucl_type == 2:
        # Checks if the unpaired nucleon is a proton or neutron
        if Z % 2 != 0:
            g_s = g_p
            g_l = 1
        else:
            g_s = g_n
            g_l = 0
        moment = ((g_l+g_s)*j +(g_l-g_s)*((l-s)*(l+s+1)/(j+1))) # Nuclear magneton
    
    return 0.5*moment # *Nuclear magneton

def ProtonScattering(E_i, E_f, M, theta):
    """ Computes the energy of a proton after scattering off a nucleus.
    
    Parameters
    ----------
    E_i : float
        Initial energy of proton in MeV.
    E_f : float
        Final energy of proton in MeV.
    M : float
        Mass of nucleus in MeV/c^2.
    theta : float
        Scattering angle in radians.
    
    Returns
    -------
    delta_E : float
        Energy change of proton in MeV.
    """
    # Computes energy separation
    m_p = 938.2720813 # MeV/c^2
    m_ratio = m_p/M
    delta_E = (1-m_ratio)*E_i - (1+m_ratio)*E_f 
    delta_E += 2*m_ratio*np.sqrt(E_i*E_f)*np.cos(theta)
    data = np.array([E_f, delta_E]).T

    # Creates Dataframe and makes it Pretty
    df = pd.DataFrame(data)
    df.columns = ["Proton energy E_f (MeV)",
                  "Energy level separation E (MeV)"]
    pd.set_option("display.precision", 3)
    
    
    return df #MeV