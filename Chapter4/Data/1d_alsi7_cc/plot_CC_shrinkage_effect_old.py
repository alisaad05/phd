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
fig, ax = plt.subplots()
fig.set_size_inches(10, 6.05)


foldername = 'no_macro_with_shrinkage'
z1 = np.genfromtxt(foldername+'\CapteurP1_1.xls', delimiter='\t', skip_header=0, skip_footer=0, names=True , usecols=("Temps","TemperatureC") )
z2 = np.genfromtxt(foldername+'\CapteurP1_2.xls', delimiter='\t', skip_header=0, skip_footer=0, names=True , usecols=("Temps","TemperatureC") )
z3 = np.genfromtxt(foldername+'\CapteurP1_3.xls', delimiter='\t', skip_header=0, skip_footer=0, names=True , usecols=("Temps","TemperatureC") )
z4 = np.genfromtxt(foldername+'\CapteurP1_4.xls', delimiter='\t', skip_header=0, skip_footer=0, names=True , usecols=("Temps","TemperatureC") )
z5 = np.genfromtxt(foldername+'\CapteurP1_5.xls', delimiter='\t', skip_header=0, skip_footer=0, names=True , usecols=("Temps","TemperatureC") )
z6 = np.genfromtxt(foldername+'\CapteurP1_6.xls', delimiter='\t', skip_header=0, skip_footer=0, names=True , usecols=("Temps","TemperatureC") )
z7 = np.genfromtxt(foldername+'\CapteurP1_7.xls', delimiter='\t', skip_header=0, skip_footer=0, names=True , usecols=("Temps","TemperatureC") )
z8 = np.genfromtxt(foldername+'\CapteurP1_8.xls', delimiter='\t', skip_header=0, skip_footer=0, names=True , usecols=("Temps","TemperatureC") )


mSize = 7
# just to generate a legend with the color i want
mFreq = 6000 #Mark plot every x number of points
mTransp = 1.0
c1 = 'k'
lw = 1
marker = itertools.cycle(('^','x', 'o', 'p', 'v','d','>','+'))  #randomize marker style
ax.plot(0,0, marker = marker.next(), color=c1, markersize=mSize, label='0 cm', markevery=mFreq, alpha=mTransp, lw=lw)
ax.plot(0,0, marker = marker.next(), color=c1, markersize=mSize, label='2 cm', markevery=mFreq, alpha=mTransp, lw=lw)
ax.plot(0,0, marker = marker.next(), color=c1, markersize=mSize, label='4 cm', markevery=mFreq, alpha=mTransp, lw=lw)
ax.plot(0,0, marker = marker.next(), color=c1, markersize=mSize, label='6 cm', markevery=mFreq, alpha=mTransp, lw=lw)
ax.plot(0,0, marker = marker.next(), color=c1, markersize=mSize, label='8 cm', markevery=mFreq, alpha=mTransp, lw=lw)
ax.plot(0,0, marker = marker.next(), color=c1, markersize=mSize, label='10 cm', markevery=mFreq, alpha=mTransp, lw=lw)
ax.plot(0,0, marker = marker.next(), color=c1, markersize=mSize, label='12 cm', markevery=mFreq, alpha=mTransp, lw=lw)
ax.plot(0,0, marker = marker.next(), color=c1, markersize=mSize, label='14 cm', markevery=mFreq, alpha=mTransp, lw=lw)


c2 = 'b'
mTransp = 1.0
mFreq = 6000 #Mark plot every x number of points
marker = itertools.cycle(('^','x', 'o', 'p', 'v','d','>','+'))  #randomize marker style

ax.plot(z1['Temps'], z1['TemperatureC'], marker = marker.next(), color=c2, markersize=mSize, markevery=mFreq, alpha=mTransp, lw=lw)
ax.plot(z2['Temps'], z2['TemperatureC'], marker = marker.next(), color=c2, markersize=mSize, markevery=mFreq, alpha=mTransp, lw=lw)
ax.plot(z3['Temps'], z3['TemperatureC'], marker = marker.next(), color=c2, markersize=mSize, markevery=mFreq, alpha=mTransp, lw=lw)
ax.plot(z4['Temps'], z4['TemperatureC'], marker = marker.next(), color=c2, markersize=mSize, markevery=mFreq, alpha=mTransp, lw=lw)
ax.plot(z5['Temps'], z5['TemperatureC'], marker = marker.next(), color=c2, markersize=mSize, markevery=mFreq, alpha=mTransp, lw=lw)
ax.plot(z6['Temps'], z6['TemperatureC'], marker = marker.next(), color=c2, markersize=mSize, markevery=mFreq, alpha=mTransp, lw=lw)
# ax.plot(z7['Temps'], z7['TemperatureC'], marker = marker.next(), color=c2, markersize=mSize, markevery=mFreq, alpha=mTransp, lw=lw)
# ax.plot(z8['Temps'], z8['TemperatureC'], marker = marker.next(), color=c2, markersize=mSize, markevery=mFreq, alpha=mTransp, lw=lw)

foldername = 'no_macro_no_shrinkage_noLS'
z1 = np.genfromtxt(foldername+'\Tsolver_CC.txt', delimiter='\t', skip_header=0, skip_footer=0, names=True , usecols=("Temps","pos1","pos2","pos3","pos4","pos5","pos6") )
c1 = (0.4,0.4,0.4)
mFreq = 3000 #Mark plot every x number of points
mTransp = 0.75
lw=3
marker = itertools.cycle(('^','x', 'o', 'p', 'v','d','>','+'))  #randomize marker style
ax.plot(z1['Temps'], z1['pos1'], marker = marker.next(), color=c1, markersize=mSize,  markevery=mFreq, alpha=mTransp, lw=lw)
ax.plot(z1['Temps'], z1['pos2'], marker = marker.next(), color=c1, markersize=mSize,  markevery=mFreq, alpha=mTransp, lw=lw)
ax.plot(z1['Temps'], z1['pos3'], marker = marker.next(), color=c1, markersize=mSize,  markevery=mFreq, alpha=mTransp, lw=lw)
ax.plot(z1['Temps'], z1['pos4'], marker = marker.next(), color=c1, markersize=mSize,  markevery=mFreq, alpha=mTransp, lw=lw)
ax.plot(z1['Temps'], z1['pos5'], marker = marker.next(), color=c1, markersize=mSize, markevery=mFreq, alpha=mTransp, lw=lw)
ax.plot(z1['Temps'], z1['pos6'], marker = marker.next(), color=c1, markersize=mSize,  markevery=mFreq, alpha=mTransp, lw=lw)





## Plot and annotate liquidus temperature
# Tliq = plt.axhline(y=618, linewidth=1, color='k')
# Tliq.set_linestyle('--')
# plt.text(10, 625, r'$T_{L}$')

## Plot and annotate eutectic temperature
# Teut = plt.axhline(y=577, linewidth=1, color='k')
# Teut.set_linestyle('--')
# plt.text(10, 583, r'$T_{E}$')

plt.xlim(0, 1000)
plt.ylim(350, 810)

## Show background grid
# plt.grid(True)

# lgd = plt.legend(bbox_to_anchor=(0., -0.3, 1., .102), loc=1,
lgd = plt.legend(bbox_to_anchor=(0., 1.05, 1., .102), loc=1,
           ncol=8, mode="expand", borderaxespad=0., prop={'size':12}, fancybox=True,  shadow=True)	
		   
plt.xlabel('Time (s)')
plt.ylabel('Temperature ($^\circ$C)')
# plt.title('Cooling Curves $T(t)$')

# plt.show()
plt.savefig('shrinkage_effect.png', dpi=300, bbox_inches='tight')
plt.savefig('shrinkage_effect.pdf', bbox_inches='tight',bbox_extra_artists=(lgd,))