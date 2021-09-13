import matplotlib as plt
import scipy
import random
import math
import numpy

e = math.e
pi = math.pi
h_dash = 6.582119569*10**(-16) / 510 #Blanc constans in m_ec^2 (I think) #There was mistake in this line before

#parameters
B_cr = 4.41 * 10**13 #critical quantum value
B_prim = 0.7 
B_0 = 0.7 * B_cr #aprox. of PSR 1509-58

B = lambda r : B_0 * r**(-3) # dipol magnetic field magnitude in flat spacetime 

theta = 0 #magnetic colitude
theta_k = 0 #angle 
z_0 = 0 #distance from the surface 

#partial splitting cascade
e_min = 10**(-3)
e_max = 100
alpha = 1.6
N_0 = 10**6 #number of photons simulated 

N = lambda epsilon : N_0 *  epsilon ** (-1. * alpha)

#attenuation coefficient for photon splitting for _|_ -> || || polarization
T_sp = lambda theta_k, omega :  1.3631218166086345*10**(-24) * omega * (math.sin(theta_k))**6 ##aprox. value I got from all the constants in ex. 1 and 3 from paper for B' = 0.7 

#attenuation coefficient for pair production
p = lambda j, k, omega, theta_k : (omega**2 / 4 * math.sin(theta_k)**2 - 1 - (j + k) * B_prim + ((j-k)*B_prim / (omega*math.sin(theta_k)))**2 )**(1/2)
E_0 = lambda omega, theta_k : (1 + p(0, 1, omega, theta_k)**2)**(1/2)
E_1 = lambda omega, theta_k : (1 + p(0, 1, omega, theta_k)**2 + 2*B_prim)**(1/2)
# || ||
T_pp0 = lambda theta_k, omega :  2.6463117553040002*10**(-14) * e**(- omega**2 / 1.4 * math.sin(theta_k))/(omega**2 * math.sin(theta_k) * (omega**2/4 * math.sin(theta_k)**2 - 1)**(1/2))
# _|_
T_pp1 = lambda theta_k, omega :  2.6463117553040002*10**(-14) * e**(- omega**2 / 1.4 * math.sin(theta_k)) * (E_0(omega, theta_k)*E_1(omega, theta_k) + 1 + p(0, 1, omega, theta_k)**2) /(omega**2 * math.sin(theta_k) * p(0, 1, omega, theta_k))


def get_rand_pol(): #random polarization
    rand = random.uniform(0,1)
    if (rand > 0.5): 
        return 1
    else:
        return 0


def power_distribution(alpha = 1.6):
    u = random.uniform(0,1)
    rand = - 14.85 + 15.85*u
    x = pow(1.-rand,-1./(alpha-1.))
    return x


class Photon:
    def __init__(self, pol, energy):
        self.pol = get_rand_pol()
        self.energy = energy

    def get_pol(self):
        return self.pol 

    def get_energy(self):
        return self.energy/h_dash

def main():
    for in range(N_0):
        energy = power_distribution() 
        Random_Photon = Photon(1, energy)
        R1 = random.uniform(0,1)
        R2 = random.uniform(0,1)
        P_s = math.exp( -scipy.integrate.quad( T_sp(theta_k, Random_Photon.get_energy()) , 0, s))
        P_pp0 = math.exp( -scipy.integrate.quad( T_pp0(theta_k, Random_Photon.get_energy()) , 0, s))
        P_pp1 = math.exp( -scipy.integrate.quad( T_pp1(theta_k, Random_Photon.get_energy()) , 0, s))
