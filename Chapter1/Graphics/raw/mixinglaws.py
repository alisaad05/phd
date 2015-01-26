sz=20

from matplotlib import rc
rc('font',**{'family':'serif','serif':['Palatino']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)
rc('axes', labelsize=sz)
rc('xtick', labelsize=sz)
rc('ytick', labelsize=sz)
rc('legend', fontsize=sz)
#===========
# USER DATA
#===========
eps = 4e-4 # 10.0
view_factor = 1.5
MIXING_LAW = "LINEAR"
gl_a= 0.0001
gl_m= 1.0
NbNodes= 100
#===========
# PLOT DATA
#===========
mf = 4
ms = 7
al= 1
#=======================================
from math import pi, sin, cos, fabs, log10, e, log
def heaviside(alpha):
	""" Computes a linear heaviside smoothed near the limits of the mixing zone """
	if      alpha > eps: return 1
	elif    alpha < (-1)*eps: return 0
	else:   return ( 0.5 * ( 1 + alpha/eps + (1/pi) * sin(pi*alpha/eps)) )
#========================================
def dirac(alpha):
	""" Computes a dirac smoothed near the limits of the mixing zone """
	if      fabs(alpha) < eps: return ( 0.5/eps * ( 1 + cos(pi*alpha/eps)) )
	else:   return 0
#========================================
def ARITHMETIC(alpha, psi_metal, psi_air):
	""" Computes an arithmetic mixing law """
	h_metal = heaviside(alpha)
	h_air = 1 - heaviside(alpha)
	
	return( psi_metal * h_metal + h_air * psi_air )
#========================================
def LOG(alpha, psi_metal, psi_air):
	""" Computes an arithmetic mixing law """
	h_metal = heaviside(alpha)
	h_air = 1 - heaviside(alpha)
	
	return( 10**(log10(psi_metal) * h_metal + log10(psi_air) * h_air) )
#========================================
def LN(alpha, psi_metal, psi_air):
	""" Computes an arithmetic mixing law """
	h_metal = heaviside(alpha)
	h_air = 1 - heaviside(alpha)
	
	return( e**(log(psi_metal) * h_metal + log(psi_air) * h_air) )
#========================================
def GEOMETRIC(alpha, psi_metal, psi_air):
	""" Computes an arithmetic mixing law """
	h_metal = heaviside(alpha)
	h_air = 1 - heaviside(alpha)
	
	return( (psi_metal**h_metal) + (psi_air** h_air) ) 
#========================================
def HARMONIC(alpha, psi_metal, psi_air):
	""" Computes an arithmetic mixing law """
	h_metal = heaviside(alpha)
	h_air = 1 - heaviside(alpha)
	
	return( 1/ (h_metal / psi_metal + h_air / psi_air ) ) 
#========================================

import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
heaviside = np.vectorize(heaviside)
dirac = np.vectorize(dirac)

# x = np.linspace(-view_factor*eps, view_factor*eps, NbNodes)
x = np.linspace(-eps, eps, NbNodes)

# dirac_normed = dirac(x) / float(dirac(x).max())
# ax.plot(dirac_normed, x, "y-^", lw =2, label = "Dirac (Normalized)", markevery= mf, ms= ms)

mu_m = 2e-3
mu_a = 1e-4

mu = ARITHMETIC(x,mu_m,mu_a)
# ax.plot(mu,	x, "b-o", lw =2, label = "Arithmetic", markevery= mf, ms= ms, alpha= al)
ax.plot(mu,	x, ls="-", marker="o", color=(0.8,0.8,0.8) , lw =2, label = "Arithmetic", markevery= mf, ms= ms, alpha= al)


mu = LOG(x,mu_m,mu_a)
#ax.plot(mu,	x, "m-s", lw =2, label = "LOG", markevery= mf, ms= ms, alpha= al)

mu = LN(x,mu_m,mu_a)
# ax.plot(mu,	x, "r-s", lw =2, label = "Logarithmic", markevery= mf*4, ms= ms, alpha= 1)
ax.plot(mu,	x, ls="-", marker="s", color=(0.5,0.5,0.5) , lw =2, label = "Logarithmic", markevery= mf, ms= ms, alpha= al)

mu = GEOMETRIC(x,mu_m,mu_a)
# mu /= float(mu.max())
# ax.plot(mu,	x, "y-^", lw =2, label = "Geometric", markevery= mf, ms= ms, alpha= al)

mu = HARMONIC(x,mu_m,mu_a)
ax.plot(mu,	x, ls="-", marker="d", color=(0.2,0.2,0.2) , lw =2, label = "Harmonic", markevery= mf, ms= ms, alpha= al)


fs = 15
ax.text(0.0001, 0.00065, '$\psi^{F_1}$',
        horizontalalignment='center',
        verticalalignment='center',
		fontsize=fs
		)
ax.text(0.002, 0.00065, '$\psi^{F_2}$',
        horizontalalignment='center',
        verticalalignment='center',
		fontsize=fs
		)
		
ax.axhline(y=eps, lw=2, ls="--", color="k")
ax.axhline(y=-eps, lw=2, ls="--", color="k")
ax.axhline(y=0, lw=2, ls="-", color="k")
ax.axvline(x=mu_a, lw=1, ls="-.", color="k")
ax.axvline(x=mu_m, lw=1, ls="-.", color="k")
legend = ax.legend(loc='best', shadow=True)
plt.xlabel('Material property $\widehat{\psi}$', fontsize=fs)
plt.ylabel('Distance', fontsize=fs)
# plt.title('Mixing laws')
plt.ylim(ymin= -view_factor*eps , ymax=view_factor*eps)
plt.xlim(xmin= mu_a*0.1 , xmax= mu_m*1.1)
plt.gca().invert_yaxis()
ax.xaxis.tick_top()

#====================
# SET CUSTOM AXIS LABEL
#====================
# a=ax.get_xticks().tolist() 
# a=[]
a=["","","","","",""]
ax.set_xticklabels(a) 

b=["","","","","",""]
b[5]="$-\\varepsilon$"
b[3]="$0$"
b[1]="$+\\varepsilon$"
ax.set_yticklabels(b) 
 
# ax.get_xaxis().set_visible(False)
# ax.get_yaxis().set_visible(False)
plt.grid()

# plt.show()
plt.savefig("mixing_laws.png",  dpi=300, bbox_inches='tight')
plt.savefig("mixing_laws.pdf",  dpi=300, bbox_inches='tight')
# plt.savefig("mixing_laws.svg",  dpi=300, bbox_inches='tight')
