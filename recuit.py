 
import math
from graphe import *

T0 = 100 # temperature initiale
S0 = [] # solution initiale
N = 50 # nombre d'itéraion

def find_soluce(S):
    pass

def distance_tot(S: list[Node]):
    d = 0
    for (i, n) in enumerate(S[:-2]):
        d+=n.distance(S[i+1])
    d+=S[-2].distance(S[-1])
    d+=S[0].distance(S[-1])
    return d

def alea(a, b):
    return np.random.uniform() # un nombre aleatoire entre 0 et 1 normalement

def metropolis(S1, S, T):
    if distance_tot(S1) < distance_tot(S):
        return S1
    elif alea(0,1) > math.exp((distance_tot(S1) - distance_tot(S))/T):
        return S1
    return S

def recuit():
    T = T0
    S = S0
    S1 = find_soluce(S)
    S = metropolis(S1, S, T)
    T = 0.9 * T
