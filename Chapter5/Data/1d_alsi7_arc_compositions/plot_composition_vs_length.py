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

mSize = 8
# just to generate a legend with the color i want
mFreq = 100 #Mark plot every x number of points
mTransp = 0.5
c1 = 'k'
c2 = 'g'
c3 = 'm'
lw = 3
marker = itertools.cycle(('^','o', 'd'))  #randomize marker style

def modify_gs(gs):
	if gs ==1 : return 0
	else: return 1

modify_gs = np.vectorize(modify_gs)

def plot_given_at_position(axis,data):
	axis.plot(data['arc_length'], data['Concentration'], marker = marker.next(), color=c1, markersize=mSize, markevery=mFreq, alpha=mTransp, lw=lw)
	axis.plot(data['arc_length'], data['ConcentrationSolide'], marker = marker.next(), color=c2, markersize=mSize, markevery=mFreq*3, alpha=mTransp, lw=lw)
	axis.plot(data['arc_length'], data['ConcentrationLiquide']*modify_gs(data['FractionSolide_c']), marker = marker.next(), color=c3, markersize=mSize, markevery=mFreq*3, alpha=mTransp, lw=lw)

delim= ','
z1 = np.genfromtxt('200s.csv', delimiter=delim, skip_header=0, skip_footer=0, names=True ,  usecols=("Concentration","ConcentrationSolide","ConcentrationLiquide","arc_length","FractionSolide_c") )
z2 = np.genfromtxt('400s.csv', delimiter=delim, skip_header=0, skip_footer=0, names=True ,  usecols=("Concentration","ConcentrationSolide","ConcentrationLiquide","arc_length","FractionSolide_c") )
z3 = np.genfromtxt('600s.csv', delimiter=delim, skip_header=0, skip_footer=0, names=True ,  usecols=("Concentration","ConcentrationSolide","ConcentrationLiquide","arc_length","FractionSolide_c") )
z4 = np.genfromtxt('800s.csv', delimiter=delim, skip_header=0, skip_footer=0, names=True ,  usecols=("Concentration","ConcentrationSolide","ConcentrationLiquide","arc_length","FractionSolide_c") )
z5 = np.genfromtxt('1000s.csv', delimiter=delim, skip_header=0, skip_footer=0, names=True , usecols=("Concentration","ConcentrationSolide","ConcentrationLiquide","arc_length","FractionSolide_c") )
Z = [z1,z2,z3,z4,z5]

fig, ax = plt.subplots()
fig.set_size_inches(10, 6.05)

ax.plot(0,0, marker = marker.next(), color=c1, markersize=mSize, label='Average composition', markevery=mFreq, alpha=mTransp, lw=lw)
ax.plot(0,0, marker = marker.next(), color=c2, markersize=mSize, label='Solid composition', markevery=mFreq, alpha=mTransp, lw=lw)
ax.plot(0,0, marker = marker.next(), color=c3, markersize=mSize, label='Liquid composition', markevery=mFreq, alpha=mTransp, lw=lw)

plot_given_at_position(ax,z3)

plt.xlim(0, 0.14)
# plt.ylim(350, 810)

## Show background grid
# plt.grid(True)

# lgd = plt.legend(bbox_to_anchor=(0., -0.3, 1., .102), loc=1,
lgd = plt.legend(bbox_to_anchor=(0., 1.05, 1., .102), loc=1,
           ncol=3, mode="expand", borderaxespad=0., prop={'size':12}, fancybox=True,  shadow=True)	
		   
plt.xlabel('Sample length (m)')
plt.ylabel('Composition (wt.$\%$ Si)')
# plt.title('Cooling Curves $T(t)$')

# plt.show()
plt.savefig('compositions_vs_length.png', dpi=300, bbox_inches='tight')
plt.savefig('compositions_vs_length.pdf', bbox_inches='tight',bbox_extra_artists=(lgd,))