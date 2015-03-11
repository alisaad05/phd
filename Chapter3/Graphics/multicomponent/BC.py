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
C2K = 0

x = np.arange(-10,10000,1)
# top = 1410+C2K -0.1*x
bottom = 1380+C2K-0.1*x

fig, ax = plt.subplots()
#ax.plot(x,top,
#        'b-o',
#        label='Top',
#        markevery=50)

ax.plot(x,bottom,
        'k-o',
        label='Bottom',
        markevery=500)
        
ls = "-"  
lw = 1
fs = 22
col = "k"
colorFCC, colorBCC, colorLIQ , colorM7C3, colorCEM= 'red', 'green', 'blue', 'orange', 'black'
markerFCC , markerBCC , markerLIQ , markerM7C3, markerCEM= '^', 'd', 'o', 'v', 'x'    
T1 = 1340 + C2K
T2 = 1305 + C2K
T3 = 1295 + C2K
T4 = 490  + C2K
plt.axhline(y=T1, linewidth=lw, color=col, linestyle= ls)
ax.annotate( '$T_{liquidus}^{BCC}$', fontsize=fs, xy=(4000, T1), xytext=(4000,T1-200),
            # arrowprops=dict(
								# facecolor='k', #sshrink=0.05, 
								# arrowstyle="-|>", connectionstyle="arc3"
							 # ),
			arrowprops=dict(arrowstyle="-|>", #linestyle="dashed",
                            color="r",
                            patchB=None,
                            shrinkB=0,
                            connectionstyle="arc3",
                            ),
			horizontalalignment='center', 
			verticalalignment='center',
			)
			
plt.axhline(y=T2, linewidth=lw, color=col, linestyle=ls)
ax.annotate( '$T_{solvus}^{FCC}$', fontsize=fs, xy=(6000, T2), xytext=(6000,T2-300),
            arrowprops=dict(arrowstyle="-|>", #linestyle="dashed",
                            color="r",
                            patchB=None,
                            shrinkB=0,
                            connectionstyle="arc3",
                            ),
            horizontalalignment='center', verticalalignment='center'
            )
plt.axhline(y=T3, linewidth=lw, color=col, linestyle=ls)
ax.annotate( '$T_{solvus}^{M_7C_3}$', fontsize=fs, xy=(8000, T3), xytext=(8000,T3-400),
            arrowprops=dict(arrowstyle="-|>", #linestyle="dashed",
                            color="r",
                            patchB=None,
                            shrinkB=0,
                            connectionstyle="arc3",
                            ),
            horizontalalignment='center', verticalalignment='center'
            )
plt.axhline(y=T4, linewidth=lw, color=col, linestyle=ls)
plt.text(700, T4+20, '$T_{solvus}^{CEM}$', fontsize=fs)        


legend = ax.legend(loc='best', shadow=True)
plt.xlabel('Time (sec)')
plt.ylabel('Temperature ($^\circ$C)')
# plt.title('Boundary conditions')
plt.xlim(0,10000)
#plt.ylim(1000,1800)
plt.grid()

#figManager = plt.get_current_fig_manager()
#figManager.window.showMaximized()
# plt.show()
plt.savefig("BC.png",  dpi=300, bbox_inches='tight')
plt.savefig("BC.pdf",  dpi=300, bbox_inches='tight')
