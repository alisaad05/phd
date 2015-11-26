# check http://matplotlib.org/users/customizing.html
sz=20
import numpy as np
import matplotlib.pyplot as plt
import itertools
from matplotlib import rc
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)
rc('axes', labelsize=sz)
rc('xtick', labelsize=sz)
rc('ytick', labelsize=sz)
rc('legend', fontsize=sz)

# col = itertools.cycle(( (0.3,0.3,0.3), (0.4,0.4,0.4),(0.5,0.5,0.5),(0.65,0.65,0.65), (0.75,0.75,0.75),(0.9,0.9,0.9)))  #randomize marker style
# col = itertools.cycle(('g', 'b', 'r', 'c', 'y', 'k', 'm'))  #randomize color
# col = itertools.cycle((grey))
# plt.figure(1)

fn = "global_smacs"
z1 = np.genfromtxt(fn+".txt", delimiter='\t', skip_header=0, skip_footer=1000, names=True , usecols=("Temps","msoluteM", "mA", "mM","vA","vM") )
mSize = 9
mFreq = 2500 #Mark plot every x number of points
mTransp = 0.85
cA = 'g'
cM = "m"
gray = (0.2,0.2,0.2)
gray2 = (0.7,0.7,0.7)
lw = 2
marker = itertools.cycle(('^','o', 'd'))  #randomize marker style

fig, ax = plt.subplots()

# metalmass_0 = z1['mM'][0]
# solutemass_0 = z1['msoluteM'][0]
# metalmass_pct = 100*(z1['mM']-metalmass_0)/metalmass_0
# solutemass_pct = 100*(z1['msoluteM']-solutemass_0)/solutemass_0
 
ax.plot(z1['Temps'],  z1['mA'] , marker = "o", label=r"$m^A$", color=cA, markersize=mSize, markevery=mFreq, alpha=mTransp, lw=lw)
ax.plot(z1['Temps'],  z1['mM'] , marker = "s", label=r"$m^M$", color=cM, markersize=mSize, markevery=mFreq, alpha=mTransp, lw=lw)
ax.set_xlim(1750,4250)
ax.set_ylim(-0.5,55)
mTransp = 0.6
# vA0 = z1['vA'][0]
# vM0 = z1['vM'][0]
# vA_pct = 100*(z1['vA']-vA0)/vA0
# vM_pct = 100*(z1['vM']-vM0)/vM0
ax2 = ax.twinx()
ax2.plot(z1['Temps'], z1['vA'] , marker = "o", label=r"$V^A$", color=cA, markersize=mSize, markevery=mFreq, alpha=mTransp, lw=lw, ls="--" )
ax2.plot(z1['Temps'], z1['vM'] , marker = "s", label=r"$V^M$", color=cM, markersize=mSize, markevery=mFreq, alpha=mTransp, lw=lw, ls="--")
ax2.set_ylim(0.001,0.008)
ax2.set_xlim(1750,4250)

ax.set_xlabel('Time (s)')
ax.set_ylabel("Mass change (Kg)")
ax2.set_ylabel("Volume change (m$^3$)")
legend_mass = ax.legend(loc='center left', shadow=False, fancybox=True)
legend_volume = ax2.legend(loc='center right', shadow=False, fancybox=True)

# plt.grid(True)
ax.grid(b=True)
# plt.show()
plt.savefig(fn+"_metal"+".png", dpi=300, bbox_inches='tight')
plt.savefig(fn+"_metal"+".pdf", bbox_inches='tight')