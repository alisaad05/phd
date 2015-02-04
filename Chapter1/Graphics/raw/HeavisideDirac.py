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
NbNodes= 100
#===========
# PLOT DATA
#===========
mf = 4
ms = 7
al= 1
#=======================================
from math import pi, sin, cos, fabs
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

import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax2 = ax.twiny()
heaviside = np.vectorize(heaviside)
dirac = np.vectorize(dirac)

# x = np.linspace(-view_factor*eps, view_factor*eps, NbNodes)
x = np.linspace(-eps, eps, NbNodes)

# dirac_normed = dirac(x) / float(dirac(x).max())
ax.plot(heaviside(x), x, ls="-", marker="s", color=(0.8,0.8,0.8), lw =2, label = "Heaviside", markevery= mf, ms= ms, alpha=al)
ax2.plot(dirac(x), x, ls="-", marker="o", color=(0.4,0.4,0.4), lw =2, label = "Dirac", markevery= mf, ms= ms, alpha=al)
ax.plot(0,0, ls="-", marker="o", color=(0.4,0.4,0.4), lw =2, label = "Dirac", markevery= mf, ms= ms, alpha=al)

ax.axhline(y=eps, lw=2, ls="--", color="k")
ax.axhline(y=-eps, lw=2, ls="--", color="k")
ax.axhline(y=0, lw=2, ls="-", color="k")
legend = ax.legend(loc='best', fancybox=True, shadow=True)
ax.set_ylabel('Distance')
ax.set_xlabel('Heaviside')
ax2.set_xlabel('Dirac')
#plt.title('Mixing laws')
plt.ylim(ymin= -view_factor*eps , ymax=view_factor*eps)
ax.set_xticks(np.linspace(0, ax.get_xbound()[1], 5))
ax2.set_xticks(np.linspace(0, ax2.get_xbound()[1], 5))
ax.set_xlim(xmin=0, xmax=1.1)
ax2.set_xlim(xmin=0, xmax=dirac(x).max()*1.1)
plt.gca().invert_yaxis()
# ax.xaxis.tick_top()
 
ax.grid()  # <<<< ax and not plt, otherwise plt will assume that the grid belongs to ax2
 
#======================
# SET CUSTOM AXIS LABEL
#======================
a=ax.get_xticks().tolist() 
c=ax2.get_xticks().tolist() 
# a=["","","","","",""]
a[1]=""
c[1]=""
a[2]=""
c[2]=""
a[3]=""
c[3]=""
c[4]="$1/\\varepsilon$" # \\frac{1}{\\varepsilon}
ax.set_xticklabels(a) 
ax2.set_xticklabels(c) 

b=["","","","","",""]
b[5]="$-\\varepsilon$"
b[3]="$0$"
b[1]="$+\\varepsilon$"
ax.set_yticklabels(b) 
 
# ax.get_xaxis().set_visible(False)
# ax.get_yaxis().set_visible(False)


# plt.show()
plt.savefig("HeavisideDirac.png",  dpi=300, bbox_inches='tight')
plt.savefig("HeavisideDirac.pdf",  dpi=300, bbox_inches='tight')
