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



mSize = 8
# just to generate a legend with the color i want
mFreq = 5 #Mark plot every x number of points
mTransp = 0.9
c1 = 'k'
c2 = 'g'
c3 = 'm'
lw = 2
marker = itertools.cycle(('^','o', 'd'))  #randomize marker style


#****************************************************************************************************************************************    


input_columns = ("Temperature","LIQ","ALPHA","BETA")     

delim= ','
z1 = np.genfromtxt('sp.csv', delimiter=delim, skip_header=0, skip_footer=0, names=True ,  usecols=input_columns)

fig, ax1 = plt.subplots()
	

# *****************************   COMPOSITIONS ********************************************************
ax1.plot(z1["Temperature"],z1["LIQ"], marker = marker.next(), color=c1, markersize=mSize, label='LIQ', markevery=mFreq, alpha=mTransp, lw=lw,ls="-")
ax1.plot(z1["Temperature"],z1["ALPHA"], marker = marker.next(), color=c1, markersize=mSize, label=r'$\alpha$', markevery=mFreq, alpha=mTransp, lw=lw,ls="--")
ax1.plot(z1["Temperature"],z1["BETA"], marker = marker.next(), color=c1, markersize=mSize, label='EUT', markevery=mFreq, alpha=mTransp, lw=lw,ls=":")

plt.ylim(-0.05,1.05)
plt.xlim(576,619)
plt.xlabel(r"Temperature [$^\circ$C]")
plt.ylabel("Volume fraction [-]")
legend1 = ax1.legend(loc='best', shadow=False, fancybox=True)

# plt.show()
plt.savefig('sp_plot.png', dpi=300, bbox_inches='tight')
plt.savefig('sp_plot.pdf', bbox_inches='tight')