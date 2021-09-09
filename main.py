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
B_0 = 0.7 * B_cr #aprox. of PSR 1509-58
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
T_sp = lambda thetha_k, omega :  1223575244542.2058 * omega * (math.sin(thetha_k))**6 ##aprox. value I got from all the constants in ex. 1 and 3 from paper for B' = 0.7 

#attenuation coefficient for pair production
#TBA


def get_rand_pol(): #random polarization
    rand = random.uniform(0,1)
    if (rand > 0.5): 
        return 1
    else:
        return 0

def get_rand_energy(minimum, maximum):
    size = maximum - minimum
    u = random.uniform(0,1)
    return e_min + size*u

def power_law_distribution(N_0, minimum, maximum):
    size = maximum - minimum
    rand = random.uniform(0,1)
    u = e_min + size*rand
    return (u/N_0)**(1/alpha)


class Photon:
    def __init__(self, pol, energy):
        self.pol = get_rand_pol()
        self.energy = energy

    def energy_to_omega(self, energy):
        return energy/h_dash

def main():
    for in range(N_0):
        energy = get_rand_energy(e_min, e_max) 
        for in range(N(energy)):
            Random_Photon = Photon(1, energy)



def f_of_x(x):
    """
    This is the main function we want to integrate over.
    Args:
    - x (float) : input to function; must be in radians
    Return:
    - output of function f(x) (float)
    """
    return (e**(-1*x))/(1+(x-1)**2)

def crude_monte_carlo(num_samples=5000):
    """
    This function performs the Crude Monte Carlo for our
    specific function f(x) on the range x=0 to x=5.
    Notice that this bound is sufficient because f(x)
    approaches 0 at around PI.
    Args:
    - num_samples (float) : number of samples
    Return:
    - Crude Monte Carlo estimation (float)
    

    lower_bound = 0
    upper_bound = 5
    
    sum_of_samples = 0
    for i in range(num_samples):
        x = get_rand_number(lower_bound, upper_bound)
        sum_of_samples += f_of_x(x)
    
    return (upper_bound - lower_bound) * float(sum_of_samples/num_samples)
    """