# check http://matplotlib.org/users/customizing.html
sz=20
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)
rc('axes', labelsize=sz)
rc('xtick', labelsize=sz)
rc('ytick', labelsize=sz)
rc('legend', fontsize=sz)

import sys
reload(sys)
sys.setdefaultencoding("cp1252")
# sys.setdefaultencoding("utf-8")


dataT = np.genfromtxt('Tsolver_CC.txt', delimiter=None, skip_header=0, skip_footer=0, names=True , usecols=("Time","pos1","pos2","pos3","pos4","pos5" ,"pos6") )
dataH = np.genfromtxt('Hsolver_CC.txt', delimiter=None, skip_header=0, skip_footer=0, names=True , usecols=("Time","pos1","pos2","pos3","pos4","pos5" ,"pos6") )


timeT = dataT['Time']
timeH = dataH['Time']
y1,y2,y3,y4,y5,y6 = dataT['pos1'], dataT['pos2'], dataT['pos3'], dataT['pos4'], dataT['pos5'], dataT['pos6']
z1,z2,z3,z4,z5,z6  = dataH['pos1'], dataH['pos2'], dataH['pos3'], dataH['pos4'], dataH['pos5'], dataH['pos6']


fig, ax = plt.subplots()


alphaH = 1
orderH = 1
lw_H = 5
col_H = '#FF8000'
ax.plot(timeH, z1, color= col_H, lw= lw_H,    alpha=alphaH, label='Hsolver')
ax.plot(timeH, z2, color= col_H, lw= lw_H,    alpha=alphaH, zorder= orderH)
ax.plot(timeH, z3, color= col_H, lw= lw_H,	  alpha=alphaH, zorder= orderH)
ax.plot(timeH, z4, color= col_H, lw= lw_H,	  alpha=alphaH, zorder= orderH)
ax.plot(timeH, z5, color= col_H, lw= lw_H,	  alpha=alphaH, zorder= orderH)
ax.plot(timeH, z6, color= col_H, lw= lw_H,    alpha=alphaH, zorder= orderH)

alphaT = 1
orderT = 2
lw_T = 1
col_T = 'k'
ax.plot(timeT, y1, color= col_T, lw= lw_T,    alpha=alphaT, zorder= orderT, label='Tsolver')
ax.plot(timeT, y2, color= col_T, lw= lw_T,    alpha=alphaT, zorder= orderT)
ax.plot(timeT, y3, color= col_T, lw= lw_T,	  alpha=alphaT, zorder= orderT)
ax.plot(timeT, y4, color= col_T, lw= lw_T,	  alpha=alphaT, zorder= orderT)
ax.plot(timeT, y5, color= col_T, lw= lw_T,	  alpha=alphaT, zorder= orderT)
ax.plot(timeT, y6, color= col_T, lw= lw_T,    alpha=alphaT, zorder= orderT)

markerFT = "^"
markersizeFT = 7
NbMarkerFT = 300
ax.plot(timeT, y1, ls = "", color= col_T, lw= lw_T, marker = markerFT, markersize = markersizeFT,   markevery=NbMarkerFT, alpha=alphaT, zorder= orderT, label='Front Tracking')
ax.plot(timeT, y2, ls = "", color= col_T, lw= lw_T, marker = markerFT, markersize = markersizeFT, markevery=NbMarkerFT, alpha=alphaT, zorder= orderT)
ax.plot(timeT, y3, ls = "", color= col_T, lw= lw_T, marker = markerFT, markersize = markersizeFT,	markevery=NbMarkerFT, alpha=alphaT, zorder= orderT)
ax.plot(timeT, y4, ls = "", color= col_T, lw= lw_T, marker = markerFT, markersize = markersizeFT,	markevery=NbMarkerFT, alpha=alphaT, zorder= orderT)
ax.plot(timeT, y5, ls = "", color= col_T, lw= lw_T, marker = markerFT, markersize = markersizeFT,	markevery=NbMarkerFT, alpha=alphaT, zorder= orderT)
ax.plot(timeT, y6, ls = "", color= col_T, lw= lw_T, marker = markerFT, markersize = markersizeFT, markevery=NbMarkerFT, alpha=alphaT, zorder= orderT)


# plt.xlim(0,4500)
plt.ylim(570,630)
plt.grid(True)

legend = ax.legend(loc='best', fancybox=True, shadow=True)
plt.xlabel('Time (sec)')
plt.ylabel('Temperature ($^\circ$C)') # \xb0C
plt.title('Cooling Curves')

# Get artists and labels for legend and chose which ones to display
# handles, labels = ax.get_legend_handles_labels()
# display = (0,1,2)

# Create custom artists
# art = plt.Line2D((0,1),(0,0), color="k",  linestyle='', marker='^', linewidth=2)

# Create legend from custom artist/label lists
# fig.legend([handle for i,handle in enumerate(handles) if i in display]+[art],
         # [label for i,label in enumerate(labels) if i in display]+['Front Tracking Model'],loc='best', shadow=True)


# plt.show()
plt.savefig('diffusion_CC.pdf', bbox_inches='tight')
plt.savefig('diffusion_CC.png', dpi=300, bbox_inches='tight')

