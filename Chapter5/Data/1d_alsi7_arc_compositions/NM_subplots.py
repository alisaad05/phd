# check http://matplotlib.org/users/customizing.html
sz=15
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

mSize = 6
# just to generate a legend with the color i want
mFreq = 100 #Mark plot every x number of points
mTransp = 0.75
c1 = 'k'
c2 = 'g'
c3 = 'm'
lw = 2
marker = itertools.cycle(('^','o', 'd'))  #randomize marker style

def modify_gs(gs):
	if gs ==1 : return 0
	else: return 1



def plot_composition_at_position(axis,data):
    axis.plot(data['arc_length'], data['Concentration'],  label=r"$\widehat{\left \langle w \right \rangle}$",  marker = marker.next(), color=c1, markersize=mSize, markevery=mFreq, alpha=mTransp, lw=lw)
    axis.plot(data['arc_length'], data['ConcentrationSolide'], label=r"$\left \langle w \right \rangle^s$",  marker = marker.next(), color=c2, markersize=mSize, markevery=mFreq*3, alpha=mTransp, lw=lw)
    axis.plot(data['arc_length'], data['ConcentrationLiquide']*modify_gs(data['FractionSolide_c']), label=r"$\left \langle w \right \rangle^l$", marker = marker.next(), color=c3, markersize=mSize, markevery=mFreq*3, alpha=mTransp, lw=lw)
    axis.set_xlim(0, 0.14)
    axis.set_ylim(0, 14)
#    axis.set_ylabel("Composition (wt.$\%$ Si)")
    axis.tick_params(axis='x', which='both', bottom='on', top='off', labelbottom='off')
    


def plot_density_at_position(axis,data):
    marker = itertools.cycle(('^'))  #randomize marker style
    axis.plot(data['arc_length'], data['DensityP1'], marker = marker.next(),label=r"$\widehat{\left \langle \rho \right \rangle}$",  color="b", markersize=mSize, markevery=mFreq, alpha=mTransp, lw=lw)
    axis.set_xlim(0, 0.14)
    axis.set_ylim(2550, 2850)
#    axis.set_ylabel("Average metal density (Kg m$^{-3}$)")
    axis.tick_params(axis='x', which='both', bottom='on', top='off', labelbottom='off')
    axis.tick_params(axis='y', which='both', bottom='off', top='off', labelbottom='off')
    

def plot_velocities_at_position(axis,data):
    vx , vy , gl, gs = data["Vitesse0"], data["Vitesse1"], data["FractionLiquide_c"], data["FractionSolide_c"]
    vavg = np.sqrt(vx*vx+vy*vy)
    # vintr = np.divide(vavg,gl) # ignored_states = np.seterr(**old_err_state)
    vintr = vavg/(1-gs)
    vintr[vintr>1e6]=0
    marker = itertools.cycle(('o', 'd'))  #randomize marker style
    axis.plot(data['arc_length'], vavg , marker = marker.next(), label=r"$\left \langle v^F \right \rangle$", color=(0.5,0,0.1), markersize=mSize, markevery=mFreq, alpha=mTransp, lw=lw)
    axis.plot(data['arc_length'], vintr, marker = marker.next(), label=r"$\left \langle v \right \rangle^F$", color="y", markersize=mSize, markevery=mFreq, alpha=mTransp, lw=lw)
    axis.set_xlim(0, 0.14)
    # axis.set_ylim(0, 5e-4)
#    axis.set_ylabel("Average metal density (Kg m$^{-3}$)")
    axis.tick_params(axis='x', which='both', bottom='on', top='off', labelbottom='off')
    axis.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

modify_gs = np.vectorize(modify_gs)
    
#****************************************************************************************************************************************    


input_columns = ("Concentration","ConcentrationSolide","ConcentrationLiquide","arc_length","FractionSolide_c","FractionLiquide_c", "DensityP1", "Vitesse0", "Vitesse1")     

delim= ','
z1 = np.genfromtxt('NM_200s.csv', delimiter=delim, skip_header=0, skip_footer=0, names=True ,  usecols=input_columns)
z3 = np.genfromtxt('NM_600s.csv', delimiter=delim, skip_header=0, skip_footer=0, names=True ,  usecols=input_columns )
z5 = np.genfromtxt('NM_800s.csv', delimiter=delim, skip_header=0, skip_footer=0, names=True , usecols=input_columns )

fig, ( (ax1, ax4, ax7),  
       (ax2, ax5, ax8),
       (ax3, ax6, ax9)) = plt.subplots(nrows=3, ncols=3)
		
fig.set_size_inches(20, 12)


# *****************************   COMPOSITIONS ********************************************************
# ax1.plot(0,0, marker = marker.next(), color=c1, markersize=mSize, label='Average composition', markevery=mFreq, alpha=mTransp, lw=lw)
# ax1.plot(0,0, marker = marker.next(), color=c2, markersize=mSize, label='Solid composition', markevery=mFreq, alpha=mTransp, lw=lw)
# ax1.plot(0,0, marker = marker.next(), color=c3, markersize=mSize, label='Liquid composition', markevery=mFreq, alpha=mTransp, lw=lw)

ax1.set_title("Average and phase compositions (wt.$\%$ Si)")
plot_composition_at_position(ax1,z1)
legend = ax1.legend(loc='best', shadow=False, fancybox=True)
plot_composition_at_position(ax2,z3)
plot_composition_at_position(ax3,z5)
ax3.tick_params(axis='x', which='both', bottom='on', top='off', labelbottom='on')
ax3.set_xlabel("Sample length (m)")
ax1.set_ylabel("t=200 s")
ax2.set_ylabel("t=600 s")
ax3.set_ylabel("t=800 s")
lgd = plt.legend(bbox_to_anchor=(0., 1.05, 1., .102), loc=1, ncol=3, mode="expand", borderaxespad=0., prop={'size':12}, fancybox=True,  shadow=True)

# *****************************   Density ********************************************************
ax4.set_title("Average metal density (Kg m$^{-3}$)")
plot_density_at_position(ax4,z1)
legend = ax4.legend(loc='best', shadow=False, fancybox=True)
plot_density_at_position(ax5,z3)
plot_density_at_position(ax6,z5)
ax6.tick_params(axis='x', which='both', bottom='on', top='off', labelbottom='on')
ax6.set_xlabel("Sample length (m)")

# *****************************   Velocities ********************************************************
ax7.set_title("Average and intrinsic velocities (m s$^{-1}$)")
plot_velocities_at_position(ax7,z1)
ax7.set_ylim(0, 3e-5)
legend = ax7.legend(loc='upper left', shadow=False, fancybox=True)
plot_velocities_at_position(ax8,z3)
ax8.set_ylim(0, 4e-5)
plot_velocities_at_position(ax9,z5)
ax9.tick_params(axis='x', which='both', bottom='on', top='off', labelbottom='on')
ax9.set_ylim(0, 2e-3)
ax9.set_xlabel("Sample length (m) ")

# ***************************************************************************************************
    
#plt.show()
plt.savefig('NM_subplots.png', dpi=300, bbox_inches='tight')
plt.savefig('NM_subplots.pdf', bbox_inches='tight')